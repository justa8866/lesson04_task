# Lekcja 04 - Zadanie 10
# Python: składnia, typy i operatory

model = "XGBoost Classifier"
dataset = "Credit Card Fraud"
n = 284807
accuracy, precision, recall = 0.9991, 0.8876, 0.7561
f1 = 2 * precision * recall / (precision + recall)
print("=" * 50)
print(f"{'RAPORT MODELU':^50}")
print("=" * 50)
print(f"{'Model:':<20}{model}")
print(f"{'Dataset:':<20}{dataset}")
print(f"{'Liczba próbek:':<20}{n:,}")
print("-" * 50)
for name, value in [("Accuracy", accuracy), ("Precision", precision), ("Recall", recall), ("F1-Score", f1)]:
    print(f"{name + ':':<20}{value:.2%}")
print("=" * 50)
