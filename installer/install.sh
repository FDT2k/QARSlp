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
## Apps

function i_zsh(){
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
    git clone https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/plugins/zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/plugins/zsh-syntax-highlighting
}

function i_paru(){
  git clone https://aur.archlinux.org/paru.git
  cd paru
  makepkg -sri --noconfirm
  cd ..
  rm -rf paru
}

function i_base () {
  packets=('htop' 'alsa-utils' 'alsa-lib' 'bc' 'nextcloud-client' 'hugo' 'ntfs-3g' 'grub-customizer' 'libreoffice-fresh' 'alsa-firmware' 'ttf-fira-code' 'ttf-font-awesome' 'playerctl' 'kdeconnect' 'firefox' 'pulseaudio' 'pulseaudio-alsa' 'pavucontrol' 'volumeicon' 'picom' 'scrot' 'rofi' 'surfraw' 'python-pip' 'pkgfile' 'ranger' 'tumbler' 'feh' 'neofetch' 'lxappearance' 'lxsession' 'numlockx' 'unzip' 'bmon' 'dunst' 'lightdm' 'lm_sensors' 'obconf' 'viewnior' 'ntp' 'nm-connection-editor' 'network-manager-applet' 'arandr' 'cmatrix' 'thunar' 'thunar-archive-plugin' 'thunar-volman' 'python-pywal' 'python-psutil' 'python-xdg' 'python-iwlib' 'python-dateutil' 'ueberzug' 'xsettingsd' 'otf-ipafont' 'acpi' 'qtile' 'wget' 'cmake' 'lightdm-webkit2-greeter' 'tlp'
)

for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    sudo pacman -S "${packet}" --noconfirm --needed
done
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
    'git+http://github.com/bcbnz/python-rofi.git'
   
  )

  for pip_packet in "${pip_packets[@]}"; do
    echo "Instalando --> ${pip_packet}"
    sudo pip install "${pip_packet}"
  done
}

function i_aur () {
  packets=(
    'visual-studio-code-bin' '7-zip' 'rxvt-unicode' 'wpgtk-git' 'nbfc' 'slack-desktop' 'ncspot' 'telegram-desktop' 'notion-app' 'qtile-extras-git'
)


for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    paru -S "${packet}" --noconfirm
done
}

function i_settings(){
  /usr/local/bin/genwal &
  sudo timedatectl set-timezone America/Mexico_City &
  sudo timedatectl set-ntp true &
  pywalfox install &
  git clone https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/plugins/zsh-autosuggestions &
  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/plugins/zsh-syntax-highlighting &
  git config --global user.name "gibranlp" &
  git config --global user.email gibranlp@gmail.com & 
  wpg-install.sh -g -d -i &
  /usr/local/bin/autostart &
  /usr/local/bin/alwaystart &
  
}

function i_files(){
\cp -r ~/QARSlp/dotfiles/.[^.]* ~/ 
sudo \cp -r ~/QARSlp/dotfiles/.[^.]* /root 
\cp -r ~/QARSlp/dotfiles/.config/qtile/themes/default/wallPapers ~/Pictures 
sudo \cp -r  ~/QARSlp/scripts/* /usr/local/bin 
sudo chmod +x /usr/local/bin/*
sudo \cp -r ~/QARSlp/lightdm/* /etc/lightdm
sudo \cp -r ~/QARSlp/lightdm-webkit /usr/share
  
fi

}


i_zsh
i_paru
i_base
i_pip
i_aur
i_files
i_settings

