
import subprocess
from os.path import expanduser

home = expanduser("~")


dir="${HOME}"'/Pictures/wallPapers' # Wallpapers Directory
backend="$1" # Argument for backend to use
rand_wall (){
  file=`/bin/ls -1 "$dir" | sort --random-sort | head -1` # Select random file on directory
  path=`readlink --canonicalize "$dir/$file"` # Converts to full path
  echo "${path}" | tee ~/.config/qtile/current_wallpaper #Write wallpaper path to file
  wpg -s "${path}" # Wal sets wallpaper and genates new color scheme
  sudo rm -rf /usr/share/background.png
  sudo cp "${path}" /usr/share/backgrounds/background.png #Copy background image image to be used in sddm
  wal -R #Refresh wal for visual studio code
  qtile cmd-obj -o cmd -f restart # Restarts Qtile
}
rand_wall &
