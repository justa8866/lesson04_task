# Lekcja 04 - Zadanie 13
# Python: składnia, typy i operatory

values = [120, 125, 118, 190, 122]
mean = sum(values) / len(values)
variance = sum((x - mean) ** 2 for x in values) / len(values)
std = variance ** 0.5
print(f"Średnia: {mean:.2f}; odchylenie standardowe: {std:.2f}")
for value in values:
    status = "ANOMALIA!" if abs(value - mean) > 3 * std else "OK"
    print(f"Wartość: {value} - {status}")
# Uwaga: dla tych pięciu danych reguła 3-sigma nie oznacza 190 jako anomalii.
# Oczekiwany wynik w PDF jest sprzeczny z tą regułą dla podanej próbki.
