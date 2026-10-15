# Lekcja 04 - Zadanie 6
# Python: składnia, typy i operatory

accuracy = 0.9234
precision = 0.8891
recall = 0.9456
print(f"{'Metryka':<15} {'Wartość':>12}")
print("-" * 28)
for name, value in [("Accuracy", accuracy), ("Precision", precision), ("Recall", recall)]:
    print(f"{name:<15} {value:>12.2%}")
