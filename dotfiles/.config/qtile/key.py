# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
from theme import *

#### Layouts ####
def init_layout_theme():
    return {"font":"Fira Code Medium",
            "fontsize":14,
            "margin": 10,
            "border_width":3,
            "border_normal":color[0],
            "border_focus":color[6],
            "single_margin":0,
            "single_border_width":0,
           }

def init_layouts():
    return [
        layout.Matrix(
            **layout_theme),
        layout.MonadTall(
            max_ratio=0.90,
            ratio=0.70,
            **layout_theme),
        layout.TreeTab(
            sections = ["Tabs"],
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
            panel_width = 200,
            **layout_theme),
        layout.Floating(
            **layout_theme)
            ]


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
#### End layouts ####

#### Keys ####
def init_keys():
    keys = [ 
            #### Basics ####          
            Key([mod], "Return", lazy.spawn(term)), # Open Terminal
            Key([mod, "shift"], "Return", lazy.spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show drun')),
            Key([mod, "mod1"], "Return", lazy.spawn('sudo rofi -theme "~/.config/rofi/launcher.rasi" -show drun')),
            Key([alt], "Return", lazy.spawn('rofi  -theme "~/.config/rofi/finder.rasi" -show "find -modi find:~/.config/rofi/finder.sh"')),
            Key([mod], "q",lazy.window.kill()), # Close Window 
            Key([mod, "shift"], "r",lazy.restart()), # Restart Qtile
            Key([mod, "shift"], "q",lazy.shutdown()), # Logout 
            Key([mod], "Escape", lazy.spawn('xkill')), # Click window to close
            
            #### Widgets ####
            Key([mod],"h",lazy.spawn('/opt/bin/shortc')), # Sortcurts widget
            Key([mod],"p",lazy.spawn('/opt/bin/qback')), # Launcher
            Key([mod],"f",lazy.function(ksearx)), # WEB Search
            Key([mod],"x",lazy.spawn('/opt/bin/logout')), # Log out
            Key([mod],"n",lazy.spawn('/opt/bin/network')), # Network Settings
            Key([alt],"r",lazy.spawn('/opt/bin/qback')), # Change Color Scheme
            Key([mod],"c",lazy.spawn('/opt/bin/fans')), # Fans
            Key([alt],"w",lazy.spawn('/opt/bin/chgth')), # Change Theme 

            #### Add Screen ####
            Key([mod, "shift"],"y",lazy.spawn(term + ' -e xrandr --output HDMI1 --auto --left-of eDP1')),
            #### Theming ####
            Key([mod], "r",lazy.function(set_wallpaper)), # Set randwom wallpaper / colors to entire system

            #### Apps ####
            Key([mod, "shift"],"e",lazy.function(app_or_group("1", "nautilus"))), #File manager
            Key([alt, "shift"],"e",lazy.function(ranger)), # CLI file manager
            Key([mod, "shift"],"a",lazy.function(app_or_group("1", "anydesk"))),
            Key([mod, "shift"],"s",lazy.function(app_or_group('2', 'simplenote'))),

            ## Group 2 (Organization: Mail)
            Key([mod, "shift"],"m",lazy.function(app_or_group('2', 'thunderbird'))),
            
            ## Group 3 (Social: Whatsapp, Telegram, )
            Key([mod, "shift"],"w",lazy.function(app_or_group('3', 'whatsdesk'))),
            Key([mod, "shift"],"t",lazy.function(app_or_group('3', 'telegram-desktop'))),
            Key([mod, "shift"],"d",lazy.function(app_or_group('3', 'discord'))),

            ## Group 4 (WEB: Firefox)(Admin: Mail, notes, social)
            Key([mod, "shift"],"f",lazy.function(app_or_group('4', 'firefox'))),
            Key([mod, "shift"],"g",lazy.function(app_or_group('4', 'google-chrome-stable'))),
            
            ## Group 5 (Code/Write/Office: visual studio, typora, onlyofice)
            Key([mod, "shift"],"h",lazy.function(app_or_group('5', 'typora'))),
            Key([mod, "shift"],"o",lazy.function(app_or_group("6", 'libreoffice'))),
            Key([mod, "shift"],"c",lazy.function(app_or_group('5', 'code'))),

            ## Group 6 (Design: Gimp, Inkscape, feh)
            Key([mod],"g",lazy.function(app_or_group('6', 'gimp'))),

            ## Group 7 (Music: Ncsp, Spotify)
            Key([alt, "shift"],"s",lazy.function(ncsp)),

            ## Group 8 (Virtual Stuff games)
            Key([mod, "shift"],"v",lazy.spawn(term + ' -e vis')),
            Key([mod],"b",lazy.function(app_or_group('8', '/home/gibranlp/albiononline/./Albion-Online'))),
            
            #### Layouts ####
            Key([mod], "Tab",lazy.layout.next()), # Change focus of windows down
            Key([mod, "shift"], "Tab",lazy.layout.up()), # Change focus of windows up
            Key([alt], "Tab", lazy.layout.swap_left()),
            Key([alt, "shift"], "Tab", lazy.layout.swap_right()),
            #Key([mod], "h", lazy.layout.left()),
            #Key([mod], "l", lazy.layout.right()),
            #Key([mod], "Up", lazy.layout.down()),
            #Key([mod], "Down", lazy.layout.up()),

            #### Brightness ####
            Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
            Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

            #### Volume ####
            Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
            Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
            Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

            #### Media Control ####
            #Key([mod], "v", lazy.spawn('/home/gibranlp/MEGA/computerStuff/keyboard/keyboard_activate.sh')),
            #Key([mod], "b", lazy.spawn('/home/gibranlp/MEGA/computerStuff/keyboard/keyboard_deactivate.sh')),
            Key([], "XF86AudioPlay", lazy.spawn("playerctl -p ncspot play-pause")),
            Key([], "XF86AudioNext", lazy.spawn("playerctl -p ncspot next")),
            Key([], "XF86AudioPrev", lazy.spawn("playerctl -p ncspot previous")),
            Key([], "XF86AudioStop", lazy.spawn("playerctl -p ncspot stop")),

            #### Window hotkeys ####
            Key([alt], "f", lazy.window.toggle_fullscreen()),
            Key([alt, "shift"], "f", lazy.window.toggle_floating()),
            Key([mod], "space", lazy.next_layout()),

            #### Resize windows ####
            Key([mod, "shift"], "Up", lazy.layout.grow()),
            Key([mod, "shift"], "Down", lazy.layout.shrink()),
            Key([mod, "shift"], "space", lazy.layout.flip()),

            ##### Change focus ####
            Key([mod], "Up", lazy.layout.up()),
            Key([mod], "Down", lazy.layout.down()),
            Key([mod], "Left", lazy.layout.left()),
            Key([mod], "Right", lazy.layout.right()),

            ### Screenshots ####
            Key([], "Print", lazy.spawn('/opt/bin/screenshot')),]


    for i in groups:
            keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))
            keys.append(Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)))
    return keys
#### End Keys ####

##### Mouse/Keyboard #####

def init_mouse():
    return [Drag([mod], "Button1", lazy.window.set_position_floating(),      # Move floating windows
                 start=lazy.window.get_position()),
            Drag([mod], "Button2", lazy.window.set_size_floating(),          # Resize floating windows
                 start=lazy.window.get_size()),
            Click([mod, "shift"], "Button1", lazy.window.bring_to_front())]  # Bring floating window to front

keys = init_keys()
mouse = init_mouse()
layout_theme = init_layout_theme()
layouts = init_layouts()
