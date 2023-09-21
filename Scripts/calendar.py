import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show_selected_date():
    selected_date = cal.get_date()
    messagebox.showinfo("Selected Date", f"Selected Date: {selected_date}")

# Create the main application window
root = tk.Tk()
root.title("Calendar Label Example")

# Create a ttkbootstrap style theme (You need to install ttkbootstrap for this)
style = ttk.Style()
style.theme_use('superhero')  # You can change the theme as per your preference

# Create a Calendar widget

# Create a button to get the selected date
get_date_button = ttk.Button(root, text="Get Selected Date", command=show_selected_date)
get_date_button.pack(pady=10)

# Start the main event loop
root.mainloop()
