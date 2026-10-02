def main():
    msg = input("Text: ")

    result = convert(msg)
    print(result)

def convert(msg):
    # Replace happy expression
    msg  = msg.replace(':)','🙂')
    # Replace sad expression
    msg = msg.replace(':(','🙁')
    # Return string
    return msg

main()    