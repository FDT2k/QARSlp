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
groups = [
    Group("1",
    exclusive = True,
    matches=[Match(wm_class=[
        'nautilus','gnome-disks','Gnome-disks','anydesk','Anydesk'])],
    layout="monadtall",
    label=""),
    Group("2",
    matches=[Match(wm_class=[
        'Zoom','zoom', 'Thunderbird', 'thunderbird','transmission-gtk','Transmission-gtk', 'Simplenote',])],
    layout="matrix",
    label=""),
    Group("3",
    matches=[Match(wm_class=[
        'whatsdesk','telegram-desktop-bin', 'TelegramDesktop', 'Discord', 'discord'])],
    layout="matrix",
    label=""),
    Group("4",
    matches=[Match(wm_class=[
        'firefox', 'google-chrome', 'Google-chrome'])],
    layout="monadtall",
    label=""),
    Group("5",
    matches=[Match(wm_class=[
        'Code', 'code','Filezilla','typora'])],
    layout="monadtall",
    label=""),
    Group("6",
    matches=[Match(wm_class=[
        'Gimp-2.10','Inkscape','Evince', 'libreoffice','Com.github.phase1geo.minder', 'libreoffice-writer', 'libreoffice-calc', 'libreoffice-impress', 'libreoffice-draw', 'libreoffice-calc'])],
    layout="monadtall",
    label=""),
    Group("7",
    matches=[Match(wm_class=[
        'Spotify', 'spotify'])],
    layout="monadtall",
    label=""),
    Group("8",
    matches=[Match(wm_class=[
        'VirtualBox Manager', 'VirtualBox Machine', 'Steam', 'steam'])],
    layout="matrix",
    label=""),
    Group("9",
    layout="monadtall",
    label="")]

#### End Groups ####


#### Widgets ####
def init_widgets_defaults():
    return dict(font="Fira Code Medium",fontsize=14,padding=2,background=color[0])

def init_widgets_top():    
    widgets_top = [
                #### Shortcuts ####
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('rofi -theme "~/.config/rofi/launcher.rasi" -show drun')},
                    fontshadow=color[3]
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1':lambda: qtile.cmd_spawn('rofi  -theme "~/.config/rofi/finder.rasi" -show "find -modi find:~/.config/rofi/finder.sh"')},
                    fontshadow=color[3]
                    ),        
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term)},
                    fontshadow=color[3]
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("nautilus")},
                    fontshadow=color[3]
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/opt/bin/genwal')},
                    fontshadow=color[3]
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/opt/bin/shortc')},
                    fontshadow=color[3]
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1': lambda: qtile.current_window.kill()},
                    fontshadow=color[3],
                    desc="Close Window"
                    ),
                widget.TextBox(
                    foreground=color[1],
                    text="◢",
                    fontsize=65,
                    padding=-2
                    ),
                #### Groups ####
                widget.GroupBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    disable_drag=True,
                    hide_unused=False,
                    fontshadow=color[0],
                    margin_y=1,
                    padding_x=5,
                    borderwidth=0,
                    active=color[7],
                    inactive=color[1],
                    rounded=False,
                    highlight_method="text",
                    this_current_screen_border=color[0],
                    this_screen_border=color[3],
                    other_current_screen_border=color[0],
                    other_screen_border=color[0],
                    foreground=color[2],
                    background=color[1]
                    ),
                #### Notification ####
                widget.Prompt(
                    prompt = prompt,
                    foreground=color[0],
                    background = color[1]
                    ),
                widget.TextBox(
                    background=color[0],
                    foreground=color[1],
                    text="◤",
                    fontsize=65,
                    padding=-2
                    ),
                widget.WindowName(
                    foreground=color[7],
                    background=color[0],
                    padding=5,
                    format=' {name}',
                    empty_group_string=' QARSlp',
                    ),
                #### Spacer ####
                #widget.Spacer(
                #    length=bar.STRETCH,
                #    background=color[0],
                #    foreground=color[0]
                #    ),   
                #### Spotify ####
                widget.TextBox(
                    text="◢",
                    background=color[0],
                    foreground=color[6],
                    padding=-2,
                    fontsize=65
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,text="",
                    padding=5,
                    foreground=color[0],
                    background=color[6],
                    fontshadow=color[7],
                    mouse_callbacks={'Button1': ncsp}
                    ),
                widget.Mpris2(
                    name='ncspot',
                    objname='org.mpris.MediaPlayer2.ncspot',
                    scroll_chars=30,
                    background=color[6],
                    foreground=color[0],
                    stop_pause_text='',
                    display_metadata=['xesam:artist','xesam:title'],
                    scroll_interval=0.5,
                    scroll_wait_intervals=2000
                    ),
                    
                #### Layouts ####
                widget.TextBox(
                    text="◢",
                    background=color[6],
                    foreground=color[2],
                    padding=-2,
                    fontsize=65
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    background=color[2],
                    foreground=color[0],
                    fontshadow=color[7],
                    text="  "
                    ),
                widget.CurrentLayout(
                    background=color[2],
                    foreground=color[0]
                    ),

                #### Pomodoro ####
                widget.TextBox(
                    text='◢',
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
                    text=" ",
                    fontshadow=color[7]
                    ),
                widget.Pomodoro(
                    background=color[5],
                    foreground=color[0],
                    color_active=color[0],
                    color_break=color[2],
                    color_inactive=color[0],
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
                    fontshadow=color[7],
                    text="  ",
                    ),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro='Arch_paru',
                    foreground=color[0],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e paru -Syyu')},
                    display_format="{updates} up",
                    background=color[3],
                    colour_have_updates=color[0],
                    colour_no_updates=color[0],
                    no_update_string="",
                    restart_indicator=""
                    ),
                #### Khal Calendar ####
                #widget.KhalCalendar(lookahead=15, remindertime=60, foreground=color[0], background=color[7]),
                #### Sound Control ####
                widget.TextBox(
                    text='◢',
                    background=color[3],
                    foreground=color[7],
                    padding=-2,
                    fontsize=65
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    text=" ",
                    foreground=color[0],
                    background=color[7],
                    padding=0,
                    fontsize=15,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
                    fontshadow=color[3]
                    ),
                widget.Volume(
                    channel='Master',
                    background=color[7],
                    foreground=color[0],
                    fontshadow=color[7]
                    ),
                #widget.Backlight(
                #    background=color[7],
                #    foreground=color[0],
                #    fontshadow=color[7]
                #    ),
                #### Date Clock Session Control ####
                widget.TextBox(
                    text='◢',
                    background=color[7],
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
                    foreground=color[7],
                    text="",
                    mouse_callbacks={'Button1': wsess},
                    fontshadow=color[3]
                    ),
    ]
    return widgets_top

def init_widgets_bott():
    widgets_bott = [
                #widget.DebugInfo(foreground=color[7], background=color[0], fontshadow=color[2]),
                #### Spacer ####
                widget.Spacer(
                    length=bar.STRETCH,
                    background=color[0],
                    foreground=color[0]
                    ),   
                #### Network ####
                widget.TextBox(
                    text='◢',
                    background=color[0],
                    foreground=color[5],
                    padding=-2,
                    fontsize=65
                    ),
                widget.Net(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    interface=netact,
                    format='',
                    foreground=color[0],
                    background=color[5],
                    fontshadow=color[7],
                    mouse_callbacks={'Button1': wnetw}
                    ),
                widget.Wlan(
                    interface=netact,
                    format='{essid} {percent:2.0%} ',
                    disconnected_message='Unplugged',
                    foreground=color[0],
                    background=color[5],
                    mouse_callbacks={'Button1':wnetw}
                    ),
                widget.Net(
                    fontsize=15,
                    interface=netact,
                    format='{down}',
                    foreground=color[0],
                    background=color[5],
                    use_bits=True,
                    mouse_callbacks={'Button1':wnetw}
                    ),
                #### Bitcoin ####
                #widget.TextBox(
                #    text="◢",
                #    background=color[5],
                #    foreground=color[3],
                #    padding=-2,
                #    fontsize=65
                #    ),
                #widget.BitcoinTicker(
                #    background=color[3],
                #    foreground=color[0]
                #    ),
                widget.TextBox(
                    text="◢",
                    background=color[5],
                    foreground=color[1],
                    padding=-2,
                    fontsize=65
                    ),
                #### Weather ####
                widget.OpenWeather(
                    app_key='e45a0f07f0c675b273ef8636663941db',
                    cityid='3520914',
                    background=color[1],
                    foreground=color[0],
                    format='{main_temp}°{units_temperature} {humidity}% {weather_details}',
                    metric=True,
                    update_interval=600
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
                    fontshadow=color[7],
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
                    text="",
                    fontshadow=color[7]
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
                    fontshadow=color[7],
                    text=""
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
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(term + ' -e ranger"')},
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
                    foreground=color[0],
                    fontshadow=color[6],
                    ),
                widget.ThermalSensor(
                    background = color[7],
                    foreground=color[0],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('/opt/bin/fans')},
                    ),
                widget.TextBox(
                    font='Font Awesome 5 Free Solid',
                    fontsize=15,
                    text=" ",
                    background=color[7],
                    foreground=color[0],
                    fontshadow=color[6],
                    ),
                widget.NvidiaSensors(
                    foreground=color[0],
                    background=color[7],
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
                    text="",
                    foreground=color[7],
                    background=color[0]
                    ),
                widget.KeyboardLayout(
                    foreground=color[7],
                    background=color[0],
                    padding=5,
                    fontshadow=color[4]
                    ),
                
                #### Caps lock Num Lock Indicator ####
                widget.TextBox(
                    text="◢",
                    background=color[0],
                    foreground=color[1],
                    padding=-2,
                    fontsize=65
                    ),
                widget.CapsNumLockIndicator(
                    foreground=color[0],
                    background=color[1],
                    padding=5
                    ),
                #### Battery for laptops ####
                widget.TextBox(
                    text="◢",
                    background=color[1],
                    foreground=color[0],
                    padding=-2,
                    fontsize=65
                    ),
                #widget.BatteryIcon(
                #    show_short_text=True,
                #    notify_below=30,
                #    discharge_char=' ',
                #    empty_char='',
                #    full_char=' ',
                #    background=color[0],
                #    foreground=color[7]
                #    ),
                #widget.Battery(
                #   battery="BAT1",
                #    format='{char} {percent:2.0%} {hour:d}:{min:02d}',
                #    show_short_text=True,
                #    update_interval=10,
                #    background=color[0],
                #    foreground=color[7]
                #    ),
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
        Screen(top=bar.Bar(widgets=init_widgets_screen_top(),  size=25, background=color[0]),
        bottom=bar.Bar(widgets=init_widgets_screen_bot(), size=25, background=color[0])),
        Screen()
        ]

#### End Screens ####

widget_defaults = init_widgets_defaults()
widgets_top = init_widgets_top()
widgets_bott = init_widgets_bott()