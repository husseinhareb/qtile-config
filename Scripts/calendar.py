import calendar
import datetime
import tkinter as tk
import ttkbootstrap as tb


current_date = datetime.date.today()

year = current_date.year
month = current_date.month
day = current_date.day

cal = calendar.TextCalendar(calendar.SUNDAY)  

calendar_text = cal.formatmonth(year, month)
highlighted_calendar = calendar_text.replace(f"{day:2}", f"\033[1;37;41m{day:2}\033[m", 1)

print(highlighted_calendar)

root = tk.Tk(className="monitoring_widget")
theme = tb.Style("darkly")
root.configure(bg="#3b3b3b")
root.geometry('250x250+1725+38')



root.mainloop()