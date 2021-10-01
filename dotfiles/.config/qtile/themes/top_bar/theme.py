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
            "single_margin":10,
            "single_border_width":3,
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
                    foreground=color[0],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('rofi -theme "~/.config/rofi/"' + current_theme + '"/launcher.rasi" -show drun')},
                    fontshadow=color[3],
                    background=color[6],
                    padding=5
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[4],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/usr/local/bin/shortc')}
                    ),
                widget.Sep(
                    width=10
                ),
                #### Groups ####
                widget.GroupBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    disable_drag=True,
                    fontshadow=color[0],
                    center_aligned=True,
                    padding=5,
                    active=color[4],
                    inactive=color[2],
                    rounded=False,
                    this_current_screen_border=color[2],
                    this_screen_border=color[2],
                    other_current_screen_border=color[2],
                    other_screen_border=color[2],
                    block_highlight_text_color= color[4],
                    highlight_method="block",
                    foreground=color[7],
                    background=color[0]
                    ),
                widget.Sep(
                    width=10
                ),
                widget.Prompt(
                       prompt=prompt,
                       padding=10,
                       foreground=color[0],
                       background=color[2]
                       ),
                widget.Sep(
                    width=10
                ),
                widget.WindowName(
                    foreground=color[4],
                    background=color[0],
                    padding=5,
                    format=' {name}',
                    empty_group_string=' QARSlp',
                    ),
                widget.Systray(
                    icon_size=18,
                    background=color[0],
                    foreground=color[7]
                    ),
                widget.Sep(
                    width=10
                ),
                widget.Mpris2(
                    name='ncspot',
                    objname='org.mpris.MediaPlayer2.ncspot',
                    scroll_chars=30,
                    background=color[0],
                    foreground=color[6],
                    stop_pause_text='',
                    max_chars=50,
                    display_metadata=['xesam:title', 'xesam:artist', 'xesam:album'],
                    ),
                widget.Mpris2(
                    name='Spotify',
                    objname='org.mpris.MediaPlayer2.spotify',
                    scroll_chars=30,
                    background=color[6],
                    foreground=color[0],
                    stop_pause_text='',
                    max_chars=50,
                    display_metadata=['xesam:title', 'xesam:artist', 'xesam:album'],
                    ),
                widget.Sep(
                    width=10
                    ),
                widget.Wlan(
                    interface=netact,
                    format='{essid} {percent:2.0%} ',
                    disconnected_message='Unplugged',
                    foreground=color[6],
                    background=color[0],
                    mouse_callbacks={'Button1':wnetw}
                    ),
                widget.Net(
                    interface=netact,
                    format='{down}',
                    foreground=color[6],
                    background=color[0],
                    use_bits=True,
                    mouse_callbacks={'Button1':wnetw}
                    ),
                widget.Sep(
                    width=10
                    ),
                widget.WidgetBox(
                    text_closed='',
                    text_open='',
                    foreground=color[6],
                    widgets=[widget.OpenWeather(
                        app_key='e45a0f07f0c675b273ef8636663941db',
                        cityid='3520914',
                        background=color[0],
                        foreground=color[6],
                        format=' {main_temp}°{units_temperature} {weather_details}',
                        metric=True,
                        update_interval=600
                        ),
                    widget.Sep(
                    width=10
                    ),
                ]),
                widget.Sep(
                    width=10
                    ),
                 widget.DF(
                    format='{uf}{m}',
                    measure='G',
                    Partition='/',
                    update_interval=1800,
                    foreground=color[6],
                    background=color[0],
                    padding=5,
                    visible_on_warn=False,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e ranger"')},
                    warn_color="ff0000"
                    ),
                widget.Sep(
                    width=10
                    ),
                widget.CheckUpdates(
                    update_interval=300,
                    distro='Arch_paru',
                    foreground=color[0],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e paru -Syyu')},
                    display_format="up",
                    background=color[0],
                    colour_have_updates=color[6],
                    colour_no_updates=color[6],
                    no_update_string="",
                    restart_indicator=""
                    ),
                widget.Sep(
                    width=10
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    text=" ",
                    foreground=color[6],
                    background=color[0],
                    padding=0,
                    fontsize=15,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol')}
                    ),
                widget.Volume(
                    channel='Master',
                    background=color[0],
                    foreground=color[6]
                    ),
                widget.Sep(
                    width=10
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
                    width=10
                    ),
                #### Lock, Logout, Poweroff ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1': wsess},
                    fontshadow=color[3]
                    ),
                widget.Sep(
                    foreground=color[0],
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
                margin=10,
                background=color[0],
                )),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen_top(),  
                size=25,
                margin=10,
                background=color[0],
                ))
        ]

#### End Screens ####

widget_defaults = init_widgets_defaults()
widgets_top = init_widgets_top()
widgets_screen_top = init_widgets_screen_top()
screens = init_screens()
