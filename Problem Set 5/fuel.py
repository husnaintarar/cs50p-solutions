def main():
    user_input = input("Fraction: ")    
    percentage = convert(user_input)
    print(gauge(percentage))


def convert(fraction):
    x_str, y_str = fraction.split("/")
    x = int(x_str)
    y = int(y_str)
    if x >= 0 and x <= y:
        percentage = round((x / y) * 100)
        return percentage
    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    raise ValueError("Invalid fraction")

    

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()