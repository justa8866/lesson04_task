# Lekcja 04 - Zadanie 13
# Python: składnia, typy i operatory

values = [120, 125, 118, 190, 122]

# Każdy pomiar porównujemy z pozostałymi czterema, aby nie wpływał
# na średnią i odchylenie standardowe używane do jego oceny.
for index, value in enumerate(values):
    reference = values[:index] + values[index + 1:]
    mean = sum(reference) / len(reference)
    variance = sum((x - mean) ** 2 for x in reference) / len(reference)
    std = variance ** 0.5
    status = "ANOMALIA!" if abs(value - mean) > 3 * std else "OK"
    print(f"Wartość: {value} - {status}")
