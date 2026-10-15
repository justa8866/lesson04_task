# Lekcja 04 - Zadanie 9
# Python: składnia, typy i operatory

values = [75, 50, 100, 62.5]
minimum, maximum = 50, 100
print(f"{'Oryginalna':<15} {'Znormalizowana':<18} Status")
for value in values:
    normalized = (value - minimum) / (maximum - minimum)
    status = "OK" if 0 <= normalized <= 1 else "Poza zakresem"
    print(f"{value:<15} {normalized:<18.2f} {status}")
