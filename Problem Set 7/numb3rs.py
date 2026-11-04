import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip.strip())

    if matches:
        for group in matches.groups():
            if not (0 <= int(group) <= 255) or str(int(group)) != group:
                return False
        return True
        
    return False

if __name__ == "__main__":
    main()