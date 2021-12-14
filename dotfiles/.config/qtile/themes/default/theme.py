# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
from funct import *

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
            sections = ["QTabs"],
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

#### Widgets ####
def init_widgets_defaults():
    return dict(font="Fira Code Medium",fontsize=14,padding=2,background=color[0])

def init_widgets_top():
    widgets_top = [
                widget.TextBox(
                    foreground=color[2],
                    text="◢",
                    fontsize=65,
                    padding=-2
                    ),
                #### Groups ####
                widget.GroupBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=14,
                    disable_drag=True,
                    hide_unused=False,
                    padding_x=6,
                    padding_y=5,
                    borderwidth=0,
                    active=color[7],
                    inactive=color[0],
                    rounded=False,
                    highlight_color=color[7],
                    highlight_method="block",
                    this_current_screen_border=color[0],
                    this_screen_border=color[0],
                    other_current_screen_border=color[0],
                    other_screen_border=color[0],
                    block_highlight_text_color=color[7],
                    foreground=color[2],
                    background=color[2],
                    urgent_border=color[4]
                    ),
                widget.Prompt(
                       prompt=prompt,
                       padding=10,
                       foreground=color[0],
                       background=color[2]
                       ),
                widget.TextBox(
                    background=color[0],
                    foreground=color[2],
                    text="◤",
                    fontsize=65,
                    padding=-2
                    ),
                widget.WindowName(
                    foreground=color[7],
                    background=color[0],
                    padding=5,
                    format=' {name}',
                    empty_group_string=ver,
                    ),
                #### Spotify ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,text="",
                    padding=5,
                    foreground=color[1],
                    background=color[0],
                    mouse_callbacks={'Button1':lambda: qtile.cmd_spawn(term + ' -e vis')},
                    ),
                widget.Mpris2(
                    name='ncspot',
                    objname='org.mpris.MediaPlayer2.ncspot',
                    scroll_chars=30,
                    background=color[0],
                    foreground=color[5],
                    stop_pause_text='',
                    display_metadata=['xesam:title', 'xesam:artist', 'xesam:album'],
                    ),
                widget.Mpris2(
                    name='Spotify',
                    objname='org.mpris.MediaPlayer2.spotify',
                    scroll_chars=30,
                    background=color[0],
                    foreground=color[5],
                    stop_pause_text='',
                    display_metadata=['xesam:title', 'xesam:artist', 'xesam:album'],
                    ),
                widget.Mpris2(
                    name='vlc',
                    objname='org.mpris.MediaPlayer2.vlc',
                    scroll_chars=30,
                    background=color[0],
                    foreground=color[5],
                    stop_pause_text='',
                    display_metadata=['xesam:title'],
                    scroll_interval=1,
                    scroll_wait_interval=200
                    ),
                widget.TextBox(
                    background=color[0],
                    foreground=color[1],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(prev)},
                    ),
                widget.TextBox(
                    background=color[0],
                    foreground=color[1],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(play_pause)},
                    ),
                widget.TextBox(
                    background=color[0],
                    foreground=color[1],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(nexts)},
                    ),           
                #### Layouts ####
                widget.TextBox(
                    text="◢",
                    background=color[0],
                    foreground=color[1],
                    padding=-2,
                    fontsize=65
                    ),
                widget.TextBox(
                    text='  ',
                    background=color[1],
                    foreground=color[0],
                ),
                widget.CurrentLayout(
                    background=color[1],
                    foreground=color[0]
                    ),
                #### Pomodoro ####
                widget.TextBox(
                    text='◢',
                    background=color[1],
                    foreground=color[5],
                    padding=-2,
                    fontsize=65
                    ),
                widget.WidgetBox(
                    text_closed='',
                    text_open='  ',
                    background=color[5],
                    foreground=color[0],
                    widgets=[widget.Pomodoro(
                        background=color[5],
                        foreground=color[0],
                        color_active=color[0],
                        color_break=color[2],
                        color_inactive=color[0],
                        length_pomodori=50,
                        length_short_break=5,
                        length_long_break=15,
                        num_pomodori=3,
                        prefix_break=' Break',
                        prefix_inactive=' Pomodoro',
                        prefix_long_break=' Long Break',
                        prefix_paused=' '
                    )],
                ),
                #### Updates ####
                widget.TextBox(
                    text='◢',
                    background=color[5],
                    foreground=color[4],
                    padding=-2,
                    fontsize=65
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    background=color[4],
                    foreground=color[0],
                    text="  ",
                    ),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro='Arch_paru',
                    foreground=color[0],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e paru -Syyu')},
                    display_format="{updates} up",
                    background=color[4],
                    colour_have_updates=color[0],
                    colour_no_updates=color[0],
                    no_update_string="",
                    restart_indicator=""
                    ),
                widget.TextBox(
                    text='◢',
                    background=color[4],
                    foreground=color[6],
                    padding=-2,
                    fontsize=65
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    text=" ",
                    foreground=color[0],
                    background=color[6],
                    padding=0,
                    fontsize=15,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol')}
                    ),
                widget.Volume(
                    channel='Master',
                    background=color[6],
                    foreground=color[0]
                    ),
                #### Date Clock Session Control ####
                widget.TextBox(
                    text='◢',
                    background=color[6],
                    foreground=color[0],
                    padding=-2,
                    fontsize=65
                    ),
                widget.Clock(
                    foreground=color[7],
                    background=color[0],
                    format="%b %a %d %H:%M",
                    update_interval=1
                    ),
                #### Lock, Logout, Poweroff ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[1],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_function(session_widget)}
                    ),
                widget.Sep(
                    foreground=color[0],
                ),
    ]
    return widgets_top

def init_widgets_bott():
    
    widgets_bott = [
                #### Shortcuts ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=16,
                    text="",
                    padding=5,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show drun')},
                    background=color[7],
                    foreground=color[0]
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[1],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_spawn('rofi  -theme "~/.config/rofi/left_toolbar.rasi" -show find -modi find:/usr/local/bin/finder')}
                    ),        
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[2],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term)}
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[3],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("thunar")}
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[4],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(set_rand_wallpaper)},
                ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[5],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(change_color_scheme)},
                ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[6],
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
                #### Spacer ####
                widget.Spacer(
                    length=bar.STRETCH,
                    background=color[0],
                    foreground=color[0]
                    ),   
                #### Network ####
                widget.WidgetBox(
                    text_closed=wifi_icon,
                    text_open='  ',
                    background=color[0],
                    foreground=color[5],
                    widgets=[widget.TextBox(
                        text=' '+private_ip,
                        background=color[0],
                        foreground=color[5],
                        mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                        ),
                        widget.TextBox(
                        text='   '+public_ip,
                        background=color[0],
                        foreground=color[5],
                        mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                        ),]
                ),
                widget.Wlan(
                    interface=wifi,
                    format=' {essid} {percent:2.0%} ',
                    disconnected_message='Unplugged',
                    foreground=color[5],
                    background=color[0],
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                    ),
                widget.Net(
                    interface=wifi,
                    format=' {down}',
                    foreground=color[5],
                    background=color[0],
                    use_bits=True,
                    mouse_callbacks={'Button1':lambda: qtile.cmd_function(network_widget)}
                    ),
                widget.TextBox(
                    text="◢",
                    background=color[0],
                    foreground=color[1],
                    padding=-2,
                    fontsize=65
                    ),
                #### Weather ####
                widget.WidgetBox(
                    text_closed='  ',
                    text_open='  ',
                    background=color[1],
                    foreground=color[0],
                    widgets=[widget.OpenWeather(
                        app_key='e45a0f07f0c675b273ef8636663941db',
                        cityid='3520914',
                        background=color[1],
                        foreground=color[0],
                        format='{main_temp}°{units_temperature} {humidity}% {weather_details}',
                        metric=True,
                        update_interval=600
                        )]
                ),
                #### RAM ####
                widget.TextBox(
                    text="◢",
                    background=color[1],
                    foreground=color[2],
                    padding=-2,
                    fontsize=65
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    background=color[2],
                    foreground=color[0],
                    text=""
                    ),
                widget.Memory(
                    format='{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
                    foreground=color[0],
                    background=color[2],
                    padding=5
                    ),
                #### CPU ####
                widget.TextBox(
                    text="◢",
                    background=color[2],
                    foreground=color[5],
                    padding=-2,
                    fontsize=65
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    background=color[5],
                    foreground=color[0],
                    text=""
                    ),
                widget.CPU(
                    format='{load_percent}%',
                    foreground=color[0],
                    background=color[5],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e htop')},
                    ),
                #### Disk Space ####
                widget.TextBox(
                    text="◢",
                    background=color[5],
                    foreground=color[3],
                    padding=-2,
                    fontsize=65
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    background=color[3],
                    foreground=color[0],
                    text=""
                    ),
                widget.DF(
                    format='{p} ({uf}{m}|{r:.0f}%)',
                    measure='G',
                    Partition='/',
                    update_interval=60,
                    foreground=color[0],
                    background=color[3],
                    padding=5,
                    visible_on_warn=False,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e ranger')},
                    warn_color="ff0000"
                    ),
                #### Thermal Sensors ####
                widget.TextBox(
                    text="◢",
                    background=color[3],
                    foreground=color[7],
                    padding=-2,
                    fontsize=65
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    text=" ",
                    background=color[7],
                    foreground=color[0]
                    ),
                widget.ThermalSensor(
                    background = color[7],
                    foreground=color[0],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/usr/local/bin/fans')},
                    ),
                #### Keyboard Layout ####
                widget.TextBox(
                    text="◢",
                    background=color[7],
                    foreground=color[0],
                    padding=-2,
                    fontsize=65
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=17,
                    text="",
                    foreground=color[7],
                    background=color[0]
                    ),
                widget.KeyboardLayout(
                    foreground=color[7],
                    background=color[0],
                    padding=5
                    ),
                
                #### Caps lock Num Lock Indicator ####
                widget.TextBox(
                    text="◢",
                    background=color[0],
                    foreground=color[1],
                    padding=-2,
                    fontsize=65
                    ),
                widget.WidgetBox(
                    text_closed=' ',
                    text_open='  ',
                    background=color[1],
                    foreground=color[0],
                    widgets=[widget.CapsNumLockIndicator(
                        foreground=color[0],
                        background=color[1],
                        padding=5
                        )]
                ),
                #### Battery for laptops ####
                widget.TextBox(
                    text="◢",
                    background=color[1],
                    foreground=color[0],
                    padding=-2,
                    fontsize=65
                    ),
                #### Systray ####
                widget.Systray(
                    icon_size=18,
                    background=color[0],
                    foreground=color[7]
                    ),
                    ]
    return widgets_bott

#### End Widgets ####

##### Screens #####

def init_widgets_screen_top():
    widgets_screen_top = init_widgets_top()
    return widgets_screen_top
def init_widgets_screen_bot():
    widgets_screen_bot = init_widgets_bott()  
    return widgets_screen_bot

def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen_top(),  
                size=25,
                background=color[0],
                ),
            bottom=bar.Bar(widgets=init_widgets_screen_bot(), size=25, background=color[0])),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen_top(),  
                size=25,
                background=color[0],
                ),
            bottom=bar.Bar(widgets=init_widgets_screen_bot(), size=25, background=color[0])
        )
        ]

#### End Screens ####

widget_defaults = init_widgets_defaults()
widgets_top = init_widgets_top()
widgets_screen_top = init_widgets_screen_top()
screens = init_screens()
widgets_bott = init_widgets_bott()
widgets_screen_top = init_widgets_screen_top()
init_widgets_screen_bot = init_widgets_screen_bot()
