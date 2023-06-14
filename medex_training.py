import torch
from torch.utils.data import DataLoader
from transformers import AdamW, get_linear_schedule_with_warmup
from medex_project.preprocessing.clean_data import clean_data
from medex_project.preprocessing.split_data import split_data
from medex_project.preprocessing.tokenize_data import tokenize_data
from medex_project.model_parameters.medex_language_model import MedexLanguageModel
from medex_project.utils.save_load_model import save_model

def train_medex_model():
    # Load and preprocess data
    data = clean_data()
    train_data, val_data = split_data(data)
    train_dataset, val_dataset = tokenize_data(train_data, val_data)

    # Initialize model
    model = MedexLanguageModel()

    # Set up training parameters
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    epochs = 3
    batch_size = 16
    train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_dataloader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    # Set up optimizer and learning rate scheduler
    optimizer = AdamW(model.parameters(), lr=5e-5)
    total_steps = len(train_dataloader) * epochs
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)

    # Training loop
    for epoch in range(epochs):
        model.train()
        total_train_loss = 0

        for batch in train_dataloader:
            input_ids, attention_mask, labels = batch
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()
            loss, _ = model(input_ids, attention_mask=attention_mask, labels=labels)
            total_train_loss += loss.item()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            scheduler.step()

        avg_train_loss = total_train_loss / len(train_dataloader)
        print(f"Epoch {epoch + 1}, Training Loss: {avg_train_loss}")

        # Validation loop
        model.eval()
        total_val_loss = 0

        for batch in val_dataloader:
            input_ids, attention_mask, labels = batch
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            labels = labels.to(device)

            with torch.no_grad():
                loss, _ = model(input_ids, attention_mask=attention_mask, labels=labels)
                total_val_loss += loss.item()

        avg_val_loss = total_val_loss / len(val_dataloader)
        print(f"Epoch {epoch + 1}, Validation Loss: {avg_val_loss}")

    # Save trained model
    save_model(model)