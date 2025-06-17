#Age Calculator
from datetime import datetime

birth_date = input("Enter your birth date (YYYY-MM-DD): ")
birth = datetime.strptime(birth_date, "%Y-%m-%d")
today = datetime.today()

age_years = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
age_months = (today.year - birth.year) * 12 + today.month - birth.month - (today.day < birth.day)
age_days = (today - birth).days

print(f"You are {age_years} years, {age_months % 12} months, and {age_days} days old.")

#Days Until Next Birthday
next_birthday = birth.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left = (next_birthday - today).days
print(f"Days until your next birthday: {days_left}")

#Meeting Scheduler
from datetime import timedelta

current_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
hours = int(input("Enter meeting duration (hours): "))
minutes = int(input("Enter meeting duration (minutes): "))

start_time = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
end_time = start_time + timedelta(hours=hours, minutes=minutes)

print(f"The meeting will end at: {end_time}")

#Time Zone Converter
from pytz import timezone, all_timezones

dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
src_tz = input("Enter current timezone (e.g., Europe/Moscow): ")
dst_tz = input("Enter target timezone (e.g., Asia/Tokyo): ")

dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
dt = timezone(src_tz).localize(dt)
converted = dt.astimezone(timezone(dst_tz))

print("Converted time:", converted.strftime("%Y-%m-%d %H:%M (%Z)"))

#Countdown Timer
import time

target_str = input("Enter a future date and time (YYYY-MM-DD HH:MM): ")
target = datetime.strptime(target_str, "%Y-%m-%d %H:%M")

while True:
    now = datetime.now()
    if now >= target:
        print("Time is up!")
        break
    remaining = target - now
    print(f"Time remaining: {remaining}", end='\r')
    time.sleep(1)

#Email Validator
import re

email = input("Enter your email: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")

#Phone Number Formatter
number = input("Enter a 10-digit phone number: ").strip()
if len(number) == 10 and number.isdigit():
    formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
    print("Formatted number:", formatted)
else:
    print("Invalid phone number.")

#Password Strength Checker
password = input("Enter your password: ")

if (len(password) >= 8 and
    re.search(r'[A-Z]', password) and
    re.search(r'[a-z]', password) and
    re.search(r'[0-9]', password)):
    print("Strong password.")
else:
    print("Weak password.")

#Word Finder
text = input("Enter a block of text: ")
word = input("Enter a word to search: ").lower()

matches = [m.start() for m in re.finditer(rf'\b{word}\b', text.lower())]

if matches:
    print(f"The word '{word}' was found {len(matches)} time(s) at positions: {matches}")
else:
    print("Word not found.")

#Date Extractor
text = input("Enter a text with dates (like 12.04.2023 or 2023-04-12): ")
dates = re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b|\b\d{4}-\d{2}-\d{2}\b', text)

if dates:
    print("Dates found:", dates)
else:
    print("No dates found.")
