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
my_scale.pack(pady=10)
my_scale.set(int(current_volume))        
def set_volume(volume):
    subprocess.run(["pactl", "set-source-volume", "0", f"{volume}%"])
def update_label(value):    
    if int(value) == 0:
        label.config(text="")
    else:
        label.config(text="")

def scale_changed(event):
    volume_value = my_scale.get()
    set_volume(volume_value)
    update_label(volume_value)

if current_volume == 0:
    label = tb.Label(root, text="", font=("Symbols Nerd Font", 10))
    label.pack()
else:
    label = tb.Label(root, text="", font=("Symbols Nerd Font", 10))
    label.pack()

my_scale.bind("<Motion>", scale_changed)

def on_focus_out(event):
    root.quit()
root.bind("<FocusOut>", on_focus_out)



root.mainloop()