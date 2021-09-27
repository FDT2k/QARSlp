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
group_names=["1","2","3","4","5","6","7","8","9"]
group_labels=["","","","","","","","",""]
group_layouts=["monadtall", "matrix", "matrix","monadtall", "monadtall", "monadtall","monadtall", "matrix", "monadtall"]
group_matches=[
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

groups=[]

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
    return dict(font="Fira Code Medium",fontsize=14,padding=2,background=color[0])

def init_widgets_top():    
    widgets_top=[
                widget.Sep(
                       linewidth=0,
                       padding=6,
                       foreground=color[2],
                       background=color[0]
                       ),
              widget.TextBox(
                       padding_y=5,
                       fontsize=15,
                       text="",
                       mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term)},
                       foreground=color[3],
                       background=color[0]
                       ),
             widget.Sep(
                       linewidth=0,
                       padding=6,
                       foreground=color[2],
                       background=color[0]
                       ),
              widget.GroupBox(
                       font="Font Awesome",
                       fontsize=14,
                       margin_y=3,
                       margin_x=0,
                       padding_y=5,
                       padding_x=3,
                       borderwidth=3,
                       active=color[4],
                       inactive=color[6],
                       rounded=False,
                       highlight_color=color[7],
                       highlight_method="line",
                       this_current_screen_border=color[6],
                       this_screen_border=colors [4],
                       other_current_screen_border=color[6],
                       other_screen_border=color[4],
                       foreground=color[2],
                       background=color[0]
                       ),
              widget.Prompt(
                       prompt=prompt,
                       font="Fira Code",
                       padding=10,
                       foreground=color[6],
                       background=color[0]
                       ),
              widget.Sep(
                       linewidth=0,
                       padding=40,
                       foreground=color[2],
                       background=color[0]
                       ),
              widget.WindowName(
                       foreground=color[6],
                       background=color[0],
                       padding=0
                       ),
              widget.Systray(
                       background=color[0],
                       padding=5
                       ),
              widget.Sep(
                       linewidth=0,
                       padding=6,
                       foreground=color[0],
                       background=color[0]
                       ),
              widget.TextBox(
                       text='',
                       background=color[0],
                       foreground=color[1],
                       padding=-2,
                       fontsize=48
                       ),
             widget.Net(
                       interface="enp34s0",
                       format='{down} ↓↑ {up}',
                       foreground=color[0],
                       background=color[1],
                       padding=5
                       ),
              widget.TextBox(
                       text='',
                       background=color[1],
                       foreground=color[5],
                       padding=-2,
                       fontsize=48
                       ),
              widget.TextBox(
                       text="🌡",
                       padding=2,
                       foreground=color[0],
                       background=color[5],
                       fontsize=13
                       ),
               widget.ThermalSensor(
                        foreground=color[0],
                        background=color[5],
                        threshold=90,
                        padding=5
                        ),
              widget.TextBox(
                       text='',
                       background=color[5],
                       foreground=color[3],
                       padding=-2,
                       fontsize=48
                       ),
              widget.TextBox(
                       text=" ⟳",
                       padding=2,
                       foreground=color[0],
                       background=color[3],
                       fontsize=14
                       ),
              widget.CheckUpdates(
                       update_interval=60,
                       distro='Arch_paru',
                       display_format="{updates} Updates",
                       foreground=color[0],
                       mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e sudo pacman -Syu')},
                       background=color[3]
                       ),
              widget.TextBox(
                       text='',
                       background=color[3],
                       foreground=color[7],
                       padding=-2,
                       fontsize=48
                       ),
              widget.TextBox(
                       text=" ",
                       foreground=color[0],
                       background=color[7],
                       padding=0,
                       fontsize=14
                       ),
              widget.Memory(
                       foreground=color[0],
                       background=color[7],
                       mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e htop')},
                       padding=5
                       ),
              widget.TextBox(
                       text='',
                       background=color[7],
                       foreground=color[2],
                       padding=-2,
                       fontsize=48
                       ),
              widget.TextBox(
                       text=" ₿",
                       padding=0,
                       foreground=color[0],
                       background=color[2],
                       fontsize=12
                       ),
              #widget.BitcoinTicker(
              #         foreground=color[0],
              #         background=color[2],
              #         padding=5
              #         ),
              widget.TextBox(
                       text='',
                       background=color[2],
                       foreground=color[4],
                       padding=-2,
                       fontsize=48
                       ),
              widget.TextBox(
                      text=" Vol:",
                       foreground=color[0],
                       background=color[4],
                       padding=0
                       ),
              widget.Volume(
                       foreground=color[0],
                       background=color[4],
                       padding=5
                       ),
              widget.TextBox(
                       text='',
                       background=color[4],
                       foreground=color[6],
                       padding=-2,
                       fontsize=48
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                       foreground=color[0],
                       background=color[6],
                       padding=0,
                       scale=0.7
                       ),
              widget.CurrentLayout(
                       foreground=color[0],
                       background=color[6],
                       padding=5
                       ),
              widget.TextBox(
                       text='',
                       background=color[6],
                       foreground=color[0],
                       padding=-2,
                       fontsize=48
                       ),
              widget.Clock(
                       foreground=color[6],
                       background=color[0],
                       format="%A, %B %d - %H:%M "
                       ),

    ]
    return widgets_top

#### End Widgets ####

##### Screens #####

def init_widgets_screen_top():
    widgets_screen_top=init_widgets_top()
    return widgets_screen_top

def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen_top(),  size=25, background=color[0])),
        Screen()
        ]

#### End Screens ####

widget_defaults=init_widgets_defaults()
widgets_top=init_widgets_top()
widgets_screen_top=init_widgets_screen_top()
screens=init_screens()