def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")

def value(greeting):
    cleaned_input = greeting.strip().lower()
    if cleaned_input.startswith("hello"):
        return 0
    elif cleaned_input.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
