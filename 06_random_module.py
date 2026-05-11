# import module random

import random

# random angka integer
print("Random Angka 1-10:", random.randint(1,10))
print("Random Angka 0-100:", random.randint(0,100))

# random angka float
print("Random Angka 0.0-1.0:", random.random())
print("Random Angka 1.5-10.5:", random.uniform(1.5,10.5))

# random pilih item
buah = ["apel", "jeruk", "semangka","durian"]
pilihan = random.choice(buah)
print("Buah yang dipilih:", pilihan)

random.shuffle(buah)
print("List Random Buah:", buah)