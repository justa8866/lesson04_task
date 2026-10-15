# Lekcja 04 - Zadanie 15
# Python: składnia, typy i operatory

weights = [65.5, 78.2, 54.8, 92.1, 70.0]
n = len(weights)
mean = sum(weights) / n
std = (sum((x - mean) ** 2 for x in weights) / n) ** 0.5
zs = []
for weight in weights:
    z = (weight - mean) / std
    zs.append(z)
    if z > 2:
        description = "Bardzo wysoka"
    elif z < -2:
        description = "Bardzo niska"
    elif abs(z) < 1:
        description = "Typowa"
    else:
        description = "Poza typowym zakresem"
    print(f"{weight:.1f} kg | z={z:.2f} | {description}")
print(f"Średnia z: {sum(zs) / n:.2f}")
print(f"Odchylenie z: {(sum(z ** 2 for z in zs) / n) ** 0.5:.2f}")
