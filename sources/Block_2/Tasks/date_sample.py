from datetime import date
from datetime import datetime
from datetime import time

date_one = date(1815, 12, 25)
print(date_one)

time_one = time(16, 20, 00)
print(time_one)

datetime_one = datetime(1986, 4, 26, 1, 23, 47)
print(datetime_one)

print("Год", datetime_one.year)
print("Месяц", datetime_one.month)
print("День", datetime_one.day)
print("Час", datetime_one.hour)
print("Минута", datetime_one.minute)
print("Секунда", datetime_one.second)

print(datetime_one.weekday())

print(datetime.now())

thedate = date.fromisoformat("2021-05-04")

print(thedate.year)
print(thedate.month)
print(thedate.day)

thetime = time.fromisoformat("23:14")

print(thetime.hour)
print(thetime.minute)

thedatetime = datetime.fromisoformat("2020-12-06 23:14")

print(thedatetime.year)
print(thedatetime.month)
print(thedatetime.day)

print(thedatetime.hour)
print(thedatetime.minute)

print(thedate.strftime("%d %B %Y "))