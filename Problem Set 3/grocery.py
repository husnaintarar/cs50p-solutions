groceries = {}

while True:
    try:
        item = input().upper()
        
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
            
    except EOFError:
        print()

        for key in sorted(groceries):
            value = groceries[key]
            print(f"{value} {key}")
        break
    