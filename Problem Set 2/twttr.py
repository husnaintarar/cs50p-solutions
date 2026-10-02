def main():
    str = input("Input: ")
    print(shorten(str))

def shorten(str):
    vowels = "aeiouAEIOU"
    result = ""
    for char in str:
        if char not in vowels:
            result += char
    return result

main()