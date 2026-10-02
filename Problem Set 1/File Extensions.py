def main():
    file_name = input("File Name: ")
    print(extension(file_name))

def extension(file_name):
    cleaned_input = file_name.strip().lower()

    if cleaned_input.endswith((".gif", ".png")):
        return f"image/{cleaned_input[-3:]}"
    elif cleaned_input.endswith((".jpg", ".jpeg")):
            return "image/jpeg"
    elif cleaned_input.endswith((".pdf", ".zip")):
            return f"application/{cleaned_input[-3:]}"
    elif cleaned_input.endswith(".txt"):
            return "text/plain"
    else:
          return "application/octet-stream"

main()