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
    'nm-connection-editor'
    'nm-applet'
    'arandr'
    'system-config-printer'
    'cmatrix'
    'pip'
    'python-pywal'
    'python-psutil'
    'python-xdg'
    'python-iwlib'
    'python-ipc'
    'python-dateutil'

    
)

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
    'fontawesome'
    'ipc'
    'pywalfox'
    'colorz'
    'colorthief'
    'haishoku'
  )

  for pip_packet in "${pip_packets[@]}"; do
    echo "Instalando --> ${pip_packet}"
    sudo pip install "${pip_packet}"
  done
}

function i_aur () {
  packets=(
    'betterlockscreen'
    'python-haishoku'
    'python-colorthief'
    'visual-studio-code-bin'
    'cli-visualizer'

    
)

for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    sudo paru -S "${packet}" --noconfirm
done
}

# paru -S   python-haishoku python-colorthief visual-studio-code-bin cli-visualizer --skipreview --noconfirm


function i_post(){
  pywalfox install &
  timedatectl set-timezone America/Cancun &
  timedatectl set-ntp true &

}

i_base
i_paru
i_pip
