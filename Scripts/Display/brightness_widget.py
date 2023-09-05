import subprocess
import ttkbootstrap as tb
from subprocess import check_output, call
import subprocess
import tkinter as tk
symbols = ["󰃞", "󰃝", "󰃟", "󰃠"]

root = tk.Tk(className="brightness_widget")
root.geometry('40x210+1745+38')
root.configure(bg="#222222")
theme = tb.Style("darkly")
current_brightness = int(check_output(["brightnessctl", "get"]).decode("utf-8").strip("%\n"))
my_scale = tb.Scale(root, bootstyle="info",
                    length=160,
                    orient="vertical",
                    from_=100,
                    to=0,
                    )
my_scale.pack(pady=10)
my_scale.set(current_brightness)



def set_brightness(value):
    try:
        subprocess.run(['brightnessctl', 'set', str(value) + '%'], check=True)
    except subprocess.CalledProcessError:
        print("Error setting brightness")

def update_label(value):
    symbol_index = int(value) // 25 
    label.config(text=f"{symbols[symbol_index]}")

def scale_changed(event):
    brightness_value = my_scale.get()
    set_brightness(brightness_value)
    update_label(brightness_value)


symbol_index = (int(current_brightness-1) // 25)  
label = tb.Label(root, text=f"{symbols[symbol_index]}", font=("Symbols Nerd Font", 10))
label.pack()

my_scale.bind("<Motion>", scale_changed)

def on_focus_out(event):
    root.quit()


root.bind("<FocusOut>", on_focus_out)

root.mainloop()
