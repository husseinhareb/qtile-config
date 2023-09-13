import ttkbootstrap as tb
from subprocess import check_output, call
import subprocess
import tkinter as tk

symbols = [""]
root = tk.Tk(className="mic_widget")
root.geometry('40x210+1650+38')
root.configure(bg="#222222")
theme = tb.Style("darkly")

bash_command = "pactl list sources | grep 'Volume:' | awk -F/ '{print $2}' | awk '{print $1}' | head -n 3 | tail -n 1"

completed_process = subprocess.run(bash_command, shell=True, capture_output=True, text=True)

volume_info = completed_process.stdout.strip()

volume_info = volume_info.replace('%','')
current_volume = int(volume_info)

my_scale = tb.Scale(root, bootstyle="info",
                    length=160,
                    orient="vertical",
                    from_=100,
                    to=0,
                    )