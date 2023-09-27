#!/bin/sh
(polybar power)&
(polybar clock)&
(polybar spotify)&
(polybar workspaces)&
(polybar monitor)&
(polybar wifi)&
(polybar settings)&
(polybar sound)&
(polybar weather)&

dunst&

picom --experimental-backends b 
