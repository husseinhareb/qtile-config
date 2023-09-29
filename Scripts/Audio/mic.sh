#!/bin/bash

mic_source=$(pactl info | grep "Default Source:" | awk '{print $3}')

if [ "$1" == "1" ]; then
  # Left mouse button clicked - toggle microphone mute status
  pactl set-source-mute "$mic_source" toggle
fi

# Get the microphone status (mute/unmute)
mic_status=$(pactl list sources | awk -v mic_source="$mic_source" '/^Source/ {in_source=0} $0 ~ ("Name: " mic_source) {in_source=1} in_source && /Mute:/ {print $2}')

mic_volume=$(pactl list sources | awk -v mic_source="$mic_source" '/^Source/ {in_source=0} $0 ~ ("Name: " mic_source) {in_source=1} in_source && /Volume:/ {print $5}')

# Convert the volume to percentage
mic_percentage=$(awk -v volume="$mic_volume" 'BEGIN {split(volume, a, "%"); print a[1]}')

# Check the microphone status and set the output accordingly
if [ "$mic_status" == "yes" ]; then
   echo " Muted"
else
   echo " $mic_percentage%"
fi
