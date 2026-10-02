def main():
    time = input("What time is it? ")
    converted = convert(time)
    
    if 7.0 <= converted <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted <= 13.0:
        print("lunch time")
    elif 18.0 <= converted <= 19.0:
        print("dinner time") 

def convert(time):
    time = time.strip().lower()

    is_am = False #is_am and is_pm are boolean variables that will be used to determine if the time is in the morning or evening.
    is_pm = False

    if "a.m." in time: # if the time string contains "a.m.", it is morning time, so we set is_am to True and remove "a.m." from the time string.
        is_am = True
        time = time.replace("a.m.", "")
    elif "p.m." in time: # else if the time string contains "p.m.", it is evening time, so we set is_pm to True and remove "p.m." from the time string.
        is_pm = True
        time = time.replace("p.m.", "")

    hour, minutes = time.split(":")
    new_hours = float(hour)
    new_minutes = float(minutes) / 60

    if is_pm and new_hours != 12:
        new_hours += 12
    elif is_am and new_hours == 12:
        new_hours -= 12

    return new_hours + new_minutes

if __name__ == "__main__":
    main()
