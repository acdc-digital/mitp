class MedexHyperparameters:
    def __init__(self):
        self.learning_rate = 5e-5
        self.epochs = 3
        self.batch_size = 16
        self.max_seq_length = 128
        self.model_name = "distilbert-base-uncased"

    def get_hyperparameters(self):
        return {
            "learning_rate": self.learning_rate,
            "epochs": self.epochs,
            "batch_size": self.batch_size,
            "max_seq_length": self.max_seq_length,
            "model_name": self.model_name,
        }