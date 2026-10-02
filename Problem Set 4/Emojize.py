import emoji
user_input = input("Input: ")
a = emoji.emojize(user_input, language='alias')
print(f"Output: {a}")