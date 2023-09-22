import tkinter as tk
import calendar
import datetime

current_date = datetime.date.today()

year = current_date.year
month = current_date.month
day = current_date.day  # Extract the day of the month and convert to a string
cal = calendar.TextCalendar(calendar.SUNDAY) 
calendar_text =  cal.formatmonth(year, month)
    
root = tk.Tk()
root.title("Linux-like Calendar")

text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack()

text_widget.configure(font=("Courier", 12))

text_widget.insert("1.0", calendar_text)

text_start = "2.0"  # Start of the second line (where the dates start)
text_end = text_widget.index(tk.END)

while True:
        # Find the position of today's date in the text
    start_idx = text_widget.search(str(day), text_start, text_end)

    if not start_idx:
        break

    end_idx = text_widget.index(f"{start_idx}+2c")  # Calculate the end position

        # Tag the date with a red background
    text_widget.tag_add("highlight", start_idx, end_idx)
    text_widget.tag_configure("highlight", background="red", foreground="white")

        # Update the start position for the next search
    text_start = end_idx

    # Start the Tkinter event loop
root.mainloop()

# Call the function to display the calendar
