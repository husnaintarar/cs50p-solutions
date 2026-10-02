def main():
    a = input("What is the answer to the Great Question of Life, the Universe and Everything? " )
    result = answer(a)
    print(result)

def answer(a):
    cleaned_input = a.strip()
    if cleaned_input in ["42", "forty-two", "Forty Two"]:
        return "Yes"
    else:
        return "No"

main()