# Lekcja 04 - Zadanie 1
# Python: składnia, typy i operatory

waga = 70
wzrost = 1.75
bmi = waga / wzrost ** 2
if bmi < 18.5:
    opis = "Niedowaga"
elif bmi < 25:
    opis = "Norma"
else:
    opis = "Nadwaga"
print(f"BMI: {bmi:.2f}")
print(f"Interpretacja: {opis}")
