from medex_project.data.medical_corpus import MedicalCorpus
from medex_project.data.privacy_data import PrivacyData
from medex_project.data.user_data_corpus import UserDataCorpus
from medex_project.preprocessing.clean_data import clean_data
from medex_project.preprocessing.split_data import split_data
from medex_project.preprocessing.tokenize_data import tokenize_data
from medex_project.model_parameters.medex_hyperparameters import MedexHyperparameters
from medex_project.model_parameters.medex_language_model import get_medex_language_model
from medex_project.model_parameters.medex_training import train_medex_model
from medex_project.model_parameters.medex_evaluation import evaluate_medex_model
from medex_project.utils.privacy_filter import apply_privacy_filter
from medex_project.utils.interpretation import interpret_medical_data
from medex_project.utils.save_load_model import save_model, load_model


def main():
    # Define user_id and sensitive_data
    user_id = 123  # Replace with the actual user ID
    sensitive_data = "Some sensitive data"  # Replace with the actual sensitive data

    # Create PrivacyData instance
    privacy_data = PrivacyData(user_id, sensitive_data)

    # Try-except blocks to handle potential errors
    try:
        # Load data
        medical_corpus = MedicalCorpus("medex_project/data/medical_corpus.json")
        user_data_corpus = UserDataCorpus("medex_project/data/user_data")
        # Update with the correct directory path
    except FileNotFoundError as e:
        print("Unable to load data:", e)
        return

    # Preprocess data
    clean_data(medical_corpus, privacy_data, user_data_corpus)
    train_data, test_data = split_data(medical_corpus)
    train_data_tokenized, test_data_tokenized = tokenize_data(train_data, test_data)

    # Set up model parameters
    hyperparameters = MedexHyperparameters()

    try:
        language_model, tokenizer = get_medex_language_model(hyperparameters.medex_language_model)
    except ImportError as e:
        print("Unable to import MedexLanguageModel:", e)
        return

    # Train and evaluate the model
    train_medex_model(language_model, train_data_tokenized, hyperparameters)
    evaluation_results = evaluate_medex_model(language_model, test_data_tokenized)

    # Apply privacy filter and interpret medical data
    filtered_data = apply_privacy_filter(user_data_corpus, privacy_data)
    interpreted_data = interpret_medical_data(filtered_data, language_model, tokenizer)

    # Save and load the model
    save_model(language_model, "medex_language_model.pth")

    try:
        loaded_model = load_model("medex_language_model.pth")
    except Exception as e:
        print("Unable to load the saved model:", e)
        return


