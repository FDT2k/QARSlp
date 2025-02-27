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
from qtile_extras import widget

#### Variables ####
ver = ' QARSlp v1.1'
mod = "mod4"
alt = "mod1"                                   
term = "urxvt"
home = os.path.expanduser('~')
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
#### Internet Chekup ####
internet = ' Yei Internet is working!'
#### Themes ####
theme=['default', 'top_bar', 'bottom_bar', 'minimal']
backend = ["Wal", "Colorz", "Colorthief","Haishoku"]
rofi_l = Rofi(rofi_args=['-theme', '~/.config/rofi/left_toolbar.rasi'])
rofi_r = Rofi(rofi_args=['-theme', '~/.config/rofi/right_toolbar.rasi'])
widgets = ('widget.TextBox', 'widget.Battery')
widgets_index = 0
#### Weather ####
w_appkey = "e45a0f07f0c675b273ef8636663941db"
w_cityid = "3520914"

#### Hooks ####
@hook.subscribe.startup
def start():
    subprocess.call('/usr/local/bin/alwaystart')
    wraith_colors()
    
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

#### Gety IP addreses Private / Public

def get_private_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip

private_ip = get_private_ip()

def get_public_ip():
    try:
        raw = requests.get('https://api.duckduckgo.com/?q=ip&format=json')
        answer = raw.json()["Answer"].split()[4]
    except Exception as e:
        return "0.0.0.0"
    else:
        return answer
       
public_ip = get_public_ip()

if public_ip.startswith('0'):
    internet = "OMG You Have No Internet"

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
    val_colors = list(colors.values())
    def getList(val_colors):
        return [*val_colors]
    
def init_colors():
    return [*val_colors]

color = init_colors()

def wraith_colors():
    subprocess.Popen(['sudo cm-rgb-cli set logo --mode=static --brightness=5 --color=%s fan --mode=static --brightness=5 --color=%s ring --mode=swirl --speed=2 --brightness=5 --color=%s' %(color[1], color[2], color[6])], shell = True)

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

##### Specific Apps/Groups #####
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
    subprocess.run(["sudo", "cp", "%s" % rand_wallpaper,  "/usr/share/backgrounds/background.png"])
    subprocess.run(["wal", "-R"])
    qtile.cmd_restart()

#### Functions for Widgets ####
#### Display Shortcuts widget
def shortcuts(qtile):
    subprocess.run("cat ~/.shortcuts | rofi -theme '~/.config/rofi/left_toolbar.rasi' -i -dmenu -p ' Shortcuts:'",shell=True)

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
            subprocess.run("scrot -d 1 'Sc_%Y-%m-%S_$wx$h.png' -e 'mv $f $$(xdg-user-dir PICTURES) #; viewnior $$(xdg-user-dir PICTURES)/$f' && dunstify ' Screenshot Taken!'",shell=True)
        elif index==1:
            subprocess.run("scrot -u 'Sc_%Y-%m-%S_$wx$h.png' -e 'mv $f $$(xdg-user-dir PICTURES) #; viewnior $$(xdg-user-dir PICTURES)/$f' && dunstify ' Screenshot Taken!'",shell=True)
        elif index==2:
            subprocess.run("scrot -s 'Sc_%Y-%m-%S_$wx$h.png' -e 'mv $f $$(xdg-user-dir PICTURES)  #; viewnior $$(xdg-user-dir PICTURES)/$f'&& dunstify ' Screenshot Taken!'",shell=True)
        else:
            subprocess.run("scrot -d 5 -c 'Sc_%Y-%m-%S_$wx$h.png' -e 'mv $f $$(xdg-user-dir PICTURES) #; viewnior $$(xdg-user-dir PICTURES)/$f' && dunstify ' Screenshot Taken!'",shell=True)

#### Network Widget
def network_widget(qtile):
    get_ssid = "iwgetid -r"
    pos = subprocess.Popen(get_ssid,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    ssid = pos.communicate()[0].decode('ascii').strip()
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
    index, key = rofi_r.select(wifi_icon + internet, options)
    if key == -1:
        rofi_r.close()
    else:
        if index ==0:
            subprocess.run("nmcli radio wifi " + active, shell=True)
        elif index==1:
            qtile.cmd_spawn(term + ' -e bmon')
        elif index==2:
            qtile.cmd_spawn(term + ' -e nmtui')
        else:
            qtile.cmd_spawn('nm-connection-editor')
                 

#### Change Theme widget ####
def change_theme(qtile):
    options = [theme[0],theme[1],theme[2],theme[3]]
    index, key = rofi_l.select('  Color Scheme', options)
    if key == -1 or index >= 4:
        rofi_r.close()
    elif key == 0 and index < 4:
        subprocess.run('\cp ~/.config/qtile/themes/%s/theme.py ~/.config/qtile/'% theme[index], shell=True)
        subprocess.run('\cp ~/.config/qtile/themes/%s/rofi/* ~/.config/rofi/' % theme[index],shell=True)
        qtile.cmd_restart()

#### Change Color scheme widget ####
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

#### Multimedia #### 
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

#### Internet Search ####
def wsearx():
    run('/usr/local/bin/wsearch')

#### Files/Folders Search ####
def cfilex():
    qtile.groups_map["1"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn('thunar')

#### End Functions ####


##### Groups #####
group_names = ["1","2","3","4","5","6","7","8","9"]
group_labels=["","","","","","","","",""]
group_layouts=["monadtall", "matrix", "matrix","monadtall", "monadtall", "monadtall","monadtall", "monadtall", "monadtall"]
group_matches=[
    [Match(wm_class=['gnome-disks','Gnome-disks','anydesk','Anydesk'])],
    [Match(wm_class=['Zoom','zoom', 'Thunderbird', 'thunderbird','transmission-gtk','Transmission-gtk', 'Simplenote', 'filezilla', 'Filezilla', 'QOwnNotes'])],
    [Match(wm_class=['whatsdesk','telegram-desktop-bin', 'TelegramDesktop', 'Discord', 'discord', 'slack', 'ferdi', 'Slack', 'Ferdi'])],
    [Match(wm_class=['firefox', 'google-chrome', 'Google-chrome'])],
    [Match(wm_class=['Code', 'code','Filezilla','typora'])],
    [Match(wm_class=['Gimp-2.10','Inkscape','Evince', 'libreoffice','Com.github.phase1geo.minder', 'libreoffice-writer', 'libreoffice-calc', 'libreoffice-impress', 'libreoffice-draw', 'libreoffice-calc'])],
    [Match(wm_class=['Spotify', 'spotify'])],
    [Match(wm_class=['VirtualBox Manager', 'VirtualBox Machine', 'Steam', 'steam'])],
    None
]
groups = []

@hook.subscribe.client_new
def follow_window(client):
    for group in groups:
        match = next((m for m in group.matches if m.compare(client)), None)
        if match:
            targetgroup = qtile.groups_map[group.name]
            targetgroup.cmd_toscreen(toggle=False)
            break

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            matches=group_matches[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

#### End Groups ####


#### Layouts ####
def init_layout_theme():
    return {"font":"Fira Code Medium",
            "fontsize":14,
            "margin": 5,
            "border_width":3,
            "border_normal":color[0],
            "border_focus":color[1],
            "single_margin":0,
            "single_border_width":0,
           }

layout_theme = init_layout_theme()

def init_layouts():
    return [
        layout.Matrix(
            **layout_theme),
        layout.MonadTall(
            max_ratio=0.90,
            ratio=0.70,
            **layout_theme),
        layout.TreeTab(
            sections = ["Worskpace"],
            section_fontsize=15,
            bg_color=color[0],
            active_bg=color[8],
            active_fg=color[0],
            inactive_bg=color[0],
            inactive_fg=color[7],
            padding_left = 0,
            padding_x = 0,
            padding_y = 5,
            section_top = 10,
            section_bottom = 20,
            level_shift = 8,
            vspace = 3,
            panel_width = 250,
            **layout_theme),
        layout.Floating(
            **layout_theme)
            ]

floating_layout = layout.Floating(auto_float_rules=[
    Match(title='Confirmation'),  # tastyworks exit box
    Match(title='Qalculate!'),  # qalculate-gtk
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='branchdialog'),
    Match(wm_class='pinentry'),
    Match(wm_class='ssh-askpass'),
    Match(wm_class='Obconf')
])
layouts = init_layouts()
#### End layouts ####
