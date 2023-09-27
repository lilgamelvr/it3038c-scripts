import datetime

while True:
    try:
        birthdayinput = input("Please enter your Date of Birth in Month Day Year format: ")
        birthday = datetime.datetime.strptime(birthdayinput, '%B %d %Y')
        break
    except:
        print("Please put in the Format 'Month Day Year'")

today = datetime.datetime.today()
timedelta = (today - birthday).total_seconds()
print("You have been alive for:", timedelta, "seconds")
