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
  packets=('htop' 'alsa-utils' 'alsa-lib' 'alsa-firmware' 'ttf-fira-code' 'ttf-font-awesome' 'playerctl' 'kdeconnect' 'firefox' 'pulseaudio' 'pulseaudio-alsa' 'pavucontrol' 'volumeicon' 'picom' 'scrot' 'rofi' 'surfraw' 'python-pip' 'pkgfile' 'ranger' 'tumbler' 'feh' 'neofetch' 'lxappearance' 'lxsession' 'numlockx' 'unzip' 'bmon' 'dunst' 'lightdm' 'lightdm-gtk' 'lightdm-gtk-greeter' 'lightdm-gtk-greeter-settings' 'lm_sensors' 'obconf' 'viewnior' 'ntp' 'nm-connection-editor' 'network-manager-applet' 'arandr' 'cmatrix' 'thunar' 'thunar-archive-plugin' 'thunar-volman' 'python-pywal' 'python-psutil' 'python-xdg' 'python-iwlib' 'python-dateutil' 'ueberzug' 'xsettingsd' 'otf-ipafont' 'acpi' 'qtile' 'wget' 'cmake'
)

for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    sudo pacman -S "${packet}" --noconfirm --needed
done
}

function i_aur () {
  packets=(
    'visual-studio-code-bin' '7-zip' 'rxvt-unicode-patched-with-scrolling' 'wpgtk-git' 'nbfc' 'gtk-theme-flat-color-git' 'otf-symbola' 'pamac-classic'
)


for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    paru -S "${packet}" --noconfirm
done
}

function i_files(){
  \cp -r  ~/QARSlp/dotfiles/.[^.]* ~/
  cp -r  ~/QARSlp/dotfiles/shortc.conf ~/
  mkdir -p ~/Pictures/wallPapers
  cp ~/QARSlp/walls/* ~/Pictures/wallPapers
  sudo cp -r  ~/.cache/wal /root/.cache/
  sudo \cp ~/.face /usr/share/profile.png
  cp ~/QARSlp/dotfiles/.config/wal/dunstrc ~/.config/wal/templates/
  if [ -d "/usr/local/bin" ];  then
    sudo cp -r  ~/QARSlp/scripts/* /usr/local/bin 
    sudo cp -r  ~/QARSlp/widgets/* /usr/local/bin 
  else
    sudo mkdir /usr/local/bin 
    sudo cp -r  ~/QARSlp/scripts/* /usr/local/bin 
    sudo cp -r  ~/QARSlp/widgets/* /usr/local/bin 
 fi
if [ -d "/root/.themes/FlatColor" ]; then
    sudo cp -r  ~/QARSlp/dotfiles/.themes/FlatColor/* /root/.themes/FlatColor/ 
  else
    sudo mkdir -p /root/.themes/FlatColor 
    sudo cp -r  ~/QARSlp/dotfiles/.themes/FlatColor/* /root/.themes/FlatColor/
fi

}

function i_settings(){
    /usr/local/bin/genwal 
    sudo systemctl enable lightdm.service
    pywalfox install 
    wpg-install.sh -g -d -i 
    /usr/local/bin/autostart 
    /usr/local/bin/alwaystart 
    
}


i_files
i_settings
