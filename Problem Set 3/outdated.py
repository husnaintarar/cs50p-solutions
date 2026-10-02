months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
  try:
    user_input = input("Date: ").strip()

    if "/" in user_input:
      month, day, year = user_input.split("/")

      month = int(month)
      day = int(day)
      year = int(year)

    elif "," in user_input:
      parts = user_input.split(" ") 

      if parts[0] in months:
        month = months.index(parts[0]) + 1
        day = int(parts[1].replace(",", ""))
        year = int(parts[2])
      else: 
        continue
        
    else:
      continue

    if 1 <= month <= 12 and 1 <= day <= 31:
      print(f"{year:04}-{month:02}-{day:02}")
      break
      
  except (ValueError, IndexError):
    pass