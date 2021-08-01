# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
import os
import re
import socket
import subprocess
import json
from libqtile import qtile
from libqtile import hook
from libqtile.command import lazy
from libqtile.config import Screen, Key, Group, Match, Drag, Click, Rule
from libqtile import qtile, layout, bar, widget
from libqtile.lazy import lazy
from subprocess import run

#### Variables ####
mod = "mod4"
alt = "mod1"                                   
term = "alacritty"
home = os.path.expanduser('~')
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
#### End variables ####

##### Import Pywal Palette #####
with open(home + '/.cache/wal/colors.json') as json_file:
    data = json.load(json_file)
    colorsarray = data['colors']
    val_list = list(colorsarray.values())
    def getList(val_list):
        return [*val_list]

def init_colors():
    return [*val_list]

colors = init_colors()

##### End Import Pywal Palette #####



#### Import Network Interface ####

with open(home + '/.config/qtile/actnet', 'r') as file:
    netact = file.read().replace('\n', '')

#### End Import Network Interface ####


#### Hooks ####

@hook.subscribe.startup_once
def start_once():
    subprocess.call('/opt/bin/autostart')

@hook.subscribe.startup
def start():
    subprocess.call('/opt/bin/alwaystart')
    subprocess.call('/opt/bin/wvis')

@hook.subscribe.screen_change
def restart_on_randr():
    qtile.cmd_spawn(term + ' -e xrandr --output HDMI1 --auto --right-of eDP1')
    qtile.cmd_restart()

@hook.subscribe.client_new
def floating(window):
    floating_types = ['notification', 'toolbar', 'splash', 'dialog','Nextcloud','Gcr-prompter','lxappearance','Pavucontrol','pavucontrol','_NET_WM_WINDOW_TYPE_NORMAL']
    transient = window.window.get_wm_transient_for()
    if window.window.get_wm_type() in floating_types or transient:
        window.floating = True

#### End hooks ####

##### Functions #####

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

def ncsp(qtile):
    qtile.groups_map["7"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn(term + ' -e bash -c ". ~/.zshrc; ncspot"')

def ranger(qtile):
    qtile.groups_map["1"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn(term + ' -e bash -c ". ~/.zshrc; ranger"')

def cranger(qtile):
    qtile.groups_map["1"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn(term + ' -e bash -c ". ~/.zshrc; ranger"')

def wsearx():
    qtile.groups_map["4"].cmd_toscreen(toggle=False)
    run('/opt/bin/wsearch')

def cthunar():
    qtile.groups_map["1"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn('thunar')

def ksearx(qtile):
    qtile.groups_map["4"].cmd_toscreen(toggle=False)
    run('/opt/bin/wsearch')

def wnetw():
    qtile.cmd_spawn('/opt/bin/network')


def wsess():
    run('/opt/bin/logout')

#### End Functions ####

#### Layouts ####
def init_layout_theme():
    return {"font":"Fira Code Medium",
            "fontsize":16,
            "margin": 10,
            "border_width":3,
            "border_normal":colors[0],
            "border_focus":colors[5],
            "single_margin":0,
            "single_border_width":0,
           }

def init_layouts():
    return [#layout.MonadWide(**layout_theme),
            #layout.Bsp(**layout_theme),
            #layout.Stack(stacks=2, **layout_theme),
            #layout.Columns(**layout_theme),
            #layout.RatioTile(**layout_theme),
            #layout.VerticalTile(**layout_theme),
            #layout.Tile(shift_windows=True, **layout_theme),
            layout.Matrix(**layout_theme),
            #layout.Zoomy(**layout_theme),
            layout.MonadTall(max_ratio=0.80, ratio=0.70, **layout_theme),
            #layout.Max(**layout_theme),
            layout.TreeTab(sections=["Tabs"],section_fontsize=15, bg_color=colors[0], active_bg=colors[7], active_fg=colors[0], inactive_bg=colors[0], inactive_fg=colors[7],padding_y=5,panel_width=250, **layout_theme),
            layout.Floating(**layout_theme)]

#### End layouts ####

##### Groups #####

groups = [
    Group("1",position=1,matches=[Match(wm_class=['thunar', 'Thunar', 'gnome-disks', 'Gnome-disks', 'anydesk', 'Simplenote', 'Anydesk'])],layout="monadtall",label=""),
    Group("2",position=2,matches=[Match(wm_class=['Zoom','zoom', 'Mailspring', 'mailspring', 'transmission-gtk','Transmission-gtk'])],layout="monadtall",label=""),
    Group("3",position=3,matches=[Match(wm_class=['whatsdesk','telegram-desktop-bin', 'TelegramDesktop', 'Discord', 'discord'])],layout="matrix",label=""),
    Group("4",position=4,matches=[Match(wm_class=['firefox'])],layout="monadtall",label=""),
    Group("5",position=5,matches=[Match(wm_class=['Code', 'code','Filezilla'])],layout="monadtall",label=""),
    Group("6",position=6,matches=[Match(wm_class=['Gimp-2.10','Inkscape','Evince', 'libreoffice','Com.github.phase1geo.minder'])],layout="monadtall",label=""),
    Group("7",position=7,layout="monadtall",label=""),
    Group("8",position=8,matches=[Match(wm_class=['VirtualBox Manager', 'VirtualBox Machine'])],layout="monadtall",label=""),
    Group("9",position=9,layout="monadtall",label="")]

#### End Groups ####

#### Keys ####

def init_keys():
    keys = [ 
            #### Basics ####          
            Key([mod], "Return", lazy.spawn(term)), # Open Terminal
            Key([mod, "shift"], "Return", lazy.spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show drun')),
            Key([mod, "mod1"], "Return", lazy.spawn('sudo rofi -theme "~/.config/rofi/launcher.rasi" -show drun')), 
            Key([mod], "q",lazy.window.kill()), # Close Window 
            Key([mod, "shift"], "r",lazy.restart()), # Restart Qtile
            Key([mod, "shift"], "q",lazy.shutdown()), # Logout 
            Key([mod], "Escape", lazy.spawn('xkill')), # Click window to close
            
            #### Widgets
            Key([mod],"h",lazy.spawn('/opt/bin/shortc')), # Sortcurts widget
            Key([mod],"p",lazy.spawn('/opt/bin/qback')), # Launcher
            Key([mod],"f",lazy.function(ksearx)), # WEB Search
            Key([mod],"x",lazy.spawn('/opt/bin/logout')),
            Key([mod],"n",lazy.spawn('/opt/bin/network')),
            Key([mod, "shift"],"w",lazy.spawn('/opt/bin/qback')),
            Key([mod, "shift"],"c",lazy.spawn('/opt/bin/fans')),
            #### Theming ####
            Key([mod], "w",lazy.spawn('/opt/bin/genwal')), # Set randwom wallpaper / colors to entire system

            #### Apps ####

            Key([mod],"e",lazy.function(app_or_group("1", "thunar"))), #File manager
            Key([mod, "shift"],"e",lazy.function(ranger)), # CLI file manager

            Key([mod, "shift"],"a",lazy.function(app_or_group("1", "anydesk"))),
            Key([mod, "shift"],"s",lazy.function(app_or_group('1', 'simplenote'))),

            ## Group 2 (Organization)
            Key([mod],"m",lazy.function(app_or_group('2', 'mailspring'))),
           

            ## Group 2 (Social: Whatsapp, Telegram, )
            Key([mod, "shift"],"t",lazy.function(app_or_group('3', 'telegram-desktop'))),
            Key([mod, "shift"],"d",lazy.function(app_or_group('3', 'discord'))),


            ## Group 3 (WEB: Firefox)(Admin: Mail, notes, social)
            Key([mod, "shift"],"f",lazy.function(app_or_group('4', 'firefox'))),
            

            ## Group 4 (Code/Write/Office: visual studio, typora, onlyofice)
            Key([mod],"v",lazy.function(app_or_group('5', 'code'))),
            Key([mod],"o",lazy.function(app_or_group("6", 'libreoffice'))),
            Key([mod],"c",lazy.function(app_or_group('5', 'code'))),

            ## Group 5 (Design: Gimp, Inkscape, feh)
            Key([mod],"g",lazy.function(app_or_group('6', 'gimp'))),

            ## Group 6 (Virtual Stuff games)
            Key([mod, "shift"],"v",lazy.spawn(term + ' -e bash -c ". ~/.zshrc; vis"')),
            Key([mod],"b",lazy.function(app_or_group('8', '/home/gibranlp/albiononline/./Albion-Online'))),

            ## Group 7 (Música)
            Key([mod],"s",lazy.function(ncsp)),
            
            #### Layouts ####
            Key([mod], "Tab",lazy.layout.down()), # Change focus of windows down
            Key([mod, "shift"], "Tab",lazy.layout.up()), # Change focus of windows up
            Key([alt], "Tab", lazy.layout.swap_left()),
            Key([alt, "shift"], "Tab", lazy.layout.swap_right()),
            #Key([mod], "h", lazy.layout.left()),
            #Key([mod], "l", lazy.layout.right()),
            #Key([mod], "Up", lazy.layout.down()),
            #Key([mod], "Down", lazy.layout.up()),

            #### Brightness
            Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
            Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

            #### Volume
            Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
            Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
            Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

            #### Media Control
            #Key([mod], "v", lazy.spawn('/home/gibranlp/MEGA/computerStuff/keyboard/keyboard_activate.sh')),
            #Key([mod], "b", lazy.spawn('/home/gibranlp/MEGA/computerStuff/keyboard/keyboard_deactivate.sh')),
            Key([], "XF86AudioPlay", lazy.spawn("playerctl -p ncspot play-pause")),
            Key([], "XF86AudioNext", lazy.spawn("playerctl -p ncspot next")),
            Key([], "XF86AudioPrev", lazy.spawn("playerctl -p ncspot previous")),
            Key([], "XF86AudioStop", lazy.spawn("playerctl -p ncspot stop")),

            ### Window hotkeys
            Key([alt], "f", lazy.window.toggle_fullscreen()),
            Key([alt, "shift"], "f", lazy.window.toggle_floating()),
            Key([mod], "space", lazy.next_layout()),

            # Resize windows
            Key([mod, "shift"], "Up", lazy.layout.grow()),
            Key([mod, "shift"], "Down", lazy.layout.shrink()),
            Key([mod, "shift"], "space", lazy.layout.flip()),

            # Change focus
            Key([mod], "Up", lazy.layout.up()),
            Key([mod], "Down", lazy.layout.down()),
            Key([mod], "Left", lazy.layout.left()),
            Key([mod], "Right", lazy.layout.right()),

            ### Screenshots
            Key([], "Print", lazy.spawn('/opt/bin/screenshot')),]

    for i in groups:
            keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))
            keys.append(Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)))
    return keys

#### Widgets ####

def init_widgets_defaults():
    return dict(font="Fira Code Medium",fontsize=16,padding=2,background=colors[0])

def init_wid_list_top():    
    wid_list_top = [
                #### Shortcuts ####
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    foreground=colors[7],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show drun')},
                    fontshadow=colors[3]
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    foreground=colors[7],
                    text="",
                    mouse_callbacks={'Button1': wsearx},
                    fontshadow=colors[3]
                    ),        
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    foreground=colors[7],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term)},
                    fontshadow=colors[3]
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    foreground=colors[7],
                    text="",
                    mouse_callbacks={'Button1': cthunar},
                    fontshadow=colors[3]
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    foreground=colors[7],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/opt/bin/genwal')},
                    fontshadow=colors[3]
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    foreground=colors[7],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/opt/bin/shortc')},
                    fontshadow=colors[3]
                    ),
                widget.TextBox(
                    foreground=colors[1],
                    text="◢",
                    fontsize=45,
                    padding=-2
                    ),
                #### Groups ####
                widget.GroupBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    disable_drag=True,
                    hide_unused=False,
                    fontshadow=colors[0],
                    margin_y=1,
                    padding_x=5,
                    borderwidth=0,
                    active=colors[7],
                    inactive=colors[1],
                    rounded=False,
                    highlight_method="text",
                    this_current_screen_border=colors[0],
                    this_screen_border=colors[3],
                    other_current_screen_border=colors[0],
                    other_screen_border=colors[0],
                    foreground=colors[2],
                    background=colors[1]
                    ),
                #### Notification ####
                widget.Prompt(
                    prompt = prompt,
                    foreground=colors[0],
                    background = colors[1]
                    ),
                widget.TextBox(
                    background=colors[0],
                    foreground=colors[1],
                    text="◤",
                    fontsize=45,
                    padding=-2
                    ),
                #### Notifications ####
                widget.Notify(
                    default_timeout=30,
                    foreground=colors[7],
                    background=colors[0],
                    max_chars=50,
                    foreground_urgent='ff0000',
                    action=True,
                    ),
                widget.WindowName(
                    foreground=colors[7],
                    background=colors[0],
                    padding=5,
                    format='{state}{name}',
                    empty_group_string='QARSlp',
                    max_chars=35
                    ),
                #### Spacer ####
                #widget.Spacer(
                #    length=bar.STRETCH,
                #    background=colors[0],
                #    foreground=colors[0]
                #    ),   
                #### Spotify ####
                widget.TextBox(
                    text="◢",
                    background=colors[0],
                    foreground=colors[6],
                    padding=-2,
                    fontsize=45
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,text="",
                    padding=5,
                    foreground=colors[0],
                    background=colors[6],
                    fontshadow=colors[7],
                    mouse_callbacks={'Button1': ncsp}
                    ),
                widget.Mpris2(
                    name='ncspot',
                    objname='org.mpris.MediaPlayer2.ncspot',
                    scroll_chars=30,
                    background=colors[6],
                    foreground=colors[0],
                    stop_pause_text='',
                    display_metadata=['xesam:artist','xesam:title'],
                    scroll_interval=0.5,
                    scroll_wait_intervals=2000
                    ),
                #### Layouts ####
                widget.TextBox(
                    text="◢",
                    background=colors[6],
                    foreground=colors[2],
                    padding=-2,
                    fontsize=45
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    background=colors[2],
                    foreground=colors[0],
                    fontshadow=colors[7],
                    text=""
                    ),
                widget.CurrentLayout(
                    background=colors[2],
                    foreground=colors[0]
                    ),
                #### Pomodoro ####
                widget.TextBox(
                    text='◢',
                    background=colors[2],
                    foreground=colors[5],
                    padding=-2,
                    fontsize=45
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    background=colors[5],
                    foreground=colors[0],
                    text="",
                    fontshadow=colors[7]
                    ),
                widget.Pomodoro(
                    background=colors[5],
                    foreground=colors[0],
                    color_active=colors[0],
                    color_break=colors[2],
                    color_inactive=colors[0],
                    length_pomodori=50,
                    length_short_break=5,
                    length_long_break=15,
                    num_pomodori=3,
                    prefix_break='Break',
                    prefix_inactive='start',
                    prefix_long_break='Long Break',
                    prefix_paused=''
                    ),
                #### Updates ####
                widget.TextBox(
                    text='◢',
                    background=colors[5],
                    foreground=colors[3],
                    padding=-2,
                    fontsize=45
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    background=colors[3],
                    foreground=colors[0],
                    fontshadow=colors[7],
                    text=" ",
                    ),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro='Arch',
                    foreground=colors[0],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e bash -c ". ~/.zshrc; sudo pacman -Syu"')},
                    display_format="{updates} updates",
                    background=colors[3],
                    colour_have_updates=colors[0],
                    colour_no_updates=colors[0]
                    ),
                #### Khal Calendar ####
                #widget.KhalCalendar(lookahead=15, remindertime=60, foreground=colors[0], background=colors[7]),
                #### Sound Control ####
                widget.TextBox(
                    text='◢',
                    background=colors[3],
                    foreground=colors[7],
                    padding=-2,
                    fontsize=45
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    text=" ",
                    foreground=colors[0],
                    background=colors[7],
                    padding=0,
                    fontsize=15,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
                    fontshadow=colors[3]
                    ),
                widget.Volume(
                    channel='Master',
                    background=colors[7],
                    foreground=colors[0],
                    fontshadow=colors[7]
                    ),
                #widget.Backlight(
                #    background=colors[7],
                #    foreground=colors[0],
                #    fontshadow=colors[7]
                #    ),
                #### Date Clock Session Control ####
                widget.TextBox(
                    text='◢',
                    background=colors[7],
                    foreground=colors[0],
                    padding=-2,
                    fontsize=45
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    padding=1,
                    text="",
                    fontsize=15,
                    foreground=colors[7],
                    background=colors[0],
                    fontshadow=colors[3]
                    ),
                widget.Clock(
                    foreground=colors[7],
                    background=colors[0],
                    format="%b %a %d %H:%M",
                    update_interval=1
                    ),
                #### Lock, Logout, Poweroff ####
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    foreground=colors[7],
                    text="",
                    mouse_callbacks={'Button1': wsess},
                    fontshadow=colors[3]
                    ),
    ]
    return wid_list_top

def in_wid_list_bot():
    wid_list_bot = [
                #widget.DebugInfo(foreground=colors[7], background=colors[0], fontshadow=colors[2]),
                #### Spacer ####
                widget.Spacer(
                    length=bar.STRETCH,
                    background=colors[0],
                    foreground=colors[0]
                    ),   
                #### Network ####
                widget.TextBox(
                    text='◢',
                    background=colors[0],
                    foreground=colors[5],
                    padding=-2,
                    fontsize=45
                    ),
                widget.Net(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    interface=netact,
                    format='',
                    foreground=colors[0],
                    background=colors[5],
                    fontshadow=colors[7],
                    mouse_callbacks={'Button1': wnetw}
                    ),
                widget.Wlan(
                    interface=netact,
                    format='{essid} {percent:2.0%} ',
                    disconnected_message='Unplugged',
                    foreground=colors[0],
                    background=colors[5],
                    mouse_callbacks={'Button1':wnetw}
                    ),
                widget.Net(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    interface=netact,
                    format='{down} ↓↑ {up}',
                    foreground=colors[0],
                    background=colors[5],
                    use_bits=True,
                    mouse_callbacks={'Button1':wnetw}
                    ),
                #### Bitcoin ####
                #widget.TextBox(
                #    text="◢",
                #    background=colors[5],
                #    foreground=colors[3],
                #    padding=-2,
                #    fontsize=45
                #    ),
                #widget.BitcoinTicker(
                #    background=colors[3],
                #    foreground=colors[0]
                #    ),
                widget.TextBox(
                    text="◢",
                    background=colors[5],
                    foreground=colors[1],
                    padding=-2,
                    fontsize=45
                    ),
                #### Weather ####
                widget.OpenWeather(
                    app_key='e45a0f07f0c675b273ef8636663941db',
                    cityid='3520914',
                    background=colors[1],
                    foreground=colors[0],
                    format='{main_temp}°{units_temperature} {humidity}% {weather_details}',
                    metric=True,
                    update_interval=600
                    ),
                #### RAM ####
                widget.TextBox(
                    text="◢",
                    background=colors[1],
                    foreground=colors[2],
                    padding=-2,
                    fontsize=45
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    background=colors[2],
                    foreground=colors[0],
                    fontshadow=colors[7],
                    text=""
                    ),
                widget.Memory(
                    format='{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
                    foreground=colors[0],
                    background=colors[2],
                    padding=5
                    ),
                #### CPU ####
                widget.TextBox(
                    text="◢",
                    background=colors[2],
                    foreground=colors[5],
                    padding=-2,
                    fontsize=45
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    background=colors[5],
                    foreground=colors[0],
                    text="",
                    fontshadow=colors[7]
                    ),
                widget.CPU(
                    format='{load_percent}%',
                    foreground=colors[0],
                    background=colors[5],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e bash -c ". ~/.zshrc; htop"')},
                    ),
                #### Disk Space ####
                widget.TextBox(
                    text="◢",
                    background=colors[5],
                    foreground=colors[3],
                    padding=-2,
                    fontsize=45
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    background=colors[3],
                    foreground=colors[0],
                    fontshadow=colors[7],
                    text=""
                    ),
                widget.DF(
                    format='{p} ({uf}{m}|{r:.0f}%)',
                    measure='G',
                    Partition='/',
                    update_interval=60,
                    foreground=colors[0],
                    background=colors[3],
                    padding=5,
                    visible_on_warn=False,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e bash -c ". ~/.zshrc; ranger"')},
                    warn_color="ff0000"
                    ),
                #### Thermal Sensors ####
                widget.TextBox(
                    text="◢",
                    background=colors[3],
                    foreground=colors[7],
                    padding=-2,
                    fontsize=45
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    text=" ",
                    background=colors[7],
                    foreground=colors[0],
                    fontshadow=colors[6],
                    ),
                widget.ThermalSensor(
                    background = colors[7],
                    foreground=colors[0],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/opt/bin/fans')},
                    ),
                #### Keyboard Layout ####
                widget.TextBox(
                    text="◢",
                    background=colors[7],
                    foreground=colors[0],
                    padding=-2,
                    fontsize=45
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=17,
                    text="",
                    foreground=colors[7],
                    background=colors[0]
                    ),
                widget.KeyboardLayout(
                    foreground=colors[7],
                    background=colors[0],
                    padding=5,
                    fontshadow=colors[4]
                    ),
                
                #### Caps lock Num Lock Indicator ####
                widget.TextBox(
                    text="◢",
                    background=colors[0],
                    foreground=colors[1],
                    padding=-2,
                    fontsize=45
                    ),
                widget.CapsNumLockIndicator(
                    foreground=colors[0],
                    background=colors[1],
                    padding=5
                    ),
                #### Battery for laptops ####
                widget.TextBox(
                    text="◢",
                    background=colors[1],
                    foreground=colors[0],
                    padding=-2,
                    fontsize=45
                    ),
                #widget.BatteryIcon(
                #    show_short_text=True,
                #    notify_below=30,
                #    discharge_char=' ',
                #    empty_char='',
                #    full_char=' ',
                #    background=colors[0],
                #    foreground=colors[7]
                #    ),
                #widget.Battery(
                #    battery=0,
                #    format='{char} {percent:2.0%} {hour:d}:{min:02d}',
                #    show_short_text=True,
                #    update_interval=60,
                #    background=colors[0],
                #    foreground=colors[7]
                #    ),
                #### Systray ####
                widget.Systray(
                    icon_size=18,
                    background=colors[0],
                    foreground=colors[7]
                    ),
                    ]
    return wid_list_bot

def in_wid_list_sec():
    wid_list_sec = [
                widget.TextBox(
                    font='Font Awesome 5 Free',
                    fontsize=15,
                    foreground=colors[7],
                    text="",mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term)},
                    fontshadow=colors[3]
                    ),
                ]
    return wid_list_sec

#### End Widgets ####

##### Mouse/Keyboard #####

def init_mouse():
    return [Drag([mod], "Button1", lazy.window.set_position_floating(),      # Move floating windows
                 start=lazy.window.get_position()),
            Drag([mod], "Button2", lazy.window.set_size_floating(),          # Resize floating windows
                 start=lazy.window.get_size()),
            Click([mod, "shift"], "Button1", lazy.window.bring_to_front())]  # Bring floating window to front

keys = init_keys()
mouse = init_mouse()

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),  # tastyworks exit box
    Match(title='Qalculate!'),  # qalculate-gtk
    Match(wm_class='pavucontrol'),  # volume control
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
    Match(wm_class='lxappearance'),
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='branchdialog'),
    Match(wm_class='pinentry'),
    Match(wm_class='ssh-askpass'),
    Match(wm_class='Obconf')
])

##### End Mouse/Keyboard #####

##### Screens #####

def init_widgets_top():
    widgets_screen_top = init_wid_list_top()
    return widgets_screen_top
def init_widgets_bot():
    widgets_screen_bot = in_wid_list_bot()  
    return widgets_screen_bot
def init_widgets_sec():
    widgets_screen_sec = in_wid_list_sec()
    return widgets_screen_sec
def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_top(),  size=20, background=colors[0]),
        bottom=bar.Bar(widgets=init_widgets_bot(), size=20, background=colors[0])),
        Screen(bottom=bar.Bar(widgets=init_widgets_sec(), size=20, background=colors[0]))
        ]

#### End Screens ####

colors = init_colors()
layout_theme = init_layout_theme()
layouts = init_layouts()
widget_defaults = init_widgets_defaults()
wid_list_top = init_wid_list_top()
wid_list_bot = in_wid_list_bot()
wid_list_sec = in_wid_list_sec()
widgets_screen_top = init_widgets_top()
widgets_screen_bot = init_widgets_bot()
widgets_screen_sec = init_widgets_sec()
screens = init_screens()

#wmname = "LG3D"
wmname = "qtile"
