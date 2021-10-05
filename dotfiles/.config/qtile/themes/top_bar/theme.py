# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
from funct import *

current_theme='top_bar'

##### Groups #####
group_names = ["1","2","3","4","5","6","7","8","9"]
group_labels=["","","","","","","","",""]
group_layouts=["monadtall", "monadtall", "monadtall","monadtall", "monadtall", "monadtall","monadtall", "monadtall", "monadtall"]
group_matches=[
    [Match(wm_class=['gnome-disks','Gnome-disks','anydesk','Anydesk'])],
    [Match(wm_class=['Zoom','zoom', 'Thunderbird', 'thunderbird','transmission-gtk','Transmission-gtk', 'Simplenote',])],
    [Match(wm_class=['whatsdesk','telegram-desktop-bin', 'TelegramDesktop', 'Discord', 'discord'])],
    [Match(wm_class=['firefox', 'google-chrome', 'Google-chrome'])],
    [Match(wm_class=['Code', 'code','Filezilla','typora'])],
    [Match(wm_class=['Gimp-2.10','Inkscape','Evince', 'libreoffice','Com.github.phase1geo.minder', 'libreoffice-writer', 'libreoffice-calc', 'libreoffice-impress', 'libreoffice-draw', 'libreoffice-calc'])],
    [Match(wm_class=['Spotify', 'spotify'])],
    [Match(wm_class=['VirtualBox Manager', 'VirtualBox Machine', 'Steam', 'steam'])],
    None
]
groups = []

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
            "margin":10,
            "border_width":3,
            "border_normal":color[0],
            "border_focus":color[6],
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
        layout.Floating(
            **layout_theme)
            ]


floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
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


#### Widgets ####
def init_widgets_defaults():
    return dict(font="Fira Code Medium",fontsize=15,padding=2,background=color[0])

def init_widgets_top():    
    widgets_top = [
                #### Shortcuts ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=16,
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show drun')},
                    background=color[4],
                    foreground=color[0],
                    padding=5
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_spawn('rofi  -theme "~/.config/rofi/left_toolbar.rasi" -show find -modi "find:~/.config/rofi/finder.sh"')}
                    ),        
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term)}
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("thunar")}
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(set_rand_wallpaper)},
                ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(change_color_scheme)},
                ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_function(shortcuts)}
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.current_window.kill()},
                    desc="Close Window"
                    ),
                widget.Prompt(
                       prompt=prompt,
                       padding=10,
                       foreground=color[0],
                       background=color[3]
                       ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,text="",
                    padding=5,
                    foreground=color[0],
                    background=color[4],
                    ),
                widget.Mpris2(
                    name='ncspot',
                    objname='org.mpris.MediaPlayer2.ncspot',
                    scroll_chars=30,
                    background=color[4],
                    foreground=color[0],
                    stop_pause_text='',
                    display_metadata=['xesam:title', 'xesam:artist', 'xesam:album'],
                    ),
                widget.Mpris2(
                    name='Spotify',
                    objname='org.mpris.MediaPlayer2.spotify',
                    scroll_chars=30,
                    background=color[4],
                    foreground=color[0],
                    stop_pause_text='',
                    display_metadata=['xesam:title', 'xesam:artist', 'xesam:album'],
                    ),
                widget.TextBox(
                    background=color[4],
                    foreground=color[0],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(prev)},
                    ),
                widget.TextBox(
                    background=color[4],
                    foreground=color[0],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(play_pause)},
                    ),
                widget.TextBox(
                    background=color[4],
                    foreground=color[0],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(nexts)},
                    ),
                widget.Spacer(
                    length=bar.STRETCH,
                    background=color[0],
                    foreground=color[0]
                    ), 
                #### Groups ####
                widget.GroupBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    disable_drag=True,
                    center_aligned=True,
                    padding=5,
                    active=color[0],
                    inactive=color[7],
                    rounded=False,
                    this_current_screen_border=color[2],
                    this_screen_border=color[2],
                    other_current_screen_border=color[2],
                    other_screen_border=color[2],
                    block_highlight_text_color= color[0],
                    highlight_method="block",
                    foreground=color[8],
                    background=color[4]
                    ),
                widget.Spacer(
                    length=bar.STRETCH,
                    background=color[0],
                    foreground=color[0]
                    ),
                widget.Net(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    interface=wifi,
                    format=wifi_icon,
                    foreground=color[0],
                    background=color[4],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_function(network_widget)}
                    ),
                widget.Wlan(
                    interface=wifi,
                    format=' {essid} {percent:2.0%} ',
                    disconnected_message='Unplugged',
                    foreground=color[0],
                    background=color[4],
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                    ),
                widget.Net(
                    interface=wifi,
                    format=' {down}',
                    foreground=color[0],
                    background=color[4],
                    use_bits=True,
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                    ),
                widget.Sep(
                    width=10,
                    foreground=color[0],
                    background=color[0]
                ),
                widget.WidgetBox(
                    text_closed='  ',
                    text_open='',
                    background=color[6],
                    foreground=color[0],
                    widgets=[widget.OpenWeather(
                        app_key='e45a0f07f0c675b273ef8636663941db',
                        cityid='3520914',
                        background=color[6],
                        foreground=color[0],
                        format=' {main_temp}°{units_temperature} {weather_details}',
                        metric=True,
                        update_interval=600
                        ),
                    widget.Sep(
                    width=10
                    ),
                ]),
                widget.Sep(
                    width=10,
                    foreground=color[0],
                    background=color[0]
                ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    text=" ",
                    background=color[2],
                    foreground=color[0]
                    ),
                widget.ThermalSensor(
                    background = color[2],
                    foreground=color[0],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/usr/local/bin/fans')},
                    ),
                widget.Sep(
                    width=10,
                    foreground=color[0],
                    background=color[0]
                ),
                widget.CheckUpdates(
                    update_interval=300,
                    distro='Arch_paru',
                    foreground=color[0],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e paru -Syyu')},
                    display_format="{updates} up",
                    background=color[8],
                    colour_have_updates=color[0],
                    colour_no_updates=color[0],
                    no_update_string="",
                    restart_indicator=""
                    ),
                widget.Sep(
                    width=10,
                    foreground=color[0],
                    background=color[0]
                ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    text=" ",
                    foreground=color[0],
                    background=color[3],
                    padding=0,
                    fontsize=15,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol')}
                    ),
                widget.Volume(
                    channel='Master',
                    background=color[3],
                    foreground=color[0]
                    ),
                widget.Sep(
                    width=10,
                    foreground=color[0],
                    background=color[0]
                ),
                widget.Clock(
                    foreground=color[0],
                    background=color[6],
                    format="%b %a %d %H:%M",
                    update_interval=1,
                    padding=5,
                    padding_y=15
                    ),
                widget.Sep(
                    width=10,
                    foreground=color[0],
                    background=color[0]
                ),
                widget.Systray(
                    icon_size=18,
                    background=color[0],
                    foreground=color[7]
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=16,
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_function(session_widget)},
                    background=color[4],
                    foreground=color[0],
                    padding=5
                    ),

    ]
    return widgets_top

#### End Widgets ####

##### Screens #####

def init_widgets_screen_top():
    widgets_screen_top = init_widgets_top()
    return widgets_screen_top

def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen_top(),  
                size=25,
                background=color[0],
                )),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen_top(),  
                size=25,
                background=color[0],
                ))
        ]

#### End Screens ####

widget_defaults = init_widgets_defaults()
widgets_top = init_widgets_top()
widgets_screen_top = init_widgets_screen_top()
screens = init_screens()
