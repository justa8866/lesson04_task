# Lekcja 04 - Zadanie 8
# Python: składnia, typy i operatory

lr_initial = 0.1
decay = 0.95
epoch = 10
lr_new = lr_initial * decay ** epoch
print(f"Learning rate po {epoch} epokach: {lr_new:.2e}")
