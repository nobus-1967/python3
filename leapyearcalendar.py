# Check if a year is a leap year using module calendar
import calendar

year = int(input("Enter a year to check: "))

if calendar.isleap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

