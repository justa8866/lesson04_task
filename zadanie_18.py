# Lekcja 04 - Zadanie 18
# Python: składnia, typy i operatory

age_raw = " 45.7 "
sex_raw = "male"
pressure_raw = "120/80"
height_raw = " 175.5cm "
try:
    age = float(age_raw.strip())
    age_ok = 0 < age <= 120
except ValueError:
    age_ok = False
sex_ok = sex_raw.strip().lower() in ("male", "female")
try:
    systolic, diastolic = map(int, pressure_raw.strip().split("/"))
    # Przykładowe techniczne zakresy walidacji, nie kryteria medyczne.
    pressure_ok = 50 <= systolic <= 250 and 30 <= diastolic <= 150 and systolic > diastolic
except ValueError:
    pressure_ok = False
try:
    height = float(height_raw.strip().lower().replace("cm", "").strip())
    height_ok = 0 < height <= 300
except ValueError:
    height_ok = False
for field, valid in [("Wiek", age_ok), ("Płeć", sex_ok), ("Ciśnienie", pressure_ok), ("Wzrost", height_ok)]:
    print(f"{field}: {'OK' if valid else 'BŁĄD'}")
