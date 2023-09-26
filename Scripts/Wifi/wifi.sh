#!/bin/bash

wifi_list=$(nmcli -t -f SSID,SIGNAL dev wifi list)

formatted_list=""
while IFS=':' read -r ssid signal; do
    if ((signal < 30)); then
        signal_symbol="󰤟"
    elif ((signal < 60)); then
        signal_symbol="󰤢"
    elif ((signal < 90)); then
        signal_symbol="󰤥"
    else
        signal_symbol="󰤨" 
    fi
    formatted_list+=" $signal_symbol $ssid\n"
done <<< "$wifi_list"

chosen=$(echo -e "$formatted_list" | rofi -theme ~/.config/rofi/wifi.rasi -dmenu -p "Wi-Fi networks:" | awk -F ' ' '{print $2}' | xargs)

if [ -n "$chosen" ]; then
    nmcli device wifi connect "$chosen"
fi
