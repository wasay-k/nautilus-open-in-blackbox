# OpenInBlackBox

<p>Simple script to open BlackBox terminal from within Nautilus.
Fork of <a href="https://github.com/cargocats/nautilus-open-in-ptyxis/">nautilus-open-in-ptyxis</a>

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
Restart Nautilus
```
nautilus -q
```
Clone this repository and use the install script.
```
git clone https://github.com/wasay-k/nautilus-open-in-blackbox.git
cd nautilus-open-in-blackbox
sudo ./install.sh
```
