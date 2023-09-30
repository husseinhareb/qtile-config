# Qtile-config
Qtile config and more widgets on my Linux
![Screenshot from 2023-09-29 15-24-15](https://github.com/husseinhareb/qtile-config/assets/88323940/7bcf47e6-0ba7-4a8a-b454-80d3e61b92c3)
Starting with a simple cava configuration with neofetch to match the wallpaper.

Everything you need for this rice can be found in this repo.

The terminal used is kitty.

The bars used are polybar.

Adding to that I created three rofi configuration as follows:
![Screenshot from 2023-09-29 15-25-27](https://github.com/husseinhareb/qtile-config/assets/88323940/e5bc9863-3670-4d7a-9b42-8d54a19766f0)

Rofi with drun for openning apps.
![Screenshot from 2023-09-29 15-25-38](https://github.com/husseinhareb/qtile-config/assets/88323940/2ac1e5b1-fd55-4ff4-940d-31c7d6b6c993)
Power menu options.
![Screenshot from 2023-09-29 15-39-59](https://github.com/husseinhareb/qtile-config/assets/88323940/381aa68e-6e02-450c-a176-7a1fff62412d)
Wifi menu (You can connect easier through **known** wifi networks.
![Screenshot from 2023-09-29 15-31-07](https://github.com/husseinhareb/qtile-config/assets/88323940/a6a3b703-2bb9-41ba-9adb-f0ccc3daa584)
Neovim configuration for maximum productivity with tokyonight theme and very other helpful plugins.
![Screenshot from 2023-09-29 15-52-51](https://github.com/husseinhareb/qtile-config/assets/88323940/a162b223-7689-42fd-97fb-5c4aa78e11b1)
I developed a variety of Python widgets using tkinter and ttkboostrap, each one for distinct functionalities, as shown in the picture above. These widgets provide convenient access to features such as the calendar and adjustment of audio and display settings.
![Screenshot from 2023-09-29 15-25-57](https://github.com/husseinhareb/qtile-config/assets/88323940/246f9fae-1017-4888-9693-bf40dc0b7a1c)
Finally, there is a hardware monitor widget that retrieves essential information from the computer's hardware, including details about the CPU, GPU, and RAM. Additionally, it includes a functionality to enable or disable CPU boosting, which can be advantageous on laptops for longer battery time.

You are welcome to copy any of my dotfiles or scripts you come across here.However, I advise against attempting to duplicate the entire setup, as it lacks organization and is tailored to my specific requirements.

These widgets are done on a **1080x1920** resolution screen with nvidia drivers.

NOTE:The spotify polybar need `spotifyd` for it to work. 

NOTE:If the icons didn't load try installing `Symbols Nerd Fonts`.

NOTE:The hardware monitor and the brightness widget only works on nvidia drivers

NOTE:Don't forget to make all of the bash files executable by using `chmod +x /path/to/file`.

NOTE:You should add your city and an API key in the python script for the weather, you can get one for free from [here](https://openweathermap.org/) .

NOTE:The packages needed for the hardware monitor to work are: `python3 python-psutil python-tkinter python-ttkbootstrap nvidia nvidia-smi`
