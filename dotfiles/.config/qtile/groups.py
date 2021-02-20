# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
import os
from libqtile.command import lazy
from libqtile.config import Group, Match, Drag, Rule

home = os.path.expanduser('~')

##### Window Functions / Funciones de las ventanas #####

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

##### Specific Apps/Groups / Apps/Grupos especificos #####

def app_or_group(group, app):
    def f(qtile):
        if qtile.groups_map[group].windows:
            qtile.groups_map[group].cmd_toscreen(toggle=False)
            qtile.cmd_spawn(app)
        else:
            qtile.groups_map[group].cmd_toscreen(toggle=False)
            qtile.cmd_spawn(app)
    return f


##### GROUPS #####

groups = [
    Group("1",position=1,matches=[Match(wm_class=['thunar', 'Thunar', 'gnome-disks', 'Gnome-disks', 'anydesk', 'Simplenote', 'Anydesk'])],layout="monadtall",label=""),
    Group("2",position=2,matches=[Match(wm_class=['Zoom','zoom', 'Mailspring', 'mailspring', 'transmission-gtk','Transmission-gtk'])],layout="monadtall",label=""),
    Group("3",position=3,matches=[Match(wm_class=['whatsdesk','telegram-desktop-bin', 'TelegramDesktop', 'Discord', 'discord'])],layout="matrix",label=""),
    Group("4",position=4,matches=[Match(wm_class=['firefox'])],layout="monadtall",label=""),
    Group("5",position=5,matches=[Match(wm_class=['Code', 'code','Filezilla'])],layout="monadtall",label=""),
    Group("6",position=6,matches=[Match(wm_class=['Gimp-2.10','Inkscape','Evince', 'libreoffice','Com.github.phase1geo.minder'])],layout="monadtall",label=""),
    Group("7",position=7,layout="monadtall",label=""),
    Group("8",position=8,matches=[Match(wm_class=['VirtualBox Manager', 'VirtualBox Machine'])],layout="monadtall",label=""),
    Group("9",position=9,layout="monadtall",label="")]
