import ttkbootstrap as tb
from subprocess import check_output, call
import subprocess
import tkinter as tk

symbols = ["󰕿", "󰖀", "󰕾"]

root = tk.Tk(className="volume_widget")
root.geometry('40x210+1580+38')
root.configure(bg="#222222")
theme = tb.Style("darkly")

bash_command = "volume_info=$(pactl list sinks | grep '^[[:space:]]Volume:' | head -n 1 | awk '{print $5}') && echo $volume_info"

completed_process = subprocess.run(bash_command, shell=True, capture_output=True, text=True)

volume_info = completed_process.stdout.strip()

volume_info = volume_info.replace('%','')
current_volume = int(volume_info)

my_scale = tb.Scale(root, bootstyle="info",
                    length=160,
                    orient="vertical",
                    from_=120,
                    to=0,
                    )
my_scale.pack(pady=10)
my_scale.set(int(current_volume))        
def set_volume(volume):
    subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{volume}%"])
def update_label(value):    
    symbol_index = int(value) //  40
    if int(value) == 0:
        label.config(text="󰖁")
    else:
        label.config(text=f"{symbols[symbol_index]}")


def scale_changed(event):
    volume_value = my_scale.get()
    set_volume(volume_value)
    update_label(volume_value)

if current_volume == 0:
    label = tb.Label(root, text="󰖁", font=("Symbols Nerd Font", 10))
    label.pack()
else:
    symbol_index = (int(current_volume-1) // 40)  
    label = tb.Label(root, text=f"{symbols[symbol_index]}", font=("Symbols Nerd Font", 10))
    label.pack()


my_scale.bind("<Motion>", scale_changed)

