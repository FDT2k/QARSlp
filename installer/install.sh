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
  cd
  rm -rf paru
}

function i_base () {
  packets=('htop' 'alsa-utils' 'alsa-lib' 'alsa-firmware' 'ttf-fira-code' 'ttf-font-awesome' 'playerctl' 'kdeconnect' 'firefox' 'pulseaudio' 'pulseaudio-alsa' 'pavucontrol' 'volumeicon' 'picom' 'scrot' 'rofi' 'surfraw' 'python-pip' 'pkgfile' 'ranger' 'tumbler' 'feh' 'neofetch' 'lxappearance' 'lxsession' 'numlockx' 'unzip' 'bmon' 'dunst' 'lightdm' 'lm_sensors' 'obconf' 'viewnior' 'ntp' 'nm-connection-editor' 'network-manager-applet' 'arandr' 'cmatrix' 'thunar' 'thunar-archive-plugin' 'thunar-volman' 'python-pywal' 'python-psutil' 'python-xdg' 'python-iwlib' 'python-dateutil' 'ueberzug' 'xsettingsd' 'otf-ipafont' 'acpi' 'qtile' 'wget' 'cmake' 'lighdm-webkit2-greeter'
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
    'visual-studio-code-bin' '7-zip' 'rxvt-unicode-patched-with-scrolling' 'wpgtk-git' 'nbfc'
)


for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    paru -S "${packet}" --noconfirm
done
}

function i_settings(){
  sudo timedatectl set-timezone America/Mexico_City &
  sudo timedatectl set-ntp true &
  pywalfox install &
  git clone https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/plugins/zsh-autosuggestions &
  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/plugins/zsh-syntax-highlighting &
  git config --global user.name "gibranlp" &
  git config --global user.email gibranlp@gmail.com & 
  wpg-install.sh -g -d -i &
  /opt/bin/autostart &
  /opt/bin/alwaystart &
  /opt/bin/genwal &
}

function i_files(){
  cp -r  ~/QARSlp/dotfiles/.[^.]* ~/
  cp -r  ~/QARSlp/dotfiles/shortc.conf ~/
  cp -r ~/QARSlp/wallPapers ~/Pictures
  sudo cp -r  ~/.cache/wal /root/.cache/
  sudo cp ~/QARSlp/dotfiles/lightdm/lightdm-gtk-greeter.conf /etc/lightdm/
  ln -s ~/.config/qtile/themes/qarslp.py  ~/.config/qtile/theme.py
  
  if [ -d "/opt/bin" ];  then
    sudo cp -r  ~/QARSlp/scripts/* /opt/bin &
    sudo cp -r  ~/QARSlp/widgets/* /opt/bin &
  else
    sudo mkdir /opt/bin &
    sudo cp -r  ~/QARSlp/scripts/* /opt/bin &
    sudo cp -r  ~/QARSlp/widgets/* /opt/bin &
 fi
  if [ -d "/root/.config/rofi" ]; then
    sudo cp -r  ~/QARSlp/dotfiles/.config/rofi/* /root/.config/rofi/ &
  else
    sudo mkdir -p /root/.config/rofi &
    sudo cp -r  ~/QARSlp/dotfiles/.config/rofi/* /root/.config/rofi/ &
fi
if [ -d "/root/.themes/FlatColor" ]; then
    sudo cp -r  ~/QARSlp/dotfiles/.themes/FlatColor/* /root/.themes/FlatColor/ &
  else
    sudo mkdir -p /root/.themes/FlatColor &
    sudo cp -r  ~/QARSlp/dotfiles/.themes/FlatColor/* /root/.themes/FlatColor/ &
fi

}


i_zsh
i_paru
i_base
i_pip
i_aur
i_files
i_settings

