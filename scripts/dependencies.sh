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

#!/usr/bin/env bash

function i_base () {
  packets=(
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
    'telegram-desktop'
    'playerctl'
    'firefox'
    'filezilla'
    'rxvt-unicode'
    'urxvt-perls'
    'cups'
    'cups-pdf'
    'speedtest-cli'
    'wireshark-cli'
    'gutenprint'
    'gtk3-print-backends'
    'nmap'
    'pulseaudio'
    'pulseaudio-alsa'
    'pavucontrol'
    'volumeicon'
    'picom'
    'qtile'
    'lshw'
    'ttf-font-awesome'
    'gnome-keyring'
    'scrot'
    'rofi'
    'surfraw'
    'python-pip'
    'pkgfile'
    'ranger'
    'zsh'
    'feh'
    'xorg-server-xephyr'
    'neofetch'
    'lxappearance'
    'lxsession'
    'transmission-gtk'
    'numlockx'
    'unzip'
    'hugo'
    'khal'
    'vdirsyncer'
    'bmon'
    'lm_sensors'
    'vis'
    'obconf'
    'viewnior'
    'ntp'
    'pcmanfm'
    'imagewriter'
    'mintstick'
    'nm-connection-editor'
    'nm-applet'
    'arandr'
    'gparted'
    'system-config-printer'


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




function i_yay(){
  git clone https://aur.archlinux.org/yay.git && cd yay
  makepkg -si && cd
  rm -rf yay
  yay
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
  )

  for pip_packet in "${pip_packets[@]}"; do
    echo "Instalando --> ${pip_packet}"
    sudo pip install "${pip_packet}"
  done
}

# yay -S anydesk-bin betterlockscreen python-haishoku python-colorthief visual-studio-code-bin dnsutils

function i_post(){
  pywalfox install &
  timedatectl set-timezone America/Cancun &
  timedatectl set-ntp true &

}

i_base
i_yay
i_pip
