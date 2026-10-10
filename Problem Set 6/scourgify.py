import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")

diary = []

try:
    with open(sys.argv[1], mode = "r", encoding= "utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            full_name = row["name"]
            last, first = full_name.split(",")
            house = row["house"]
            diary.append({"first": first, "last": last, "house": house})

except FileNotFoundError:
    sys.exit("File does not exist")

with open(sys.argv[2], mode = "w", newline = "", encoding= "utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

        writer.writeheader()
        writer.writerows(diary)

print(f"Successfully transformed and saved to {sys.argv[2]}")


