# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 

import os, re
import socket, random, requests
import subprocess, json
from os.path import expanduser
from subprocess import run
from libqtile import qtile, hook, layout, bar, widget
from libqtile.config import Screen, Key, Drag, Click, Group, Match
from libqtile.command import lazy
from rofi import Rofi
from urllib.request import urlopen
import urllib

#### Variables ####
ver = ' QARSlp v0.9a'
mod = "mod4"
alt = "mod1"                                   
term = "urxvt"
hostname = "gibranlp.dev"
no_internet = 'Internet is working, Everything is fine!'
home = os.path.expanduser('~')
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
backend = ["Wal", "Colorz", "Colorthief","Haishoku"]
rofi_l = Rofi(rofi_args=['-theme', '~/.config/rofi/left_toolbar.rasi'])
rofi_r = Rofi(rofi_args=['-theme', '~/.config/rofi/right_toolbar.rasi'])
widgets = ('widget.TextBox', 'widget.Battery')
widgets_index = 0
#### Hooks ####
@hook.subscribe.startup
def start():
    subprocess.call('/usr/local/bin/alwaystart')
    
@hook.subscribe.startup_once
def start_once():
    subprocess.call('/usr/local/bin/autostart')

@hook.subscribe.client_new
def floating(window):
    floating_types = ['notification', 'toolbar', 'splash', 'dialog','Nextcloud','Gcr-prompter','lxappearance','Pavucontrol','pavucontrol','_NET_WM_WINDOW_TYPE_NORMAL']
    transient = window.window.get_wm_transient_for()
    if window.window.get_wm_type() in floating_types or transient:
        window.floating = True

#### Functions ####

#### Import Used Network Interface ####

def get_net_dev():
    get_dev = "ip addr show | awk '/inet.*brd/{print $NF; exit}'"
    ps = subprocess.Popen(get_dev,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = ps.communicate()[0].decode('ascii').strip()
    return(output)

wifi = get_net_dev()

if wifi.startswith('w'):
    wifi_icon=' '
else:
    wifi_icon=' '

#### Gety IP addreses

def get_private_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip

private_ip = get_private_ip()

def get_public_ip():
    ping = os.system("ping -c 1 " + hostname)
    if ping == 0:
        data = str(urlopen('http://checkip.dyndns.com/').read())
        return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(data).group(1)
    else:
        internet = print('no Internet')
        return(internet)
       
public_ip = get_public_ip()

###### Import Battery for Laptops
def get_bat():
    get_bat = "ls /sys/class/power_supply | grep BAT"
    ps = subprocess.Popen(get_bat,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = ps.communicate()[0].decode('ascii').strip()
    return(output)

batt = get_bat()


##### Import Pywal Palette #####
with open(home + '/.cache/wal/colors.json') as wal_import:
    data = json.load(wal_import)
    wallpaper = data['wallpaper']
    alpha = data['alpha']
    colors = data['colors']
    specials = data['special']
    val_colors = list(colors.values())
    def getList(val_colors):
        return [*val_colors]
    val_specials = list(specials.values())
    def getList(val_specials):
        return [*val_specials]
    
def init_colors():
    return [*val_colors]

def init_specials():
    return [*val_specials]

color = init_colors()
special = init_specials()
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

def set_rand_wallpaper(qtile):
    dir = home + '/Pictures/wallPapers'
    selection = random.choice(os.listdir(dir))
    rand_wallpaper = os.path.join(dir, selection)
    subprocess.run(["wpg", "-s" + rand_wallpaper])
    subprocess.run(["sudo", "cp", "%s" % rand_wallpaper,  "/usr/share/background.png"])
    subprocess.run(["wal", "-R"])
    qtile.cmd_restart()

#### Set randowm wallpaper every X minutes

#### Widgets ####
#### Display Shortcuts widget
def shortcuts(qtile):
    subprocess.run("cat ~/shortc.conf | rofi -theme '~/.config/rofi/left_toolbar.rasi' -i -dmenu -p ' Shortcuts:'",shell=True)

#### Logout widget
def session_widget(qtile):
    options = [' Lock',' Log Out', ' Reboot', ' Poweroff']
    index, key = rofi_r.select('  Session', options)
    if key == -1:
        rofi_r.close()
    else:
        if index == 0:
            os.system('dm-tool switch-to-greeter')
        elif index == 1:
            qtile.cmd_shutdown()
        elif index == 2:
            os.system('systemctl reboot') 
        else:
            os.system('systemctl poweroff') 

#### Screenshot widget
def screenshot(qtile):
    options = [' Screen', ' Window', ' Area', ' 5s Screen']
    index, key = rofi_r.select('  Screenshot mode', options)
    if key == -1:
        rofi.close()
    else:
        if index ==0:
            subprocess.run("scrot 'Sc_%Y-%m-%S_$wx$h.png' -e 'mv $f $$(xdg-user-dir PICTURES) #; viewnior $$(xdg-user-dir PICTURES)/$f' && dunstify ' Screenshot Taken!'",shell=True)
        elif index==1:
            subprocess.run("scrot -u 'Sc_%Y-%m-%S_$wx$h.png' -e 'mv $f $$(xdg-user-dir PICTURES) #; viewnior $$(xdg-user-dir PICTURES)/$f' && dunstify ' Screenshot Taken!'",shell=True)
        elif index==2:
            subprocess.run("scrot -s 'Sc_%Y-%m-%S_$wx$h.png' -e 'mv $f $$(xdg-user-dir PICTURES)  #; viewnior $$(xdg-user-dir PICTURES)/$f'&& dunstify ' Screenshot Taken!'",shell=True)
        else:
            subprocess.run("scrot -d 5 -c 'Sc_%Y-%m-%S_$wx$h.png' -e 'mv $f $$(xdg-user-dir PICTURES) #; viewnior $$(xdg-user-dir PICTURES)/$f' && dunstify ' Screenshot Taken!'",shell=True)

#### Network Widget
def network_widget(qtile):
    #get_ssid = "iwgetid -r"
    #pos = subprocess.Popen(get_ssid,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    #ssid = pos.communicate()[0].decode('ascii').strip()
    get_status = "nmcli radio wifi"
    ps = subprocess.Popen(get_status,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    status = ps.communicate()[0].decode('ascii').strip()
    if status == 'enabled':
        connected = ' Turn Wifi Off'
        active = "off"
    else:
        connected = ' Turn Wifi On'
        active= "on"
    options = [connected,' Bandwith Monitor (CLI)', ' Network Manager (CLI)', ' Network Manager (GUI)']
    index, key = rofi_r.select(wifi_icon, options)
    if key == -1:
        rofi_r.close()
    else:
        if index ==0:
            subprocess.run("nmcli radio wifi " + active, shell=True)
        elif index==1:
            subprocess.run("urxvt -e bmon", shell=True)
        elif index==2:
            subprocess.run("urxvt -e nmtui", shell=True)
        else:
            subprocess.run("nm-connection-editor")        

#### Change Color scheme widget
def change_color_scheme(qtile):
    options = [backend[0],backend[1],backend[2],backend[3], '<<-<< Light Themes >>-->>', backend[0],backend[1],backend[2],backend[3]]
    index, key = rofi_l.select('  Color Scheme', options)
    if key == -1 or index == 4:
        rofi_r.close()
    elif key == 0 and index < 4:
        subprocess.run('wpg -s ' + wallpaper + ' --backend ' + backend[index].lower(), shell=True)
        qtile.cmd_restart()
    elif key == 0 and index > 4:
        subprocess.run('wpg -s ' + wallpaper + ' -L --backend ' + backend[index-5].lower(), shell=True)
        qtile.cmd_restart()
   


#### Multimedia 

def play_pause(qtile):
    qtile.cmd_spawn("playerctl -p spotify play-pause")
    qtile.cmd_spawn("playerctl -p ncspot play-pause")
    qtile.cmd_spawn("playerctl -p vlc play-pause")

def nexts(qtile):
    qtile.cmd_spawn("playerctl -p spotify next")
    qtile.cmd_spawn("playerctl -p ncspot next")
    qtile.cmd_spawn("playerctl -p vlc next")

def prev(qtile):
    qtile.cmd_spawn("playerctl -p spotify previous")
    qtile.cmd_spawn("playerctl -p ncspot previous")
    qtile.cmd_spawn("playerctl -p vlc previous")

def stop(qtile):
    qtile.cmd_spawn("playerctl -p spotify stop")
    qtile.cmd_spawn("playerctl -p ncspot stop")
    qtile.cmd_spawn("playerctl -p vlc stop")


def ncsp(qtile):
    qtile.groups_map["7"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn(term + ' -e ncspot')

def ranger(qtile):
    qtile.groups_map["1"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn(term + ' -e ranger')

def wsearx():
    qtile.groups_map["4"].cmd_toscreen(toggle=False)
    run('/usr/local/bin/wsearch')

def cfilex():
    qtile.groups_map["1"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn('thunar')

#### End Functions ####
