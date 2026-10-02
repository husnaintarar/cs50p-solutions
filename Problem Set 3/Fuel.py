def main():
    while True:
        try:
            user_input = input("Fraction: ")
            x_str, y_str = user_input.split("/")
            x = int(x_str)
            y = int(y_str)

            if x >= 0 and x <= y:
                fraction_percentage = round((x / y) * 100)

                if fraction_percentage <= 1:
                    print("E")
                elif fraction_percentage >= 99:
                    print("F")
                else:
                    print(f"{fraction_percentage}%")
                
                break

        except (ValueError, ZeroDivisionError):
            pass

main()