from pathlib import Path

script_location = Path(__file__).absolute().parent

file_location = script_location / "mcode1.txt"
file = file_location.open()
mcode1 = file.readline()

file_location = script_location / "mcode2.txt"
file = file_location.open()
mcode2 = file.readline()

file_location = script_location / "mcode3.txt"
file = file_location.open()
mcode3 = file.readline()

file_location = script_location / "transmission1.txt"
file = file_location.open()
transmission1 = ""

for line in file.readlines():
    transmission1 += line.strip("\n")

print("Transmisión 1:")
print(transmission1)

file_location = script_location / "transmission2.txt"
file = file_location.open()
transmission2 = ""

for line in file.readlines():
    transmission2 += line.strip("\n")

print("Transmisión 2:")
print(transmission2)