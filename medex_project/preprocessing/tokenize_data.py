from transformers import BertTokenizer
from typing import List

def tokenize_data(text_data: List[str], tokenizer_name: str = 'bert-base-uncased') -> List[List[str]]:
    tokenizer = BertTokenizer.from_pretrained(tokenizer_name)
    tokenized_data = []

    for text in text_data:
        tokens = tokenizer.tokenize(text)
        tokenized_data.append(tokens)

    return tokenized_data