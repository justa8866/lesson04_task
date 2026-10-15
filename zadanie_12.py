# Lekcja 04 - Zadanie 12
# Python: składnia, typy i operatory

n = 50000
batch_size = 128
epochs = 50
seconds_per_batch = 0.15
batches = n // batch_size + (1 if n % batch_size else 0)
total = batches * epochs * seconds_per_batch
hours = int(total // 3600)
minutes = int(total % 3600 // 60)
seconds = total % 60
print(f"Batche na epokę: {batches}")
print(f"Szacowany czas: {hours} h {minutes} min {seconds:.1f} s")
