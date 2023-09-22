import subprocess

command = "cal"

try:
    output = subprocess.check_output(command, shell=True, text=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
