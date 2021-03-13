# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing System
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
import os, re, subprocess
from libqtile import hook

@hook.subscribe.startup_once
def start_once():
    subprocess.call('/opt/bin/autostart')

@hook.subscribe.startup
def start():
    subprocess.call('/opt/bin/alwaystart')

@hook.subscribe.screen_change
def restart_on_randr():
    #qtile.cmd_spawn('urxvt -e xrandr --output HDMI1 --auto --right-of eDP1')
	qtile.cmd_restart()

@hook.subscribe.client_new
def floating(window):
    floating_types = ['notification', 'toolbar', 'splash', 'dialog','Nextcloud','Gcr-prompter','lxappearance','Pavucontrol','pavucontrol','_NET_WM_WINDOW_TYPE_NORMAL']
    transient = window.window.get_wm_transient_for()
    if window.window.get_wm_type() in floating_types or transient:
        window.floating = True