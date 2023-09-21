import subprocess
import psutil
import tkinter as tk
import ttkbootstrap as tb
import os
from PIL import Image
from ttkbootstrap.constants import *
Image.CUBIC = Image.BICUBIC
import calendar

def show_calendar(year, month):
    cal_text.config(text=calendar.month(year, month))

def prev_month():
    global current_year, current_month
    if current_month == 1:
        current_year -= 1
        current_month = 12
    else:
        current_month -= 1
    show_calendar(current_year, current_month)

def next_month():
    global current_year, current_month
    if current_month == 12:
        current_year += 1
        current_month = 1
    else:
        current_month += 1
    show_calendar(current_year, current_month)

# Initialize the main window
root = tk.Tk()
root.title("Calendar Widget")

# Initialize variables for the current year and month
current_year = 2023
current_month = 9

# Create and configure widgets
prev_button = tk.Button(root, text="Prev", command=prev_month)
next_button = tk.Button(root, text="Next", command=next_month)
cal_text = tk.Label(root, text="", justify="left")

# Display widgets
prev_button.pack()
next_button.pack()
cal_text.pack()

# Show the initial calendar
show_calendar(current_year, current_month)

# Start the main loop
root.mainloop()
