import unittest
import os
from unittest.mock import patch
import torch
from sentence_transformers import SentenceTransformer
from medex_project.data.medical_corpus import MedicalCorpus
from medex_project.data.user_data_corpus import UserDataCorpus
from medex_project.model_parameters.medex_language_model import MedexLanguageModel
from medex_project.model_parameters.medex_hyperparameters import MedexHyperparameters
from medex_project.model_training.train_model import train_medex_model
from medex_project.model_evaluation.evaluate_model import evaluate_medex_model
import faiss

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.UPLOAD_FOLDER = 'test_uploads'
        os.makedirs(self.UPLOAD_FOLDER, exist_ok=True)

    def tearDown(self):
        os.rmdir(self.UPLOAD_FOLDER)

    @patch('medex_project.model_training.train_model.MedexLanguageModel')
    @patch('medex_project.model_evaluation.evaluate_model.evaluate_medex_model')
    @patch('medex_project.data.medical_corpus.MedicalCorpus')
    @patch('medex_project.data.user_data_corpus.UserDataCorpus')
    @patch('medex_project.ml_module.Unstructured')
    @patch('medex_project.model_parameters.medex_hyperparameters.MedexHyperparameters')
    @patch('medex_project.model_parameters.medex_language_model.SentenceTransformer')
    def test_load_data_from_uploads(self, mock_sentence_transformer, mock_hyperparameters, mock_unstructured,
                                   mock_user_data_corpus, mock_medical_corpus, mock_evaluate_medex_model,
                                   mock_medex_language_model):
        # Mock objects
        mock_sentence_transformer.return_value = SentenceTransformer('stanford-crfm/BioMedLM')
        mock_hyperparameters.return_value = MedexHyperparameters()
        mock_unstructured_instance = mock_unstructured.return_value
        mock_unstructured_instance.process_file.return_value = {'text': 'sample text'}
        mock_user_data_corpus_instance = mock_user_data_corpus.return_value
        mock_user_data_corpus_instance.load_user_data.return_value = {'1': 'sample data'}
        mock_medical_corpus_instance = mock_medical_corpus.return_value
        mock_medical_corpus_instance.load_medical_corpus.return_value = {'1': 'sample data'}
        mock_medex_language_model_instance = mock_medex_language_model.return_value
        mock_medex_language_model_instance.encode.return_value = torch.tensor([[1, 2, 3]])

        # Create test files
        filenames = ['1_test.txt', '2_test.txt']
        for filename in filenames:
            with open(os.path.join(self.UPLOAD_FOLDER, filename), 'w') as f:
                f.write('sample text')

        # Run the function
        from index import load_data_from_uploads
        index, documents = load_data_from_uploads()

        # Assertions
        self.assertIsInstance(index, faiss.IndexFlatL2)
        self.assertEqual(len(documents), 2)
        self.assertEqual(documents[0]['doc_id'], '1_test')
        self.assertEqual(documents[1]['doc_id'], '2_test')

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()