import calendar
import datetime

# Get the current date
current_date = datetime.date.today()

# Extract the current month and year
year = current_date.year
month = current_date.month
day = current_date.day

# Create a TextCalendar object
cal = calendar.TextCalendar(calendar.SUNDAY)  # Start weeks on Sunday

# Display the calendar for the current month and year with today's date highlighted
calendar_text = cal.formatmonth(year, month)
highlighted_calendar = calendar_text.replace(f"{day:2}", f"\033[1;37;41m{day:2}\033[m", 1)

print(highlighted_calendar)
