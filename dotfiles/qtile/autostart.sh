#!/usr/bin/env bash
# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
# 
ip addr show | awk '/inet.*brd/{print $NF; exit}' | tee ~/.config/qtile/actnet &
setxkbmap -layout us -variant intl &
picom --config ~/.config/qtile/picom.conf &
numlockx on &
nextcloud &
kdeconnect-indicator &
rand &
