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

def get_base_cpu_speed():
    command = "lscpu | awk -F ': ' '/Model name/ {split($2,a,\"@\"); gsub(/GHz/,\"\",a[2]); print a[2]}'"
    output = subprocess.check_output(command, shell=True, encoding='utf-8').strip()
    return output


def set_max_frequency(frequency_kHz):
    command = f"sudo cpupower frequency-set --max {frequency_kHz}"
    subprocess.call(command, shell=True)

def toggle_cpu_boost():
    def set_cpu_mode():
        password = password_var.get() 
        password_window.destroy() 

        if boost_var.get():
            command = f"echo {password} | sudo -S cpupower frequency-set --max {int(float(get_max_cpu_speed())*1000000)}"
        else:
            cpu_base = get_base_cpu_speed()
            command = f"echo {password} | sudo -S cpupower frequency-set --max {int(float(get_base_cpu_speed())*1000000)}"

        try:
            subprocess.run(["bash", "-c", command], check=True)
            with open('checkbox_state.txt', 'w') as file:
                file.write(str(boost_var.get()))
        except subprocess.CalledProcessError:
            open_password_window()

    def open_password_window():
        global password_window 
        password_window = tk.Toplevel(root)
        password_window.geometry('1080x140+1000+500')
        password_window.title("Password_Entry")
        password_warning_label = tk.Label(password_window,
                                          text="  DISCLAIMER",
                                          font=("Jetbrains Nerd Font",10,"bold"))
        password_warning_label.place() 
        password_warning_label.pack()
        responsibility_label = tk.Label(password_window,
                                        text="This Option tweaks the hardware of your computer.\nMe,(The creator) explicitly disclaims any responsibility or liability for any consequences arising from its use.\n By choosing to use this option, You (The user) acknowledge and accept that the creator bears no responsibility for any direct, indirect, or consequential damages resulting from its use.")
        responsibility_label.pack()
        password_label = tk.Label(password_window, text="Enter your CORRECT SUDO password:")
        password_label.pack()


                                    
        global password_var  
        password_var = tk.StringVar()
        password_entry = tk.Entry(password_window, show="*", textvariable=password_var)
        password_entry.pack()

        submit_button = tk.Button(password_window, text="Submit", command=set_cpu_mode)
        submit_button.pack()

        error_label = tk.Label(password_window, text="", fg="red")
        error_label.pack()

    open_password_window()


def get_gpu_temp():
    try:
        command = ["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader,nounits"]
        output = subprocess.check_output(command, text=True)
        return output.strip()
    except subprocess.CalledProcessError:
        return "N/A"

def get_max_gpu_clock():
    try:
        command = ["nvidia-smi", "--query-gpu=clocks.max.graphics", "--format=csv,noheader,nounits"]
        output = subprocess.check_output(command, text=True)
        return output.strip()
    except subprocess.CalledProcessError:
        return "N/A"

def get_gpu_utilization():
    try:
        command = ["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"]
        output = subprocess.check_output(command, text=True)
        return output.strip()
    except subprocess.CalledProcessError:
        return "N/A"

def get_gpu_clock():
    try:
        command = ["nvidia-smi", "--query-gpu=clocks.current.graphics", "--format=csv,noheader,nounits"]
        output = subprocess.check_output(command, text=True)
        return output.strip()
    except subprocess.CalledProcessError:
        return "N/A"

def get_ram_consumption():
    command = "free -m | awk '/Mem:/ {print int($3)}'"
    output = subprocess.check_output(command, shell=True, encoding='utf-8').strip()
    return output
def get_max_ram():
    try:
        virtual_memory = psutil.virtual_memory()
        return int(virtual_memory.total /(1024*1024))
    except Exception as e:
        return f"Error: {e}"
    

def get_battery_capacity():
    try:
        with open('/sys/class/power_supply/BAT0/capacity', 'r') as file:
            capacity = file.read().strip()
            return int(capacity)
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def get_vram_consumption():
    try:
        output = subprocess.check_output(['nvidia-smi', '--query-gpu=memory.used', '--format=csv,noheader,nounits'])
        vram_usage = output.decode().strip()
        return int(vram_usage)
    except FileNotFoundError:
        return None


def get_max_vram():
    try:
        output = subprocess.check_output(['nvidia-smi', '--query-gpu=memory.total', '--format=csv,noheader,nounits'])
        max_vram = output.decode().strip()
        return int(max_vram) 
    except FileNotFoundError:
        return None

def get_gpu_wattage():
    try:
        output = subprocess.check_output(['nvidia-smi', '--query-gpu=power.draw', '--format=csv,noheader,nounits'])
        output_str = output.decode('utf-8').strip()
        wattage = float(output_str)
        return wattage
    except Exception as e:
        return None


def get_max_gpu_wattage():
    try:
        output = subprocess.check_output(['nvidia-smi', '--query-gpu=power.max_limit', '--format=csv,noheader,nounits', '-i', '0'])
        output_str = output.decode('utf-8').strip()
        wattage_values = [float(val) for val in output_str.split('\n')]
        max_wattage = max(wattage_values)
        return max_wattage
    except Exception as e:
        return None


def update_labels():
    cpu_temp_label.configure(amountused=get_cpu_temp())
    cpu_utilization_label.configure(amountused=get_cpu_utilization())
    cpu_speed.configure(amountused=get_cpu_speed())
    gpu_temp_label.configure(amountused=get_gpu_temp())
    gpu_utilization.configure(amountused=get_gpu_utilization())
    gpu_speed.configure(amountused=get_gpu_clock())
    get_battery_capacity_label.configure(value=get_battery_capacity())
    battery_label["text"] = str(get_battery_capacity()) + "%"

    if int(get_ram_consumption()) > 1000:
        get_ram_consumption_label.configure(value=int(get_ram_consumption()))
        ram_cons = int(get_ram_consumption())/1024
        ram_cons = "{:.1f}".format(ram_cons)
        ram_label["text"] = str(ram_cons) + "GB"

    else:
        get_ram_consumption_label.configure(value=get_ram_consumption())
        ram_label["text"] = str(get_ram_consumption()) + "MB"

    get_vram_consumption_label.configure(value=get_vram_consumption())
    gpu_memory_label["text"] = str(get_vram_consumption()) + "MB"
    gpu_wattage_label["text"] = str(get_gpu_wattage())+ "W"
    get_gpu_wattage_bar.configure(value=get_gpu_wattage())
    root.after(1000, update_labels)  # Call update_labels every 1000ms (1 second)



root = tk.Tk(className="monitoring_widget")
theme = tb.Style("darkly")
root.configure(bg="#3b3b3b")
root.geometry('550x400+1725+38')

cpu_frame = tb.Frame(root,width=530,height=190)
cpu_frame.pack(pady=5)
cpu_temp_label = tb.Meter(cpu_frame,
                                bootstyle="danger",
                                arcrange=200,
                                arcoffset=170,
                                amountused=0,
                                amounttotal=100,
                                metertype='semi',
                                metersize=80,
                                #stripethickness=3,
                                meterthickness=5,
                                showtext= True,
                                textright="°C",
                                textfont=("Jetbrains Nerd Font",14),
                                subtext="Cpu Temp",
                                stepsize=1,
                                subtextfont=("Jetbrains Nerd Font",4))
cpu_temp_label.pack()
cpu_temp_label.place(x=347,y=33)
cpu_utilization_label = tb.Meter(cpu_frame,
                                bootstyle="info",
                                amountused=0,
                                amounttotal=100,
                                metertype='semi',
                                metersize=80,
                                stripethickness=3,
                                meterthickness=5,
                                showtext= True,
                                textright="%",
                                textfont=("Jetbrains Nerd Font",14),
                                subtext="Cpu Usage",
                                stepsize=1,
                                subtextfont=("Jetbrains Nerd Font",4))
cpu_utilization_label.pack()
cpu_utilization_label.place(x=70,y=30)

cpu_speed = tb.Meter(cpu_frame,
                                bootstyle="Success",
                                amountused=0,
                                amounttotal=get_max_cpu_speed(),
                                metertype='full',
                                metersize=85,
                                meterthickness=5,
                                showtext= True,
                                textright="Ghz",
                                textfont=("Jetbrains Nerd Font",14),
                                subtext="Cpu Speed",
                                stepsize=1,
                                subtextfont=("Jetbrains Nerd Font",4))
cpu_speed.pack()
cpu_speed.place(x=205,y=28)
boost_var = tk.BooleanVar()

try:
    with open('checkbox_state.txt', 'r') as file:
        state = file.read()
        boost_var.set(state.lower() == "true")
except FileNotFoundError:
    boost_var.set(False)

cpu_boost_button = tb.Checkbutton(  cpu_frame,
                                    bootstyle= "primary",
                                    variable=boost_var,
                                    style='Roundtoggle.Toolbutton',
                                    onvalue=True,
                                    text="󰓅 Cpu boost",
                                    offvalue=False,
                                    command=toggle_cpu_boost)
cpu_boost_button.pack(padx=200,pady=80)
cpu_boost_button.place(x=360,y=155)


get_ram_consumption_label= tb.Progressbar(cpu_frame,
                                     maximum=get_max_ram(),
                                     length= 130,
                                     orient="vertical",
                                     style='info.TProgressbar'
                                     )
get_ram_consumption_label.pack(padx= 0,pady=0)
get_ram_consumption_label.place(x=20,y=21)

get_ram_consumption_label.start()
get_ram_consumption_label.stop()


get_battery_capacity_label= tb.Progressbar(cpu_frame,
                                     maximum=100,
                                     length= 130,
                                     orient='vertical',
                                     style='danger.TProgressbar'
                                     )
get_battery_capacity_label.pack(padx= 0,pady=0)
get_battery_capacity_label.place(x=494,y=20)

get_battery_capacity_label.start()
get_battery_capacity_label.stop()


label = tb.Label(cpu_frame,
                 bootstyle='success',
                 text="󰍛",
                 font=("Jetbrains Nerd Font",10))
label.pack(padx=200,pady=80)
label.place(x=20,y=157)

label = tb.Label(cpu_frame,
                 bootstyle='success',
                 text="󱊢",
                 font=("Jetbrains Nerd Font",8))
label.pack(padx=200,pady=80)
label.place(x=495,y=157)


ram_label = tb.Label(cpu_frame,
                 foreground="#3498db",
                 font=("Jetbrains Nerd Font",6,"bold"),
                 )
ram_label.pack(padx=150,pady=80)
ram_label.place(x=10,y=5)

battery_label = tb.Label(cpu_frame,
                 foreground="#e74c3c",
                 font=("Jetbrains Nerd Font",6,"bold"),
                )
battery_label.pack(padx=150,pady=80)
battery_label.place(x=490,y=5)


gpu_frame = tb.Frame(root,width=530,height=190,)
gpu_frame.pack(pady=5)


gpu_temp_label = tb.Meter(gpu_frame,
                                bootstyle="danger",
                                arcrange=200,
                                arcoffset=170,
                                amountused=0,
                                amounttotal=100,
                                metertype='semi',
                                metersize=85,
                                #stripethickness=3,
                                meterthickness=5,
                                showtext= True,
                                textright="°C",
                                textfont=("Jetbrains Nerd Font",14),
                                subtext="Gpu Temp",
                                stepsize=1,
                                subtextfont=("Jetbrains Nerd Font",4))
gpu_temp_label.pack()
gpu_temp_label.place(x=347,y=33)


gpu_speed = tb.Meter(gpu_frame,
                                bootstyle="Success",
                                amountused=0,
                                amounttotal=get_max_gpu_clock(),
                                metertype='full',
                                metersize=85,
                                meterthickness=5,
                                showtext= True,
                                textright="Mhz",
                                textfont=("Jetbrains Nerd Font",14),
                                subtext="Gpu Speed",
                                stepsize=1,
                                subtextfont=("Jetbrains Nerd Font",4))
gpu_speed.pack()
gpu_speed.place(x=205,y=28)

gpu_utilization = tb.Meter(gpu_frame,
                                bootstyle="info",
                                amountused=0,
                                amounttotal=100,
                                metertype='semi',
                                metersize=85,
                                stripethickness=3,
                                meterthickness=5,
                                showtext= True,
                                textright="%",
                                textfont=("Jetbrains Nerd Font",14),
                                subtext="Gpu Usage",
                                stepsize=1,
                                subtextfont=("Jetbrains Nerd Font",4))
gpu_utilization.pack()
gpu_utilization.place(x=70,y=30)


get_vram_consumption_label= tb.Progressbar(gpu_frame,
                                     maximum=get_max_vram(),
                                     length= 130,
                                     orient="vertical",
                                     style='info.TProgressbar'
                                     )
get_vram_consumption_label.pack(padx= 0,pady=0)
get_vram_consumption_label.place(x=20,y=21)

get_vram_consumption_label.start()
get_vram_consumption_label.stop()


gpu_memory_label = tb.Label(gpu_frame,
                            foreground="#3498db",
                            font=("Jetbrains Nerd Font",6,"bold"))
gpu_memory_label.pack(padx=200,pady=80)
gpu_memory_label.place(x=10,y=5)


gpu_memory_label_icon = tb.Label(gpu_frame,
                 bootstyle='success',
                 text="󰍛",
                 font=("Jetbrains Nerd Font",8))
gpu_memory_label_icon.pack(padx=200,pady=80)
gpu_memory_label_icon.place(x=20,y=157)


get_gpu_wattage_bar= tb.Progressbar(gpu_frame,
                                     maximum= get_max_gpu_wattage(),
                                     length= 130,
                                     orient="vertical",
                                     style='danger.TProgressbar'
                                     )
get_gpu_wattage_bar.pack(padx= 0,pady=0)
get_gpu_wattage_bar.place(x=494,y=20)

get_gpu_wattage_bar.start()
get_gpu_wattage_bar.stop()

gpu_wattage_label = tb.Label(gpu_frame,
                 foreground="#e74c3c",
                 font=("Jetbrains Nerd Font",6,"bold"),
                )
gpu_wattage_label.pack(padx=150,pady=80)
gpu_wattage_label.place(x=485,y=5)

gpu_wattage_icon_label = tb.Label(gpu_frame,
                 bootstyle='success',
                 text="󱐋",
                 font=("Jetbrains Nerd Font",8))
gpu_wattage_icon_label.pack(padx=200,pady=80)
gpu_wattage_icon_label.place(x=495,y=157)
update_labels()
root.mainloop()
