# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 

import os, random
import subprocess
from os.path import expanduser



def set_wallpaper(qtile):
    dir = home + '/Pictures/wallPapers'
    wallpaper = random.choice(os.listdir(dir))
    random_wallpaper = os.path.join(dir, wallpaper)
    with open (home + "/.config/qtile/current_wallpaper", "w") as currentWal:
        currentWal.write(random_wallpaper)
    subprocess.run(["wpg", "-s" + random_wallpaper])
    subprocess.run(["sudo", "cp", "%s" % random_wallpaper,  "/usr/share/backgrounds/background.png"])
    subprocess.run(["wal", "-R"])
    qtile.cmd_restart()
  

set_wallpaper()