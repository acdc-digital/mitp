import os
import torch
from sentence_transformers import SentenceTransformer
from medex_project.ml_module import Unstructured  # Replace `your_ml_module` with your actual module name
from medex_project.preprocessing.clean_data import clean_data
from medex_project.preprocessing.split_data import split_data
from medex_project.data.medical_corpus import MedicalCorpus
from medex_project.data.user_data_corpus import UserDataCorpus
from medex_project.model_parameters.medex_language_model import MedexLanguageModel
from medex_project.model_parameters.medex_hyperparameters import MedexHyperparameters
from medex_project.model_parameters.train_model import train_medex_model
from medex_project.model_parameters.evaluate_model import evaluate_medex_model
import faiss

unstructured_instance = Unstructured()
UPLOAD_FOLDER = 'uploads'
sentence_transformer_model = SentenceTransformer('stanford-crfm/BioMedLM')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#The key point is that the model has learned useful representations of words,
# and you're leveraging these representations for your task.

def get_user_id(filename):
    return filename.split('_')[0]

def get_privacy_data(user_id):
    # Assume you have a function named `get_privacy_data_from_db` in your database module
    # that retrieves a user's privacy data
    from your_database_module import get_privacy_data_from_db  # Replace `your_database_module` with your actual module name
    return get_privacy_data_from_db(user_id)

def get_embeddings(text_data: list, model: SentenceTransformer):
    return model.encode(text_data)

def load_data_from_uploads():
    medical_corpus = MedicalCorpus()
    user_data_corpus = UserDataCorpus()

    filenames = os.listdir(UPLOAD_FOLDER)

    documents = []
    for filename in filenames:
        documents.append(process_and_get_embeddings(filename))

    # Convert documents to embeddings
    doc_texts = [doc['text'] for doc in documents]
    embeddings = sentence_transformer_model.encode(doc_texts)

    # Initialize a new Faiss index
    index = faiss.IndexFlatL2(embeddings.shape[1])

    # Add the document vectors to the Faiss index
    index.add(embeddings)

    return index, documents

def process_and_get_embeddings(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    user_data = unstructured_instance.process_file(file_path)

    user_id = get_user_id(filename)
    privacy_data = get_privacy_data(user_id)

    clean_data(medical_corpus, privacy_data, user_data_corpus)

    # Leave labels as None for now
    labels = None
    train_data, test_data, train_labels, test_labels = split_data(user_data, labels)

    # Get embeddings using sentence transformers
    embeddings_train_data = get_embeddings(train_data, sentence_transformer_model)
    embeddings_test_data = get_embeddings(test_data, sentence_transformer_model)

    # Prepare the data for model training
    train_data_for_model = embeddings_train_data
    test_data_for_model = embeddings_test_data

    # Train the model
    model = MedexLanguageModel("stanford-crfm/BioMedLM")  # Initialize model
    hyperparameters = MedexHyperparameters().get_hyperparameters()  # Get hyperparameters
    model, _ = train_medex_model(model, train_data_for_model, hyperparameters)  # Train the model

    # Evaluate the model
    accuracy, precision, recall, f1_score = evaluate_medex_model(model, test_data_for_model, device)

    # Use the trained model to update embeddings
    updated_embeddings_train_data = model.encode(train_data).tolist()
    updated_embeddings_test_data = model.encode(test_data).tolist()

    return {'doc_id':

