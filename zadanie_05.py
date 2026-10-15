# Lekcja 04 - Zadanie 5
# Python: składnia, typy i operatory

path = "data/processed/train_fold_03_normalized.csv"
parts = path.split("/")
folder = "/".join(parts[:-1])
name, extension = parts[-1].split(".")
fields = name.split("_")
print(f"Folder: {folder}")
print(f"Typ zbioru: {fields[0]}")
print(f"Numer fold: {fields[2]}")
print(f"Format: {extension}")
