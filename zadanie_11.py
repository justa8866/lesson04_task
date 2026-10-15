# Lekcja 04 - Zadanie 11
# Python: składnia, typy i operatory

learning_rate = 0.01
batch_size = 64
epochs = 100
dropout = 0.5
checks = {
    "Learning rate": 0 < learning_rate <= 1,
    "Batch size": batch_size > 0 and (batch_size & (batch_size - 1)) == 0,
    "Epochs": 0 < epochs < 1000,
    "Dropout": 0 <= dropout <= 1,
}
for name, valid in checks.items():
    print(f"{name}: {'OK' if valid else 'BŁĄD'}")
