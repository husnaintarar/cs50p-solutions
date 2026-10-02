def main():
    variable_name = input("camelCase: ")
    print(camel_to_snake(variable_name))

def camel_to_snake(variable_name):
    result = "" 
    for char in variable_name: 
        if char.isupper(): 
            result += "_" + char.lower() 
        else:
            result += char 
        
    return result

main()