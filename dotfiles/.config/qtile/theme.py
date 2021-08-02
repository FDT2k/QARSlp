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
                    mouse_callbacks={'Button1': cfilex},
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

widget_defaults = init_widgets_defaults()
wid_list_top = init_wid_list_top()
wid_list_bot = in_wid_list_bot()
wid_list_sec = in_wid_list_sec()