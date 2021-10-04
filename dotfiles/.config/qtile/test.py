from funct import *

backend = ['Wal', 'Haishoku', 'Colorz', 'Colorthief']
def change_color_scheme(qtile):
    options = [backend[0],backend[1],backend[2],backend[3], '<<-<< Light Themes >>-->>', backend[0],backend[1],backend[2],backend[3]]
    index, key = rofi_l.select('  Color Scheme', options)
    if key == -1 or index == 5:
        rofi_r.close()
    elif key == 0 and index < 4:
        print('wpg -s ' + wallpaper + ' --backend ' + backend[index].lower())
        #subprocess.run('wpg -s ' + wallpaper + ' --backend ' + backend[index].lower(), shell=True)
        #qtile.cmd_restart()
    elif key == 0 and index > 4:
        print('wpg -s ' + wallpaper + ' -L --backend ' + backend[index-5].lower())
        #subprocess.run('wpg -s ' + wallpaper + ' -L --backend ' + backend[index-5].lower(), shell=True)
        #qtile.cmd_restart()

change_color_scheme(qtile)