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
group_labels = ["☿","♀","♁","♂","♃","♄","⛢","♆","რ"]
group_layouts = ["monadtall", "matrix", "matrix","monadtall", "monadtall", "monadtall","monadtall", "matrix", "monadtall"]
group_matches = [
    [Match(wm_class=['nautilus','gnome-disks','Gnome-disks','anydesk','Anydesk'])],
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


#### Widgets ####
def init_widgets_defaults():
    return dict(font="Fira Code Medium",fontsize=12,padding=2,background=color[0])

def init_widgets_top():    
    widgets_top = [
                widget.Sep(
                    foreground=color[2],
                ),
                widget.TextBox(
                    fontsize=16,
                    foreground=color[3],
                    text="Ω",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show drun')},
                    ),
                widget.Sep(
                    foreground=color[2],
                ),
                #### Groups ####
                widget.GroupBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=16,
                    disable_drag=True,
                    hide_unused=False,
                    padding_x=1,
                    padding_y=4,
                    borderwidth=2,
                    active=color[6],
                    inactive=color[1],
                    rounded=False,
                    highlight_color=color[7],
                    highlight_method="block",
                    ),
                widget.Sep(
                    foreground=color[2],
                ),
                widget.Prompt(
                       prompt = prompt,
                       font = "Fira Code",
                       padding = 10,
                       foreground = color[6],
                       background = color[0]
                       ),
                widget.Sep(
                    foreground=color[2],
                ),
                widget.WindowName(
                    foreground=color[6],
                    background=color[0],
                    padding=5,
                    format='{name}',
                    empty_group_string='QARSlp',
                    ),
                widget.Spacer(
                    length=3
                    ),
                widget.CPUGraph(
                    graph_color=colors[6],
                    fill_color=colors[0],
                    samples=200,
                    line_width=1,
                    frequency=0.2,
                    margin_x=-149,
                    margin_y=4,
                    border_width=0,
                    width=100,
                    type='linefill',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e htop')},
                    ),
                widget.Spacer(
                    length=3,
                    ),
                widget.HDDBusyGraph(
                    graph_color=colors[6],
                    fill_color=colors[0],
                    samples=200,
                    line_width=1,
                    frequency=0.2,
                    margin_x=-149,
                    margin_y=4,
                    border_width=0,
                    width=100,
                    type='linefill',
                    device='sda',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e ranger')},
                    ),
                widget.Spacer(
                    length=3,
                    ),
                widget.NetGraph(
                    graph_color=colors[6],
                    fill_color=colors[0],
                    samples=200,
                    line_width=1,
                    frequency=0.2,
                    margin_x=-149,
                    margin_y=4,
                    border_width=0,
                    width=100,
                    type='linefill',
                    device='sda',
                    mouse_callbacks={'Button1': wnetw}
                    ),
                widget.Spacer(
                    bar.STRETCH
                    ),
                widget.Systray(
                       background=color[0],
                       padding=5
                       ),
                #### Spotify ####
                widget.Sep(
                    foreground=color[2],
                ),
                widget.Mpris2(
                    name='ncspot',
                    objname='org.mpris.MediaPlayer2.ncspot',
                    scroll_chars=30,
                    background=color[0],
                    foreground=color[6],
                    stop_pause_text='',
                    display_metadata=['xesam:artist','xesam:title'],
                    scroll_interval=0.5,
                    scroll_wait_intervals=2000
                    ),
                widget.Sep(
                    foreground=color[2],
                ),    
                #### Updates ####
                widget.CheckUpdates(
                    update_interval=60,
                    distro='Arch_paru',
                    foreground=color[6],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e paru -Syyu')},
                    display_format="{updates} up",
                    background=color[0],
                    colour_have_updates=color[6],
                    no_update_string="",
                    restart_indicator=""
                    ),
                widget.Sep(
                    foreground=color[2],
                ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    text=" ",
                    foreground=color[6],
                    background=color[0],
                    padding=0,
                    fontsize=15
                    ),
                widget.ThermalSensor(
                    background = color[0],
                    foreground=color[6],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/opt/bin/fans')},
                    ),
                widget.Sep(
                    foreground=color[2],
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    text=" ",
                    foreground=color[6],
                    background=color[0],
                    padding=0,
                    fontsize=15,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
                    ),
                widget.Volume(
                    channel='Master',
                    background=color[0],
                    foreground=color[6]
                    ),
                widget.Sep(
                    foreground=color[2],
                ), 
                #### Date Clock Session Control ####
                widget.Clock(
                    foreground=color[6],
                    background=color[0],
                    format="%b %a %d %H:%M",
                    update_interval=1
                    ),
                widget.Sep(
                    foreground=color[6],
                ),
                #### Lock, Logout, Poweroff ####
                widget.TextBox(
                    foreground=color[3],
                    fontsize=16,
                    text="ⵀ",
                    mouse_callbacks={'Button1': wsess},
                    ),
                widget.Sep(
                    foreground=color[6],
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
