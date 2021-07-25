# QARSlp OS Qtile + Arch + AutoRicing + Installable ISO

by: gibranlp thisdoesnotwork@gibranlp.dev 
MIT licence

Fork / upgrade from ![QAAS](https://github.com/gibranlp/QAAS), this OS Autoricing feature depends entirely on the Wallpaper, it generates several palettes using pywal and wpgtk to adapt the colors of the entire system to the wallpaper

## Installation

This is based on ![Arch](https://archlinux.org/) so any Arch based distro works, it also depends on Systemd, distros like ![Artix](https://artixlinux.org/) may need further configuration.

  - First you need to clone this repository
    - `git clone https://github.com/gibranlp/QARSlp.git`
    - `cd QARSlp/installer`
  - This Scrip will install all the programs and dependencies needed for this to work the sudo password is needed a few times, (if you want to avoid this add your user to the sudoers file see ![here](https://gibranlp.dev/post/sudoers/))

  - `chmod +x ./base.sh`
    - `chmod +x ./cp_files.sh`

## Features
- [x] Packs of wallpapers
- [ ] ISO installable by script (Work in progress towards version 1.0)
- [x] Qtile adapts with the wallpaper colors 
- [x] Auto detects the network card in use to display it on widgets
- [x] Wallpaper generated is now saved into a file for further use (backend changes)

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
- [x] Change palette (same wallpaper) 
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
- [x] Screenshot based on ![scrot](https://github.com/dreamer/scrot) menu
- [x] Shortcut's page / search
- [x] Session menu
    - [x] Logout
    - [x] Power Off
    - [x] Reboot

## Planned upgrades
- [ ] Autoconnect hdmi display on laptop
- [ ] Assign specific group to external display
- [x] Choose on different palettes
- [x] Color theme selector
  - [x] Dark
    - [x] Wal
    - [x] Haishoku
    - [x] Colorz
    - [x] Colorthief
  - [x] Light
    - [x] Wal
    - [x] Haishoku
    - [x] Colorz
    - [x] Colorthief

## Other included apps

- [x] Firefox
- [x] Visual-studio-code
- [x] Qtile (wm)
- [x] Rofi
- [x] Libre Office

# Screenshots

![1](https://github.com/gibranlp/QARSlp/blob/main/screenshots/1.%20.png)
![2](https://github.com/gibranlp/QARSlp/blob/main/screenshots/2.%20.png)
![3](https://github.com/gibranlp/QARSlp/blob/main/screenshots/3.%20.png)
![4](https://github.com/gibranlp/QARSlp/blob/main/screenshots/4.%20.png)
![5](https://github.com/gibranlp/QARSlp/blob/main/screenshots/5.%20.png)
![6](https://github.com/gibranlp/QARSlp/blob/main/screenshots/6.%20.png)
![7](https://github.com/gibranlp/QARSlp/blob/main/screenshots/7.%20.png)
![8](https://github.com/gibranlp/QARSlp/blob/main/screenshots/8.%20.png)
![9](https://github.com/gibranlp/QARSlp/blob/main/screenshots/9.%20.png)
![10](https://github.com/gibranlp/QARSlp/blob/main/screenshots/10.%20.png)
![11](https://github.com/gibranlp/QARSlp/blob/main/screenshots/11.%20.png)
![12](https://github.com/gibranlp/QARSlp/blob/main/screenshots/12.%20.png)