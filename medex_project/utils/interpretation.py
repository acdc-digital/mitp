from transformers import pipeline

def interpret_medical_data(text):
    model_name = "distilbert-base-uncased"
    tokenizer_name = "distilbert-base-uncased"
    nlp = pipeline("question-answering", model=model_name, tokenizer=tokenizer_name)

    questions = [
        "What is the main medical issue?",
        "What are the symptoms?",
        "What is the diagnosis?",
        "What is the treatment plan?",
    ]

    interpretations = {}
    for question in questions:
        result = nlp(question=question, context=text)
        interpretations[question] = result["answer"]

    return interpretations