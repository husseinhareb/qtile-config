import calendar
import datetime

current_date = datetime.date.today()

year = current_date.year
month = current_date.month
day = current_date.day

cal = calendar.TextCalendar(calendar.SUNDAY)  

calendar_text = cal.formatmonth(year, month)
highlighted_calendar = calendar_text.replace(f"{day:2}", f"\033[1;37;41m{day:2}\033[m", 1)

print(highlighted_calendar)
