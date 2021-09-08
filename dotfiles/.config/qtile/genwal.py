import os, random
import subprocess
from os.path import expanduser



def set_wallpaper():
  home = expanduser("~")
  dir = home + '/Pictures/wallPapers'
  wallpaper = random.choice(os.listdir(dir))
  random_wallpaper = os.path.join(dir, wallpaper)
  with open (home + "/.config/qtile/current_wallpaper", "w") as currentWal:
    currentWal.write(random_wallpaper)

  subprocess.run(["wpg", "-s" + random_wallpaper])
  subprocess.run(["sudo", "cp", "%s" % random_wallpaper,  "/usr/share/backgrounds/background.png"])
  subprocess.run(["wal", "-R"])
  subprocess.run('qtile cmd-obj -o cmd -f restart', shell=True)
  

set_wallpaper()