import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r'^([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$', s):
        start_hour = int(matches.group(1))
        start_minute = matches.group(2)
        start_ampm = matches.group(3)
        start_hour2 = int(matches.group(4))
        start_minute2 = matches.group(5)
        start_ampm2 = matches.group(6)

        if start_minute is None:
            start_minute = "00"
        if start_minute2 is None:
            start_minute2 = "00"

        if start_ampm == "AM":
            if start_hour == 12:
                start_hour = 0
        elif start_ampm == "PM":
            if start_hour != 12:
                start_hour += 12

        if start_ampm2 == "AM":
            if start_hour2 == 12:
                start_hour2 = 0
        elif start_ampm2 == "PM":
            if start_hour2 != 12:
                start_hour2 += 12

        new_start = f"{start_hour:02}:{start_minute}"
        new_end = f"{start_hour2:02}:{start_minute2}"

        return f"{new_start} to {new_end}"
    raise ValueError

if __name__ == "__main__":
    main()