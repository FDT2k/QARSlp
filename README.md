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

# Features

## Qtile changes with the wallpapers colors.

![Wallpaper 1](https://github.com/gibranlp/QARSlp/blob/main/screenshots/walls/Sc_2021-12-09_1920x1080.png)
![Wallpaper 1](https://github.com/gibranlp/QARSlp/blob/main/screenshots/walls/Sc_2021-12-22_1920x1080.png)
![Wallpaper 1](https://github.com/gibranlp/QARSlp/blob/main/screenshots/walls/Sc_2021-12-36_1920x1080.png)
![Wallpaper 1](https://github.com/gibranlp/QARSlp/blob/main/screenshots/walls/Sc_2021-12-38_1920x1080.png)
![Wallpaper 1](https://github.com/gibranlp/QARSlp/blob/main/screenshots/walls/Sc_2021-12-41_1920x1080.png)
![Wallpaper 1](https://github.com/gibranlp/QARSlp/blob/main/screenshots/walls/Sc_2021-12-53_1920x1080.png)

### More Awesome Wallpapers
- [x] Packs of wallpapers
  - [x] [Pack 1](https://gibranlp.dev/wallpacks/pack1.tar.gz)
  - [x] [Pack 2](https://gibranlp.dev/wallpacks/pack2.tar.gz)
  - [x] [Pack 3](https://gibranlp.dev/wallpacks/pack3.tar.gz)
  - [x] All the wallpapers should be on **~/Pictures/wallPapers** This folder is created with the installation.

## Widgets ![Rofi](https://github.com/davatorium/rofi) based

### Aplications Launcher

![Launcher](https://github.com/gibranlp/QARSlp/blob/main/screenshots/widgets/launcher.png)

### Color Scheme Selector

- [x] Same Wallpaper different Color Schemes

![Color Selector](https://github.com/gibranlp/QARSlp/blob/main/screenshots/widgets/color_scheme_selector.png)

### Dark Themes

![Color Selector](https://github.com/gibranlp/QARSlp/blob/main/screenshots/schemes/wal.png)
![Color Selector](https://github.com/gibranlp/QARSlp/blob/main/screenshots/schemes/colorz.png)
![Color Selector](https://github.com/gibranlp/QARSlp/blob/main/screenshots/schemes/colorthief.png)
![Color Selector](https://github.com/gibranlp/QARSlp/blob/main/screenshots/schemes/wal.png)


### Light Themes

![Color Selector](https://github.com/gibranlp/QARSlp/blob/main/screenshots/schemes/light-wal.png)
![Color Selector](https://github.com/gibranlp/QARSlp/blob/main/screenshots/schemes/light-colorz.png)
![Color Selector](https://github.com/gibranlp/QARSlp/blob/main/screenshots/schemes/light-colorthief.png)
![Color Selector](https://github.com/gibranlp/QARSlp/blob/main/screenshots/schemes/light-wal.png)


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

- [x] Firefox requires the [**Pywalfox**](https://addons.mozilla.org/en-US/firefox/addon/pywalfox/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search) plugin installed.

### Vscode
![Vscode](https://github.com/gibranlp/QARSlp/blob/main/screenshots/apps/6.png)
![Vscode](https://github.com/gibranlp/QARSlp/blob/main/screenshots/apps/16.png)

- [x] Vscode Requires the **Wal Theme** Plugin Installed.

### Libre Office
![Libre Office](https://github.com/gibranlp/QARSlp/blob/main/screenshots/apps/8.png)

# Screenshots


<a href="https://www.buymeacoffee.com/gibranlp"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a Coffee&emoji=&slug=gibranlp&button_colour=FFDD00&font_colour=000000&font_family=Bree&outline_colour=000000&coffee_colour=ffffff"></a>