import validators

def main():
    email_input = input("Enter your Email Address: ")
    if validators.email(email_input):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()