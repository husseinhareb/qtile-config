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