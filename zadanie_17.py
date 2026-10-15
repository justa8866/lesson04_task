# Lekcja 04 - Zadanie 17
# Python: składnia, typy i operatory

log = "Epoch 23/100 - loss: 0.3421 - accuracy: 0.8934 - val_loss: 0.4102 - val_accuracy: 0.8712"
parts = log.split(" - ")
epoch, total = map(int, parts[0].replace("Epoch ", "").split("/"))
loss = float(parts[1].split(":")[1].strip())
accuracy = float(parts[2].split(":")[1].strip())
val_loss = float(parts[3].split(":")[1].strip())
val_accuracy = float(parts[4].split(":")[1].strip())
difference = accuracy - val_accuracy
print(f"Epoka: {epoch}/{total}")
print(f"Loss: {loss:.4f}, val_loss: {val_loss:.4f}")
print(f"Accuracy: {accuracy:.2%}, val_accuracy: {val_accuracy:.2%}")
print(f"Różnica: {difference:.2%}")
print("Możliwa oznaka overfittingu" if difference > 0.02 else "Niewielka różnica")
