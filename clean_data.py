import re
import pandas as pd
from medex_project.data.medical_corpus import MedicalCorpus
from medex_project.data.user_data_corpus import UserDataCorpus

def clean_data(medical_corpus, privacy_data, user_data_corpus):

    medical_data = medical_corpus.load_medical_corpus()
    user_data = user_data_corpus.load_user_data()

    cleaned_medical_data = _clean_text(medical_data)
    cleaned_user_data = _clean_text(user_data)

    medical_corpus.save_medical_corpus(cleaned_medical_data)
    user_data_corpus.update_user_data(privacy_data.user_id, cleaned_user_data)

def _clean_text(data: pd.DataFrame) -> pd.DataFrame:
    data['text'] = data['text'].apply(lambda x: x.lower())
    data['text'] = data['text'].apply(lambda x: re.sub(r'\d+', '', x))
    data['text'] = data['text'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
    data['text'] = data['text'].apply(lambda x: re.sub(r'\s+', ' ', x).strip())

    return data


