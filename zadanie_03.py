# Lekcja 04 - Zadanie 3
# Python: składnia, typy i operatory

n = 1000
train = n * 70 // 100
validation = n * 15 // 100
test = n - train - validation
print(f"Trening: {train}, walidacja: {validation}, test: {test}")
print(f"Suma: {train + validation + test}")
