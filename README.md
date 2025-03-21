
# osxWIFI

[![Python](https://img.shields.io/badge/Python-100%25-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![macOS](https://img.shields.io/badge/macOS-Compatible-green?style=for-the-badge&logo=apple)](https://www.apple.com/macos/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![HitCount](https://hits.dwyl.com/heyfinal/osxWIFI.svg?style=for-the-badge)](https://hits.dwyl.com/heyfinal/osxWIFI)

## PickleRick’s WiFi Pentest Lab

Welcome to the ultimate WiFi penetration testing toolkit for macOS. Built by none other than Rick Sanchez and Daniel Gillaspy. If you’re looking to crack WiFi networks with style and efficiency, you’ve come to the right place.

## Tools Included

Here's a list of the top macOS-compatible WiFi pentest tools included in this project. Each tool is accompanied by a brief description, a common command, and its source.

| Tool         | Description                             | Command Example                                        | Source                                                      | Install Method |
|--------------|-----------------------------------------|--------------------------------------------------------|-------------------------------------------------------------|----------------|
| Aircrack-ng  | Crack WEP/WPA keys like a boss          | `aircrack-ng -w wordlist.txt capture.cap`              | [Aircrack-ng](https://github.com/aircrack-ng/aircrack-ng)    | brew           |
| Wifite       | Automated WiFi cracker (legacy)         | `wifite --all`                                         | [Wifite](https://github.com/derv82/wifite)                   | pipx           |
| Wifite2      | Automated WiFi cracker (updated)        | `wifite --all`                                         | [Wifite2](https://github.com/derv82/wifite2)                 | pipx           |
| Kismet       | Wireless network sniffer                | `kismet -c wlan0`                                      | [Kismet](https://github.com/kismetwireless/kismet)           | brew           |
| Wireshark    | Packet analysis god                     | `wireshark`                                            | [Wireshark](https://github.com/wireshark/wireshark)          | brew-cask      |
| Reaver       | WPS brute-forcer                        | `reaver -i wlan0mon -b 00:14:22:01:23:45`              | [Reaver](https://github.com/t6x/reaver-wps-fork-t6x)         | brew           |
| Wifiphisher  | Rogue AP phishing tool                  | `wifiphisher -i wlan0`                                 | [Wifiphisher](https://github.com/wifiphisher/wifiphisher)    | pipx           |
| Airgeddon    | Multi-tool WiFi suite                   | `airgeddon`                                            | [Airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon)      | git            |
| Fluxion      | Evil twin attack tool                   | `fluxion`                                              | [Fluxion](https://github.com/FluxionNetwork/fluxion)         | git            |
| CoWPAtty     | WPA-PSK brute-forcer                    | `cowpatty -f wordlist.txt -r capture.cap`              | [CoWPAtty](https://github.com/joswr1ght/cowpatty)            | brew           |
| Hashcat      | Password cracker for WiFi hashes        | `hashcat -m 2500 -a 0 capture.hccapx wordlist.txt`     | [Hashcat](https://github.com/hashcat/hashcat)                | brew           |
| Pixiewps     | Offline WPS PIN cracker                 | `pixiewps -e 00:14:22:01:23:45`                        | [Pixiewps](https://github.com/wiire-a/pixiewps)              | brew           |
| Roguehostapd | Rogue AP framework                      | `roguehostapd -i wlan0`                                | [Roguehostapd](https://github.com/wifiphisher/roguehostapd)  | pipx           |
| hcxdumptool  | Capture WiFi handshakes                 | `hcxdumptool -i wlan0 -o capture.pcapng`               | [hcxdumptool](https://github.com/ZerBea/hcxdumptool)         | brew           |
| hcxtools     | Convert/analyze WiFi captures           | `hcxpcapngtool -o hash.hc22000 capture.pcapng`         | [hcxtools](https://github.com/ZerBea/hcxtools)               | brew           |
| Bettercap    | MITM and WiFi recon tool                | `bettercap -iface wlan0`                               | [Bettercap](https://github.com/bettercap/bettercap)          | brew           |
| Linset       | Evil twin with GUI                      | `linset`                                               | [Linset](https://github.com/vk496/linset)                    | git            |
| Wifijammer   | Deauth WiFi clients                     | `wifijammer -i wlan0`                                  | [Wifijammer](https://github.com/DanMcInerney/wifijammer)     | pipx           |
| MDK4         | WiFi DoS and testing tool               | `mdk4 wlan0 d`                                         | [MDK4](https://github.com/aircrack-ng/mdk4)                  | brew           |
| Eaphammer    | Evil twin and KARMA attacks             | `eaphammer -i wlan0 --essid 'EvilAP'`                  | [Eaphammer](https://github.com/s0lst1c3/eaphammer)           | git            |
| WiFi-Pumpkin | WiFi attack framework                   | `wifi-pumpkin`                                         | [WiFi-Pumpkin](https://github.com/P0cL4bs/WiFi-Pumpkin)      | pipx           |

## Installation

  ### Install Homebrew
  Open your terminal and run the following command to install Homebrew:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

  ### Install pipx
  Once Homebrew is installed, you can install pipx with the following command:

```sh
brew install pipx
pipx ensurepath
```

  This ensures that pipx's binary directory is added to your PATH. You might need to restart your terminal for the changes to take effect.
  To install all the tools, simply run the script and let Rick’s genius do the work for you. 

```shell
chmod +x osxWIFI.py
./osxWIFI.py
```

## Usage

Each tool comes with its own set of commands. Post installation will provide a html report with some commands & links to tools source..  Here are a few commonly used commands to get you started:

```shell
# Crack WEP/WPA keys with Aircrack-ng
aircrack-ng -w wordlist.txt capture.cap

# Automated WiFi cracking with Wifite
wifite --all

# Packet analysis with Wireshark
wireshark
```

## Contributing

Feel free to contribute to this project by submitting a pull request. Your contributions are always welcome.

## License

This project is not licenced & provides no warrenty, use code as you see fit.

## Connect with Us

[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/danielgillaspy?igsh=MWRjeXJnOXo5aXhkYg%3D%3D&utm_source=qr)
[![Email](https://img.shields.io/badge/Email-daniel@gillaspy.me-blue?style=for-the-badge&logo=gmail&logoColor=white)](mailto:daniel@gillaspy.me)

---

Built with PickleRick’s genius and Daniel Gillaspy’s help—Ai, bitches!
