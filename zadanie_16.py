# Lekcja 04 - Zadanie 16
# Python: składnia, typy i operatory

tp, tn, fp, fn = 45, 38, 7, 10
accuracy = (tp + tn) / (tp + tn + fp + fn)
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)
print("CONFUSION MATRIX")
print(f"{'':<15}{'Predicted':^20}")
print(f"{'Actual':<15}{'0':>8}{'1':>10}")
print(f"{'0':<15}{tn:>8}{fp:>10}")
print(f"{'1':<15}{fn:>8}{tp:>10}")
for name, value in [("Accuracy", accuracy), ("Precision", precision), ("Recall", recall), ("F1-Score", f1)]:
    print(f"{name}: {value:.2%}")
