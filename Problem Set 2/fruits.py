import csv

def main():
    fruits = {}
    with open("fruits.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            fruits[row["name"]] = row["calories"]

    item = input("Item: ").lower().strip()
    if item in fruits:
        print(f"Calories: {fruits[item]}")

main()
