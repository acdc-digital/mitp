import os
import json

class MedicalCorpus:
    def __init__(self, filepath="medical_corpus.json"):
        self.medical_corpus_file = filepath
        self.medical_corpus = self.load_medical_corpus()

    def load_medical_corpus(self):
        if os.path.exists(self.medical_corpus_file):
            with open(self.medical_corpus_file, "r") as f:
                return json.load(f)
        else:
            return {}

    def save_medical_corpus(self):
        with open(self.medical_corpus_file, "w") as f:
            json.dump(self.medical_corpus, f)

    def add_entry(self, key, value):
        self.medical_corpus[key] = value
        self.save_medical_corpus()

    def get_entry(self, key):
        return self.medical_corpus.get(key, None)

    def remove_entry(self, key):
        if key in self.medical_corpus:
            del self.medical_corpus[key]
            self.save_medical_corpus()

    def update_entry(self, key, value):
        if key in self.medical_corpus:
            self.medical_corpus[key] = value
            self.save_medical_corpus()

