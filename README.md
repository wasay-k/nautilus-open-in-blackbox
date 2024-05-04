# OpenInPtyxis

<p>Simple script to open my favorite terminal <a href="https://gitlab.gnome.org/chergert/ptyxis">Ptyxis</a> from Nautilus (Gnome Files) Menu</p>

## Dependency
`nautilus-python`( `python-nautilus` on Debian/Ubuntu based)
### Ubuntu
```
sudo apt install python3-nautilus
```
### Fedora
```
sudo dnf install nautilus-python
```

## Installation

### Arch Linux
Install from AUR
```
yay -S nautilus-open-in-ptyxis
```
Restart Nautilus
```
nautilus -q
```

### Other Disto

Clone this repository and use the install script.
```
git clone https://github.com/GustavoWidman/nautilus-open-in-ptyxis.git
cd nautilus-open-in-ptyxis
sudo ./install.sh
```
