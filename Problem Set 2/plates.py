def main():
    plate = input("Plate: ") 
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):  
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isalpha() and s[1].isalpha():
        result = ""
        for char in s:
            if char.isdigit():
                result += char
            elif char.isalpha():
                if len(result) > 0:
                    return False
            else:
                return False
        if len(result) == 0:
            return True
        elif result[0] == "0":
            return False
        else:
            return True
    return False
    
main()