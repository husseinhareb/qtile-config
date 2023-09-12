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
