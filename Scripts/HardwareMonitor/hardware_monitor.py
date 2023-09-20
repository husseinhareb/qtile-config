import subprocess
import psutil
import tkinter as tk
import ttkbootstrap as tb
import os
from PIL import Image
from ttkbootstrap.constants import *
Image.CUBIC = Image.BICUBIC

def get_cpu_temp():
    output = subprocess.check_output(["sensors"], text=True)
    for line in output.splitlines():
        if "Package id 0:" in line:
            cpu_temp = line.split()[3][1:]
            cpu_temp = cpu_temp[:-2]
            return cpu_temp

def get_cpu_utilization():
    cpu_percent = psutil.cpu_percent(interval=1)  
    return f"{cpu_percent}"

def get_cpu_speed():
    output = subprocess.check_output("cat /proc/cpuinfo | grep 'cpu MHz' | awk '{sum += $4} END {avg = sum/NR; printf \"%.2f\", avg/1000}'", shell=True)
    average_speed_ghz = float(output)
    return average_speed_ghz;

def get_max_cpu_speed():
    output = subprocess.check_output("lscpu | grep 'CPU max MHz'", shell=True)
    max_cpu_speed_mhz = float(output.split(b':')[1].strip())
    max_cpu_speed_ghz = max_cpu_speed_mhz / 1000.0
    return max_cpu_speed_ghz;
