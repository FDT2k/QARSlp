# QARSlp Qtile Auto Ricing Script v1.1
by: gibranlp ![thisdoesnotwork@gibranlp.dev](mailto:thisdoesnotwork@gibranlp.dev)
MIT licence

Fork / upgrade from [QAAS](https://github.com/gibranlp/QAAS), the  Autoricing feature depends entirely on the Wallpaper, it generates several palettes using pywal and wpgtk to adapt the colors of the entire system to the wallpaper





## Installation

This is based on ![Arch](https://archlinux.org/) so any Arch based distro works, it also depends on Systemd, distros like ![Artix](https://artixlinux.org/) may need further configuration.

## All neded for installation is a Arch Based Distro

### Installation

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
  - [x] All the wallpapers should be on **~/Pictures/wallPapers** This folder is created with the installation.

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




- [x] Web Search (Based on ![Surfraw](https://github.com/JNRowe/surfraw))

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


## Apps and Misc

### Terminal & GTK

![TGTK](https://github.com/gibranlp/QARSlp/blob/main/screenshots/apps/2.png)
![TGTK](https://github.com/gibranlp/QARSlp/blob/main/screenshots/apps/10.png)

### Thunderbird
![Thunderbird](https://github.com/gibranlp/QARSlp/blob/main/screenshots/apps/3.png)
![Thunderbird](https://github.com/gibranlp/QARSlp/blob/main/screenshots/apps/11.png)

### Thunar & Icons
![Thunar & Icons](https://github.com/gibranlp/QARSlp/blob/main/screenshots/apps/4.png)
![Thunar & Icons](https://github.com/gibranlp/QARSlp/blob/main/screenshots/apps/12.png)

### Firefox
![Firefox](https://github.com/gibranlp/QARSlp/blob/main/screenshots/apps/5.png)
![Firefox](https://github.com/gibranlp/QARSlp/blob/main/screenshots/apps/15.png)

### Vscode
![Vscode](https://github.com/gibranlp/QARSlp/blob/main/screenshots/apps/6.png)
![Vscode](https://github.com/gibranlp/QARSlp/blob/main/screenshots/apps/16.png)

### Libre Office
![Libre Office](https://github.com/gibranlp/QARSlp/blob/main/screenshots/apps/8.png)



- [x] Firefox
  - You must install the addon pywalfox
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