# Lekcja 04 - Zadanie 19
# Python: składnia, typy i operatory

probabilities = [0.23, 0.67, 0.89, 0.34, 0.91, 0.12, 0.78, 0.45]
labels = [0, 1, 1, 0, 1, 0, 1, 0]
best_threshold, best_accuracy = None, -1
for threshold in [0.3, 0.5, 0.7]:
    predictions = [int(prob >= threshold) for prob in probabilities]
    correct = sum(pred == actual for pred, actual in zip(predictions, labels))
    accuracy = correct / len(labels)
    print(f"Threshold: {threshold:.1f} | Accuracy: {accuracy:.2%}")
    if accuracy > best_accuracy:
        best_threshold, best_accuracy = threshold, accuracy
print(f"Optymalny threshold: {best_threshold} ({best_accuracy:.2%})")
