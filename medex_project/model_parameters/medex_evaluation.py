import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def evaluate_medex_model(model_path, test_data, device):
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    model.to(device)
    model.eval()

    predictions = []
    true_labels = []

    with torch.no_grad():
        for text, label in test_data:
            inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
            inputs = {key: value.to(device) for key, value in inputs.items()}
            outputs = model(**inputs)
            _, predicted_label = torch.max(outputs.logits, 1)

            predictions.append(predicted_label.item())
            true_labels.append(label)

    accuracy = accuracy_score(true_labels, predictions)
    precision, recall, f1_score, _ = precision_recall_fscore_support(true_labels, predictions, average="weighted")

    return accuracy, precision, recall, f1_score