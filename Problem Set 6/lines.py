import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
    
try:
    line_count = 0

    with open(sys.argv[1], "r") as file:
        for line in file:
            if not line.strip():          
                pass 
            elif line.strip().startswith("#"): 
                pass
            else:                        
                line_count += 1

    print(f"{line_count}")

except FileNotFoundError:
    sys.exit("File does not exist")
