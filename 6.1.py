import sys
number = int(sys.argv[1])
if number % 2 == 0:
    parity = "парне"
else:
    parity = "непарне"
with open("number.txt", "w") as f: f.write(f"Число {number} є {parity}")