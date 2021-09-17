# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 

import os, random
import subprocess
from os.path import expanduser

rofi_theme = "rofi -theme ~/.config/rofi/logout.rasi"
log_out = " Log Out"
reboot = " Reboot"
power_off = " Poweroff"

options = [log_out, reboot, power_off]

def logout():
    for option in options:
        print(option)
        return option
