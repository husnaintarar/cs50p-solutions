import random
import sys
import pyfiglet

figlet = pyfiglet.Figlet()
available_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font_choice = random.choice(available_fonts)
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    font_choice = sys.argv[2]
    if font_choice not in available_fonts:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

user_input = input("Input: ")

result = pyfiglet.figlet_format(user_input, font=font_choice)

print("Output:")
print(result)
