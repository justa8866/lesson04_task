# Lekcja 04 - Zadanie 7
# Python: składnia, typy i operatory

accuracy_a, time_a = 0.87, 120
accuracy_b, time_b = 0.89, 450
difference = accuracy_b - accuracy_a
significant = difference > 0.02
if time_a < time_b and not significant:
    recommendation = "Model A - najlepszy kompromis"
else:
    recommendation = "Model B - wyższa dokładność"
print(f"Różnica accuracy: {difference:.2%}")
print(f"Czasy treningu: A={time_a}s, B={time_b}s")
print(recommendation)
