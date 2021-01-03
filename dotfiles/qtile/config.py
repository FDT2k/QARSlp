# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
 
import os, re
from libqtile.config import Key,Group, Match, Drag, Click, Rule
from libqtile.command import lazy
from hooks import *
from theme import *

home = os.path.expanduser('~')

##### Window Functions / Funciones de las ventanas #####

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

#### Shortcuts  ####

def init_keys():
    keys = [           
            Key([mod], "q",lazy.window.kill()), # Kill Window / Cerrar ventana
            Key([mod, "shift"], "r",lazy.restart()), # Restart Qtile / Reiniciar Qtile
            Key([mod, "shift"], "q",lazy.shutdown()), # Logout / Cerrar sesión
            Key([mod], "Escape", lazy.function(xk)), # Select window with mouse to kill / Cerrar ventana con el raton
            Key([mod], "h",lazy.function(scuts)),
            Key([mod], "r",lazy.spawn('/opt/bin/qback')),
            Key([mod], "w",lazy.spawn('/opt/bin/genwal')),

            ####  ####
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
            Key([], "Print", lazy.spawn('screenshot')),

            ##### GROUPS (DESKTOPS) #####

            ## Group 1 (Tools, )
            Key([mod], "Return", lazy.function(urx)),
            Key([mod],"e",lazy.function(rangercli)),
            Key([mod],"x",lazy.spawn(lock)),
            Key([mod, "shift"],"a",lazy.function(app_or_group("1", "anydesk"))),
             Key([mod, "shift"],"s",lazy.function(app_or_group('1', 'simplenote'))),

            ## Group 2 (Organization)
            Key([mod],"m",lazy.function(app_or_group('2', 'mailspring'))),
           

            ## Group 2 (Social: Whatsapp, Telegram, )
            Key([mod, "shift"],"w",lazy.function(app_or_group('3', 'whatsdesk'))),
            Key([mod, "shift"],"t",lazy.function(app_or_group('3', 'telegram-desktop'))),
            Key([mod, "shift"],"d",lazy.function(app_or_group('3', 'discord'))),


            ## Group 3 (WEB: Firefox)(Admin: Mail, notes, social)
            Key([mod, "shift"],"f",lazy.function(app_or_group('4', 'firefox'))),
            Key([mod],"f",lazy.spawn('/opt/bin/wsearch')),

            ## Group 4 (Code/Write/Office: visual studio, typora, onlyofice)
            Key([mod],"o",lazy.function(app_or_group("6", 'libreoffice'))),
            Key([mod],"c",lazy.function(app_or_group('5', 'code'))),

            ## Group 5 (Design: Gimp, Inkscape, feh)
            Key([mod],"g",lazy.function(app_or_group('6', 'gimp'))),
            Key([mod, "shift"],"m",lazy.function(app_or_group('6', 'com.github.phase1geo.minder'))),

            ## Group 6 (Virtual Stuff games)
            Key([mod],"v",lazy.function(app_or_group('8', 'virtualbox'))),
            Key([mod],"b",lazy.function(app_or_group('8', '/home/gibranlp/albiononline/./Albion-Online'))),

            ## Group 7 (Música)
            Key([mod],"s",lazy.function(ncsp)),

            ### Dmenu Run Launcher
            Key([mod], "d",lazy.spawn("rofi -theme '~/.config/rofi/launcher.rasi' -show drun")),]

    for i in groups:
            keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))
            keys.append(Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)))
    return keys

##### GROUPS #####

groups = [
    Group("1",position=1,matches=[Match(wm_class=['thunar', 'Thunar', 'gnome-disks', 'Gnome-disks', 'anydesk', 'Simplenote', 'Anydesk'])],layout="matrix",label=""),
    Group("2",position=2,matches=[Match(wm_class=['Zoom','zoom', 'Mailspring', 'mailspring', 'transmission-gtk','Transmission-gtk'])],layout="monadtall",label=""),
    Group("3",position=3,matches=[Match(wm_class=['whatsdesk','telegram-desktop-bin', 'TelegramDesktop', 'Discord', 'discord'])],layout="monadtall",label=""),
    Group("4",position=4,matches=[Match(wm_class=['firefox'])],layout="monadtall",label=""),
    Group("5",position=5,matches=[Match(wm_class=['Code', 'code','Filezilla'])],layout="monadtall",label=""),
    Group("6",position=6,matches=[Match(wm_class=['Gimp-2.10','Inkscape','Evince', 'libreoffice','Com.github.phase1geo.minder'])],layout="monadtall",label=""),
    Group("7",position=7,layout="monadtall",label=""),
    Group("8",position=8,matches=[Match(wm_class=['VirtualBox Manager', 'VirtualBox Machine', 'Albion Online Launcher'])],layout="monadtall",label=""),
    Group("9",position=9,layout="monadtall",label="")]




##### FLOATING WINDOWS #####

def init_mouse():
    return [Drag([mod], "Button1", lazy.window.set_position_floating(),      # Move floating windows
                 start=lazy.window.get_position()),
            Drag([mod], "Button2", lazy.window.set_size_floating(),          # Resize floating windows
                 start=lazy.window.get_size()),
            Click([mod, "shift"], "Button1", lazy.window.bring_to_front())]  # Bring floating window to front

##### DEFINING A FEW THINGS #####

if __name__ in ["config", "__main__"]:
    mod = "mod4"
    alt = "mod1"                                   
    myTerm = "urxvt"                                    

    
    keys = init_keys()
    mouse = init_mouse()



#wmname = "LG3D"
wmname = "qtile"
