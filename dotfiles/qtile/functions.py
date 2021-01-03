# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
def netw(qtile):
    qtile.cmd_spawn('network')

def urx(qtile):
    qtile.cmd_spawn('urxvt')

def htop(qtile):
    qtile.cmd_spawn('urxvt -e htop')

def rangercli(qtile):
    qtile.cmd_spawn('pcmanfm')

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
    qtile.cmd_spawn('/opt/bin/genwal')

def men(qtile):
    qtile.cmd_spawn("rofi -theme '~/.config/rofi/launcher.rasi' -show drun")

def wsh(qtile):
    qtile.groups_map["4"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn("/opt/bin/wsearch")
    

def ncsp(qtile):
    qtile.groups_map["7"].cmd_toscreen(toggle=False)
    qtile.cmd_spawn('urxvt -e ncspot')

def xki(qtile):
    qtile.cmd_spawn("xkill")

def scuts(qtile):
    qtile.cmd_spawn("/opt/bin/shortcuts")
