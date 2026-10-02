def main():
    # Prompt user for amount due
    Amount_due = 50
    # WHILE loop to continue until amount due is 0 or less
    while Amount_due > 0:
        print(f"Amount Due: {Amount_due}")
        coin = int(input("Insert Coin: "))
        #if coin is a valid coin, subtract it from amount due
        if coin in [25, 10, 5]:
            Amount_due -= coin      
    print(f"Change owed: {abs(Amount_due)}")

main()
