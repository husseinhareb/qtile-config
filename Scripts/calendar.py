import subprocess
import psutil
import tkinter as tk
import ttkbootstrap as tb
import os
from PIL import Image
from ttkbootstrap.constants import *
Image.CUBIC = Image.BICUBIC

root = tk.Tk(className="monitoring_widget")
theme = tb.Style("darkly")
root.configure(bg="#3b3b3b")
root.geometry('550x400+1725+38')

tb.DateEntry(root, style='success.TCalendar')

root.mainloop()