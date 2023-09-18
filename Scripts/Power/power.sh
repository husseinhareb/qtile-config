#!/usr/bin/env bash

uptime=$(uptime -p | sed -e 's/up //g')
dir="~/.config/rofi/"
rofi_command="rofi -theme $dir/power.rasi"

# Options
terminal=""
shutdown="󰐥"
reboot="󰜉"
suspend="󰒲"
lock=""
logout=""