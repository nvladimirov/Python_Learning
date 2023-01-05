import datetime
import locale
locale.setlocale(locale.LC_ALL, "ru_RU")
now = datetime.datetime.now()
today = now.day
year = now.year
hour = now.hour
minute = now.minute
time = f"{hour}:{minute}"
print(time)
