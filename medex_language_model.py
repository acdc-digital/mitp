from transformers import AutoModelForSequenceClassification, AutoTokenizer

class MedexLanguageModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Add any additional methods or functionality to the MedexLanguageModel class

def get_medex_language_model(model_name):
    return MedexLanguageModel(model_name)
