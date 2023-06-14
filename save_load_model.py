import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def save_model(model, tokenizer, model_name):
    model.save_pretrained(f"models/{model_name}")
    tokenizer.save_pretrained(f"models/{model_name}")

def load_model(model_name):
    model = AutoModelForSequenceClassification.from_pretrained(f"models/{model_name}")
    tokenizer = AutoTokenizer.from_pretrained(f"models/{model_name}")
    return model, tokenizer