import ttkbootstrap as tb
from subprocess import check_output, call
import subprocess
import tkinter as tk

symbols = [""]
root = tk.Tk(className="mic_widget")
root.geometry('40x210+1650+38')
root.configure(bg="#222222")
theme = tb.Style("darkly")