import tkinter as tk
import calendar
import datetime
import ttkbootstrap as tb

current_date = datetime.date.today()

year = current_date.year
month = current_date.month
day = current_date.day
cal = calendar.TextCalendar(calendar.SUNDAY)
calendar_text = cal.formatmonth(year, month)

root = tk.Tk(className="Calendar_widget")
root.configure(bg="#292938")
root.geometry('250x200+30+38')
text_widget = tb.Text(root, wrap=tk.WORD,)
text_widget.pack()

text_widget.configure(font=("Courier", 10, "bold"), background="#292938", foreground="#ababeb")
text_widget.insert("1.0", calendar_text)

text_start = "2.0"  
text_end = text_widget.index(tk.END)

while True:
    start_idx = text_widget.search(str(day), text_start, text_end)

    if not start_idx:
        break

    end_idx = text_widget.index(f"{start_idx}+2c")

    text_widget.tag_add("highlight", start_idx, end_idx)
    text_widget.tag_configure("highlight", background="#ababeb", foreground="#292938")

    text_start = end_idx

text_widget.configure(state="disabled")

root.mainloop()
