# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 

import os
import socket, random
import subprocess, json
from os.path import expanduser
from subprocess import run
from libqtile import qtile, hook, layout, bar, widget
from libqtile.config import Screen, Key, Drag, Click, Group, Match
from libqtile.command import lazy

#### Variables ####

mod = "mod4"
alt = "mod1"                                   
term = "urxvt"
home = os.path.expanduser('~')
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
backend = ["Wal", "Colorz", "Colorthief","Haishoku"]
#### Hooks ####
@hook.subscribe.startup
def start():
    subprocess.call('/opt/bin/alwaystart')
    

@hook.subscribe.startup_once
def start_once():
    subprocess.call('/opt/bin/autostart')



@hook.subscribe.client_new
def floating(window):
    floating_types = ['notification', 'toolbar', 'splash', 'dialog','Nextcloud','Gcr-prompter','lxappearance','Pavucontrol','pavucontrol','_NET_WM_WINDOW_TYPE_NORMAL']
    transient = window.window.get_wm_transient_for()
    if window.window.get_wm_type() in floating_types or transient:
        window.floating = True

#### Functions ####

#### Import Network Interface ####

with open(home + '/.config/qtile/actnet', 'r') as file:
    netact = file.read().replace('\n', '')

##### Import Pywal Palette #####

with open(home + '/.cache/wal/colors.json') as json_file:
    data = json.load(json_file)
    colorsarray = data['colors']
    val_list = list(colorsarray.values())
    def getList(val_list):
        return [*val_list]

def init_colors():
    return [*val_list]

#### Send app to group ####

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

##### Specific Apps/Groups / Apps/Grupos especificos #####

def app_or_group(group, app):
    def f(qtile):
        if qtile.groups_map[group].windows:
            qtile.groups_map[group].cmd_toscreen(toggle=False)
            qtile.cmd_spawn(app)
        else:
            qtile.groups_map[group].cmd_toscreen(toggle=False)
            qtile.cmd_spawn(app)
    return f

#### Set Random Wallpaper ####

def set_wallpaper(qtile):
    dir = home + '/Pictures/wallPapers'
    wallpaper = random.choice(os.listdir(dir))
    random_wallpaper = os.path.join(dir, wallpaper)
    with open (home + "/.config/qtile/current_wallpaper", "w") as currentWal:
        currentWal.write(random_wallpaper)
    subprocess.run(["wpg", "-s" + random_wallpaper])
    subprocess.run(["sudo", "cp", "%s" % random_wallpaper,  "/usr/share/backgrounds/background.png"])
    subprocess.run(["wal", "-R"])
    qtile.cmd_restart()

#### Change Color Scheme with same wallpaper ####

def change_scheme(qtile):
    with open (home + "/.config/qtile/current_wallpaper", "r") as currentWal:
        currentWal.read()
    subprocess.run(["wpg", "-s" + currentWal])
    qtile.cmd_restart()


def ncsp(qtile):
    qtile.groups_map["7"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn(term + ' -e ncspot')

def ranger(qtile):
    qtile.groups_map["1"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn(term + ' -e ranger')

def wsearx():
    qtile.groups_map["4"].cmd_toscreen(toggle=False)
    run('/opt/bin/wsearch')

def cfilex():
    qtile.groups_map["1"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn('nautilus')

def ksearx(qtile):
    qtile.groups_map["4"].cmd_toscreen(toggle=False)
    run('/opt/bin/wsearch')

def wnetw():
    qtile.cmd_spawn('/opt/bin/network')


def wsess():
    run('/opt/bin/logout')
#### End Functions ####

color = init_colors()