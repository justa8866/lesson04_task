# Lekcja 04 - Zadanie 14
# Python: składnia, typy i operatory

dataset = "iris"
k = 5
for fold in range(1, k + 1):
    for kind in ["train", "test"]:
        print(f"{dataset}_fold_{fold:02d}_{kind}.csv")
