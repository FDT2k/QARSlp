# QARSlp OS Qtile + Arch + AutoRicing Script

by: gibranlp thisdoesnotwork@gibranlp.dev

MIT licence

Fork / upgrade from [QAAS](https://github.com/gibranlp/QAAS), the  Autoricing feature depends entirely on the Wallpaper, it generates several palettes using pywal and wpgtk to adapt the colors of the entire system to the wallpaper

## Installation

This is based on ![Arch](https://archlinux.org/) so any Arch based distro works, it also depends on Systemd, distros like ![Artix](https://artixlinux.org/) may need further configuration.

## Prerequisites

- [x] Arch based distro
- [ ] Zen Kernel
  - [ ] Best for multimedia, and gaming workloads.
- [x] Zsh and Ohmyzsh installed,  you can check [here](https://ohmyz.sh/#install)
- [x] Also install this 2 plugins for ZSH
```bash
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
```
- [x] Add your user to the sudoers file, if you don't know how to do it check this [guide](https://gibranlp.dev/post/add-user-sudoers-file/) 

## Installation

  First you need to clone this repository
```bash
git clone https://github.com/gibranlp/QARSlp.git
cd QARSlp/installer
chmod +x dependencies.sh
chmod +x cp_files.sh
chmod +x post_install.sh
./dependencies.sh #This will install all the programs needed
./cp_files.sh #This will copy all the dotfiles needed
./post_install #This will run wpgtk for the first time
```
## Things to consider after installing

## Features
- [x] Qtile adapts with the wallpaper colors 
- [x] Auto detects the network card in use to display it on widgets
- [x] Wallpaper generated is now saved into a file for further use (backend changes)
- [x] Packs of wallpapers
  - [x] [Pack 1](https://gibranlp.dev/wallpacks/pack1.tar.gz)
  - [x] [Pack 2](https://gibranlp.dev/wallpacks/pack2.tar.gz)
  - [x] [Pack 3](https://gibranlp.dev/wallpacks/pack3.tar.gz)
  - [x] All the wallpapers should be on **~/Pictures/wallPapers**

### Menu launchers
- [x] Launcher
- [x] Web search
- [x] Terminal
- [x] Ranger ~/
- [x] Randomize wallpaper
- [x] Vis (CLI-visualizer)
- [x] Ncspot (CLI Spotify client)
- [x] Shortcuts widget
- [x] Sessión menu(top-right)

### Widgets ![Rofi](https://github.com/davatorium/rofi) based

- [x] Launcher

![Launcher](https://github.com/gibranlp/QARSlp/blob/main/screenshots/launcher.png)

- [x] Change palette using the same wallpaper dark / light 
    - [x] colorz
    - [x] haishoku
    - [x] schemer2
    - [x] wal
    - [x] colorthief

![Change theme](https://github.com/gibranlp/QARSlp/blob/main/screenshots/backend.png)

- [x] Automatically change wallpaper every X minutes

![Chwall](https://github.com/gibranlp/QARSlp/blob/main/screenshots/chwall.png)


- [x] Web Search (Based on ![Surfraw](https://github.com/JNRowe/surfraw))

![Web search](https://github.com/gibranlp/QARSlp/blob/main/screenshots/search.png)

- [x] Network / Internet
  - [x] Speedtest-cli (CLI Network settings)
  - [x] Wireshark-cli (CLI Network settings)
  - [x] Nmtui (CLI Network settings)
  - [x] Bmon (CLI Network monitor)

![Network](https://github.com/gibranlp/QARSlp/blob/main/screenshots/network.png)

- [x] Screenshot based on ![scrot](https://github.com/dreamer/scrot) menu

![Screenshot](https://github.com/gibranlp/QARSlp/blob/main/screenshots/screen.png)

- [x] Shortcuts widget

![Shortcuts](https://github.com/gibranlp/QARSlp/blob/main/screenshots/shortcuts.png)

- [x] Session menu
    - [x] Logout
    - [x] Power Off
    - [x] Reboot

![Session](https://github.com/gibranlp/QARSlp/blob/main/screenshots/session.png)


## Other included apps

- [x] Firefox
- [x] Visual-studio-code
- [x] Qtile (wm)
- [x] Rofi
- [x] Libre Office
- [x] All GTK apps are color updated now thanks to [wpgtk](https://github.com/deviantfero/wpgtk)

# Screenshots

![1](https://github.com/gibranlp/QARSlp/blob/main/screenshots/1.png)
![2](https://github.com/gibranlp/QARSlp/blob/main/screenshots/2.png)
![3](https://github.com/gibranlp/QARSlp/blob/main/screenshots/3.png)
![4](https://github.com/gibranlp/QARSlp/blob/main/screenshots/4.png)
![5](https://github.com/gibranlp/QARSlp/blob/main/screenshots/5.png)
![7](https://github.com/gibranlp/QARSlp/blob/main/screenshots/6.png)
![7](https://github.com/gibranlp/QARSlp/blob/main/screenshots/7.png)
![8](https://github.com/gibranlp/QARSlp/blob/main/screenshots/8.png)
![9](https://github.com/gibranlp/QARSlp/blob/main/screenshots/9.png)
![10](https://github.com/gibranlp/QARSlp/blob/main/screenshots/10.png)


<a href="https://www.buymeacoffee.com/gibranlp"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a Coffee&emoji=&slug=gibranlp&button_colour=FFDD00&font_colour=000000&font_family=Bree&outline_colour=000000&coffee_colour=ffffff"></a>