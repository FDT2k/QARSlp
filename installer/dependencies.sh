#!/usr/bin/env bash
# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# by: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
# 
function i_base () {
  packets=(
    'base-devel'
    'htop'
    'git'
    'alsa-utils'
    'alsa-lib'
    'alsa-firmware'
    'gstreamer'
    'gst-plugins-bad'
    'gst-plugins-base'
    'gst-plugins-ugly'
    'alsa-plugins'
    'ttf-fira-code'
    #'telegram-desktop'
    'playerctl'
    'firefox'
    #'filezilla'
    'rxvt-unicode'
    'urxvt-perls'
    'cups'
    'cups-pdf'
    'speedtest-cli'
    'wireshark-cli'
    'gutenprint'
    'gtk3-print-backends'
    #'nmap'
    'pulseaudio'
    'pulseaudio-alsa'
    'pavucontrol'
    'volumeicon'
    'picom'
    'qtile'
    'lshw'
    'ttf-font-awesome'
    #'gnome-keyring'
    'scrot'
    'rofi'
    'surfraw'
    'python-pip'
    #'pkgfile'
    'ranger'
    'zsh'
    'feh'
    'xorg-server-xephyr'
    'neofetch'
    'lxappearance'
    'lxsession'
    #'transmission-gtk'
    'numlockx'
    #'unzip'
    #'hugo'
    #'khal'
    #'vdirsyncer'
    'bmon'
    'lm_sensors'
    'obconf'
    'viewnior'
    'ntp'
    'pcmanfm'
    'imagewriter'
    #'mintstick'
    'nm-connection-editor'
    'nm-applet'
    'arandr'
    #'gparted'
    'system-config-printer'
    'cmatrix'
    #'kdeconnect'
)

for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    sudo pacman -S "${packet}" --noconfirm --needed
done
}



for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    sudo pacman -S "${packet}" --noconfirm --needed
done
}




function i_paru(){
  git clone https://aur.archlinux.org/paru.git
  cd paru
  makepkg -si
  cd
  rm -rf paru
}

function i_pip(){
  pip_packets=(
    'pywal'
    'psutil'
    'fontawesome'
    'xdg'
    'iwlib'
    'ipc'
    'pywalfox'
    'python-dateutil'
    'colorz'
    'colorthief'
    'haishoku'
    'schemer2'
  )

  for pip_packet in "${pip_packets[@]}"; do
    echo "Instalando --> ${pip_packet}"
    sudo pip install "${pip_packet}"
  done
}

# yay -S  betterlockscreen python-haishoku python-colorthief visual-studio-code-bin cli-visualizer

#anydesk-bin

function i_post(){
  pywalfox install &
  timedatectl set-timezone America/Cancun &
  timedatectl set-ntp true &

}

i_base
i_paru
i_pip
