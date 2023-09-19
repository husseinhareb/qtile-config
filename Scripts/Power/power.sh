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

options="$terminal\n$lock\n$suspend\n$logout\n$reboot\n$shutdown"

chosen="$(echo -e "$options" | $rofi_command -p "Uptime: $uptime" -dmenu -selected-row 0)"
case $chosen in
    $shutdown)
        systemctl poweroff
        ;;
    $reboot)
        systemctl reboot
        ;;
    $lock)
        i3lock
        ;;
    $suspend)
        mpc -q pause
        amixer set Master mute
        systemctl suspend
        ;;
    $logout)
        if [[ "$DESKTOP_SESSION" == "Openbox" ]]; then
            openbox --exit
        elif [[ "$DESKTOP_SESSION" == "bspwm" ]]; then
            bspc quit
        elif [[ "$DESKTOP_SESSION" == "i3" ]]; then
            i3-msg exit
        fi
        ;;
    $terminal)
        kitty ~/
        ;;
esac
