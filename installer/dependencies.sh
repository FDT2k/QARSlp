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
    'emacs'
    'fd'
    'alsa-utils'
    'alsa-lib'
    'alsa-firmware'
    'gstreamer'
    'gst-plugins-bad'
    'gst-plugins-base'
    'gst-plugins-ugly'
    'alsa-plugins'
    'ttf-fira-code'
    'ttf-font-awesome'
    'telegram-desktop'
    'playerctl'
    'kdeconnect'
    'gparted'
    'firefox'
    'filezilla'
    'libreoffice-fresh'
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
    'gnome-keyring'
    'scrot'
    'rofi'
    'surfraw'
    'python-pip'
    'pkgfile'
    'ranger'
    'dunst'
    'tumbler'
    'feh'
    'neofetch'
    'lxappearance'
    'lxsession'
    'transmission-gtk'
    'numlockx'
    'unzip'
    'hugo'
    'gnome-disk-utility'
    'bmon'
    'lm_sensors'
    'obconf'
    'viewnior'
    'ntp'
    'nautilus'
    'xarchiver'
    'nm-connection-editor'
    'network-manager-applet'
    'arandr'
    'system-config-printer'
    'cmatrix'
    'python-pywal'
    'python-psutil'
    'python-xdg'
    'python-iwlib'
    'python-dateutil'
    'ueberzug'
    'thunderbird'
    'xsettingsd'
    

    
)

for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    sudo pacman -S "${packet}" --noconfirm --needed
done
}



function i_cli(){
  git clone https://github.com/dpayne/cli-visualizer.git
  cd cli-visualizer
  chmod +x installer.sh
  ./installer.sh
  cd
  rm -rf cli-visualizer
}

function i_pip(){
  pip_packets=(
    'fontawesome'
    'ipc'
    'pywalfox'
    'colorz'
    'colorthief'
    'haishoku'
    'dbus-next'
   
  )

  for pip_packet in "${pip_packets[@]}"; do
    echo "Instalando --> ${pip_packet}"
    sudo pip install "${pip_packet}"
  done
}

function i_aur () {
  packets=(
<<<<<<< HEAD
    'python-haishoku'
    'python-colorthief'
=======
>>>>>>> f7a2963f6d70064332dff1041838b929d8b71fd8
    'visual-studio-code-bin'
    'minder'
    'ocs-url'
    'ncspot'
    'alacritty' #Terminal
    'wpgtk-git'
<<<<<<< HEAD
    'nbfc'
=======
    'spicetify-cli'
    'nbfc' # Fan speed control
    'typora' # Md files editor
>>>>>>> f7a2963f6d70064332dff1041838b929d8b71fd8
    
)

for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    paru -S "${packet}" --noconfirm
done
}

function i_post(){
  sudo timedatectl set-timezone America/Mexico &
  sudo timedatectl set-ntp true &
  pywalfox install &
  sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" -y &
  git clone https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/plugins/zsh-autosuggestions &
  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/plugins/zsh-syntax-highlighting &
  
}

i_base
i_pip
i_aur
i_post
