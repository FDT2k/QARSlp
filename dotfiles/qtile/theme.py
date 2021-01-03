# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
import os, re, subprocess, json
import socket
from libqtile.config import Key, Screen, Group, Match, Drag, Click, Rule
from libqtile import layout
from libqtile import bar, widget
from libqtile.widget import Spacer

home = os.path.expanduser('~')

## Import Network interface / Importar la tarjeta de red en uso ####

with open(home + '/.config/qtile/actnet', 'r') as file:
    netact = file.read().replace('\n', '')


##### Import Pywal Palette / Importar la paleta generada por pywal #####
with open(home + '/.cache/wal/colors.json') as json_file:
    data = json.load(json_file)
    colorsarray = data['colors']
    val_list = list(colorsarray.values())
    def getList(val_list):
        return [*val_list]

def init_colors():
    return [*val_list]

colors = init_colors()

def init_layout_theme():
    return {"font":"Fira Code Medium",
            "fontsize":14,
            "margin": 15,
            "border_width":5,
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
            #layout.Matrix(single_margin=10,border_normal=colors[0],border_focus=colors[7],**layout_theme),
            #layout.Zoomy(**layout_theme),
            layout.MonadTall(max_ratio=0.70, ratio=0.70, **layout_theme),
            #layout.Max(**layout_theme),
            layout.TreeTab(sections=["Tabs"],section_fontsize=14, bg_color=colors[0], active_bg=colors[7], active_fg=colors[0], inactive_bg=colors[0], inactive_fg=colors[7],padding_y=5,panel_width=250, **layout_theme),
            layout.Floating(float_rules=[{'wmclass': 'confirm'},{'wmclass': 'lxappearance'},{'wmclass': 'dialog'},{'wmclass': 'download'},{'wmclass': 'error'},{'wmclass': 'file_progress'},{'wmclass': 'notification'},{'wmclass': 'splash'},{'wmclass': 'toolbar'},{'wmclass': 'confirmreset'},{'wmclass': 'makebranch'},{'wmclass': 'maketag'},{'wname': 'branchdialog'},{'wname': 'pinentry'},{'wmclass': 'ssh-askpass'},{'wmclass': 'oblogout'},{'wmclass': 'Oblogout'},{'wmclass': 'Pavucontrol'},{'wmclass': 'Obconf'}])]


##### WIDGETS #####

def init_widgets_defaults():
    return dict(font="Fira Code Medium",fontsize=16,padding=2,background=colors[0])

def netw(qtile):
    qtile.cmd_spawn('network')

def urx(qtile):
    qtile.cmd_spawn('urxvt')

def htop(qtile):
    qtile.cmd_spawn('urxvt -e htop')

def rangercli(qtile):
    qtile.cmd_spawn('urxvt -e ranger')

def lock(qtile):
    qtile.cmd_spawn('betterlockscreen --lock')

def rboot(qtile):
    qtile.cmd_spawn('urxvt -e sudo reboot')

def poff(qtile):
    qtile.cmd_spawn('urxvt -e sudo poweroff')

def lout(qtile):
    qtile.cmd_spawn('qtile-cmd -o cmd -f shutdown')
    
def pav(qtile):
    qtile.cmd_spawn('pavucontrol')

def ran(qtile):
    qtile.cmd_spawn('rand')

def men(qtile):
    qtile.cmd_spawn("rofi -theme '~/.config/rofi/launcher.rasi' -show drun")

def wsh(qtile):
    qtile.cmd_spawn("/opt/bin/wsearch")
    #qtile.groups_map["4"].cmd_toscreen(toggle=False)

def ncsp(qtile):
    qtile.groups_map["7"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn('urxvt -e ncspot')

def xk(qtile):
    qtile.cmd_spawn("xkill")

def scuts(qtile):
    qtile.cmd_spawn("shortcuts")


def init_widgets_list_top():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list_top = [
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,foreground=colors[7],text="",mouse_callbacks={'Button1':men}),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,foreground=colors[7],text="",mouse_callbacks={'Button1':wsh}),        
                widget.Sep(padding=5,foreground=colors[7], linewidth=2),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,foreground=colors[7],text="",mouse_callbacks={'Button1':urx}),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,foreground=colors[7],text="",mouse_callbacks={'Button1':rangercli}),
                widget.Sep(padding=5,foreground=colors[7], linewidth=2),                        
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,foreground=colors[7],text="",mouse_callbacks={'Button1':ran}),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,foreground=colors[7],text="",mouse_callbacks={'Button1':xk}),
                widget.Sep(padding=5,foreground=colors[7], linewidth=2),                        
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,foreground=colors[7],text="",mouse_callbacks={'Button1':scuts}),
                widget.TextBox(foreground=colors[1],text="◢",fontsize=45,padding=-2),
                widget.GroupBox(font='Font Awesome 5 Free',fontsize=14, disable_drag=True, hide_unused=False, fontshadow=colors[0], margin_y=1, padding_x=5, borderwidth=0, active=colors[7],  inactive=colors[1], rounded=False, highlight_method="text", this_current_screen_border=colors[0], this_screen_border=colors[3], other_current_screen_border=colors[0], other_screen_border=colors[0], foreground=colors[2], background=colors[1]),
                widget.TextBox(background=colors[0],foreground=colors[1],text="◤ ",fontsize=45,padding=-2),
                widget.Notify(default_timeout=15, foreground_low=colors[3],foreground_urgent=colors[6], foreground=colors[7], background=colors[0]),
                widget.Spacer(length=bar.STRETCH,),
                
                widget.TextBox(text="◢", background=colors[0], foreground=colors[6], padding=-2, fontsize=45),
                ##### Network Interfaces ####
                widget.Wlan(font='Font Awesome 5 Free',fontsize=15,interface=netact, format='', foreground=colors[0], background=colors[6], fontshadow=colors[7],mouse_callbacks={'Button1':netw}),
                widget.Wlan(interface=netact, format='{essid} {percent:2.0%}', disconnected_message='Unplugged', foreground=colors[0], background=colors[6], mouse_callbacks={'Button1':netw}),
                widget.TextBox(text="◢", background=colors[6], foreground=colors[2], padding=-2, fontsize=45),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=15,text="", padding=5, foreground=colors[0], background=colors[2], fontshadow=colors[7], mouse_callbacks={'Button1': ncsp}),
                widget.Mpris2(name='ncspot', objname='org.mpris.MediaPlayer2.ncspot', scroll_chars=25, background=colors[2], foreground=colors[0], stop_pause_text= '', display_metadata=['xesam:artist','xesam:title'],scroll_interval=0.5, scroll_wait_intervals=1000),
                widget.TextBox(text='◢', background=colors[2], foreground=colors[5], padding=-2,fontsize=45),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=15,background=colors[5],foreground=colors[0],text=""),
                widget.Pomodoro(background=colors[5], foreground=colors[0], color_active=colors[0], color_break=colors[2], color_inactive=colors[0], length_pomodori=50, length_short_break= 5, length_long_break=15,
                num_pomodori=3, prefix_break='Break',  prefix_inactive='start', prefix_long_break='Long Break', prefix_paused='' ),
                widget.TextBox(text='◢', background=colors[5], foreground=colors[3], padding=-2,fontsize=45),
                #### Battery for laptops ####
                #widget.TextBox(font='Font Awesome 5 Free',text="", padding=5, foreground=colors[0], background=colors[3], fontshadow=colors[7], fontsize=14),
                #widget.KhalCalendar(lookahead=15, remindertime=60, foreground=colors[0], background=colors[7]),
                #widget.BitcoinTicker(),
                #widget.BatteryIcon(show_short_text=False, notify_below=30, charge_char=' ', discharge_char=' ', empty_char='', full_char=' ',background=colors[3], foreground=colors[0]),
                #widget.Battery(format='{percent:2.0%}', show_short_text=False,update_interval=5,background=colors[3], foreground=colors[0]),
                widget.TextBox(text='◢', background=colors[3], foreground=colors[7], padding=-2,fontsize=45),
                widget.TextBox(font='Font Awesome 5 Free',text=" ", foreground=colors[0], background=colors[7], padding=0, fontsize=15,mouse_callbacks={'Button1':pav}),
                widget.Volume(channel='Master', background=colors[7], foreground=colors[0], fontshadow=colors[7]),
                widget.TextBox(text='◢', background=colors[7], foreground=colors[0], padding=-2,fontsize=45),
                widget.TextBox(font='Font Awesome 5 Free',padding=1,text="",fontsize=14, foreground=colors[7],background=colors[0]),
                widget.Clock(foreground=colors[7], background=colors[0], format="%b %a %d", update_interval=1),
                widget.TextBox(text='◢', background=colors[0], foreground=colors[7], padding=-2,fontsize=45),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14, text="", foreground=colors[0],background=colors[7]),
                widget.Clock(foreground=colors[0], background=colors[7], format="%H:%M:%S",update_interval=1,),
                widget.TextBox(text='◢', background=colors[7], foreground=colors[0], padding=-2,fontsize=45),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,foreground=colors[7],text="",mouse_callbacks={'Button1': lock}),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,foreground=colors[7],text="",mouse_callbacks={'Button1': lout}),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,foreground=colors[7],text="",mouse_callbacks={'Button1': rboot}),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,foreground=colors[7],text="",mouse_callbacks={'Button1': poff}),
              ]
    return widgets_list_top

def init_widgets_list_bot():
    widgets_list_bot = [
                #widget.DebugInfo(foreground=colors[7], background=colors[0], fontshadow=colors[2]),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=15,foreground=colors[7],fontshadow=colors[4],text=""),
                widget.WindowName(foreground=colors[7], background=colors[0], padding=5),
                widget.Spacer(length=bar.STRETCH,),
                #widget.TextBox(text="◢",background=colors[0], foreground=colors[1], padding=-2, fontsize=45),
                #widget.YahooWeather(background=colors[1], foreground=colors[0], metric=True, update_interval=600, format='{location_city}: {condition_temp} °{units_temperature}', woeid='136973'),
                widget.TextBox(text='◢',background=colors[0],foreground=colors[6],padding=-2,fontsize=45,mouse_callbacks={'Button1': ncsp}),
                widget.Net(font='Font Awesome 5 Free',fontsize=15,interface=netact, format='↓', foreground=colors[0], background=colors[6], fontshadow=colors[7], use_bits=True, mouse_callbacks={'Button1':netw}),
                widget.Net(interface=netact, format='{down}', foreground=colors[0], background=colors[6], use_bits=True, mouse_callbacks={'Button1':netw}),
                widget.Net(font='Font Awesome 5 Free',fontsize=15,interface=netact, format='↑', foreground=colors[0], background=colors[6], fontshadow=colors[7], use_bits=True, mouse_callbacks={'Button1':netw}),
                widget.Net(interface=netact, format='{up}', foreground=colors[0], background=colors[6], use_bits=True, mouse_callbacks={'Button1':netw}),
                widget.TextBox(text="◢",background=colors[6], foreground=colors[2], padding=-2, fontsize=45),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,background=colors[2], foreground=colors[0],fontshadow=colors[7],text=""),
                widget.Memory(format='RAM {MemUsed}Mb',border_color=colors[0], graph_color=colors[0], foreground=colors[0], background=colors[2], padding=5),
                widget.TextBox(text="◢",background=colors[2], foreground=colors[5], padding=-2, fontsize=45),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,background=colors[5], foreground=colors[0],text="",fontshadow=colors[7]),
                widget.CPU(format='CPU {load_percent}%',border_color=colors[0], graph_color=colors[0], foreground=colors[0], background=colors[5], mouse_callbacks={'Button1': htop}),
                widget.CPUGraph(type='linefill', fill_color=colors[7], border_color=colors[0], graph_color=colors[0], foreground=colors[0], background=colors[5], padding=5, mouse_callbacks={'Button1': htop}),
                widget.TextBox(text="◢", background=colors[5], foreground=colors[3], padding=-2, fontsize=45),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,background=colors[3], foreground=colors[0],fontshadow=colors[7],text=""),
                widget.DF(format='{p} ({uf}{m}|{r:.0f}%)', measure='G', Partition='/', update_interval=60, foreground=colors[0], background=colors[3], padding=5, visible_on_warn=False,mouse_callbacks={'Button1':rangercli}),
                widget.TextBox(text="◢",background = colors[3],foreground=colors[7],padding=-2,fontsize=45),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=14,background=colors[7], foreground=colors[0],fontshadow=colors[7],text=""),
                widget.CurrentLayout(background=colors[7],foreground=colors[0], fontshadow=colors[7]),
                widget.TextBox(text="◢",background = colors[7],foreground=colors[0],padding=-2,fontsize=45),
                widget.TextBox(font='Font Awesome 5 Free',fontsize=17,text="",foreground=colors[7],background=colors[0]),
                widget.KeyboardLayout(foreground=colors[7],background=colors[0],padding=5, fontshadow=colors[4]),
                widget.TextBox(text="◢",background = colors[0],foreground=colors[7],padding=-2,fontsize=45),
                widget.CapsNumLockIndicator(foreground=colors[0],background=colors[7],padding=5),
                widget.TextBox(text="◢",background = colors[7],foreground=colors[0],padding=-2,fontsize=45),
                widget.Systray(icon_size=18, background=colors[0], foreground=colors[7]),]
    return widgets_list_bot

##### SCREENS #####

def init_widgets_top():
    widgets_screen_top = init_widgets_list_top()
    return widgets_screen_top
def init_widgets_bot():
    widgets_screen_bot = init_widgets_list_bot()
    return widgets_screen_bot

def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_top(),  size=20, background=colors[0]),
        bottom=bar.Bar(widgets=init_widgets_bot(), size=20, background=colors[0])),
        Screen(top=bar.Bar(widgets=init_widgets_top(),  size=20, background=colors[0]),
        bottom=bar.Bar(widgets=init_widgets_bot(), size=20, background=colors[0]))
        ]

colors = init_colors()
layout_theme = init_layout_theme()
layouts = init_layouts()
widget_defaults = init_widgets_defaults()
widgets_list_top = init_widgets_list_top()
widgets_list_bot = init_widgets_list_bot()
widgets_screen_top = init_widgets_top()
widgets_screen_bot = init_widgets_bot()
screens = init_screens()

