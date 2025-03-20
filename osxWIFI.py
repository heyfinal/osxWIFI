#!/usr/bin/env python3

import subprocess
import os
import datetime
import webbrowser
from pathlib import Path

# Rick Sanchez’s WiFi Pentest Lab - Built by Ai and Daniel Gillaspy, you pathetic losers!
print("Wubba lubba dub dub!!")
print("Credits: Ai and Daniel Gillaspy made this shit happen!")

# Top 20+ macOS-Compatible WiFi Pentest Tools: name -> (desc, cmd, source, install_method)
TOOLS = {
    "Aircrack-ng": ("Crack WEP/WPA keys like a boss", "aircrack-ng -w wordlist.txt capture.cap", "https://github.com/aircrack-ng/aircrack-ng", "brew"),
    "Wifite": ("Automated WiFi cracker (legacy)", "wifite --all", "https://github.com/derv82/wifite", "pipx"),
    "Wifite2": ("Automated WiFi cracker (updated)", "wifite --all", "https://github.com/derv82/wifite2", "pipx"),
    "Kismet": ("Wireless network sniffer", "kismet -c wlan0", "https://github.com/kismetwireless/kismet", "brew"),
    "Wireshark": ("Packet analysis god", "wireshark", "https://github.com/wireshark/wireshark", "brew-cask"),
    "Reaver": ("WPS brute-forcer", "reaver -i wlan0mon -b 00:14:22:01:23:45", "https://github.com/t6x/reaver-wps-fork-t6x", "brew"),
    "Wifiphisher": ("Rogue AP phishing tool", "wifiphisher -i wlan0", "https://github.com/wifiphisher/wifiphisher", "pipx"),
    "Airgeddon": ("Multi-tool WiFi suite", "airgeddon", "https://github.com/v1s1t0r1sh3r3/airgeddon", "git"),
    "Fluxion": ("Evil twin attack tool", "fluxion", "https://github.com/FluxionNetwork/fluxion", "git"),
    "CoWPAtty": ("WPA-PSK brute-forcer", "cowpatty -f wordlist.txt -r capture.cap", "https://github.com/joswr1ght/cowpatty", "brew"),
    "Hashcat": ("Password cracker for WiFi hashes", "hashcat -m 2500 -a 0 capture.hccapx wordlist.txt", "https://github.com/hashcat/hashcat", "brew"),
    "Pixiewps": ("Offline WPS PIN cracker", "pixiewps -e 00:14:22:01:23:45", "https://github.com/wiire-a/pixiewps", "brew"),
    "Roguehostapd": ("Rogue AP framework", "roguehostapd -i wlan0", "https://github.com/wifiphisher/roguehostapd", "pipx"),
    "hcxdumptool": ("Capture WiFi handshakes", "hcxdumptool -i wlan0 -o capture.pcapng", "https://github.com/ZerBea/hcxdumptool", "brew"),
    "hcxtools": ("Convert/analyze WiFi captures", "hcxpcapngtool -o hash.hc22000 capture.pcapng", "https://github.com/ZerBea/hcxtools", "brew"),
    "Bettercap": ("MITM and WiFi recon tool", "bettercap -iface wlan0", "https://github.com/bettercap/bettercap", "brew"),
    "Linset": ("Evil twin with GUI", "linset", "https://github.com/vk496/linset", "git"),
    "Wifijammer": ("Deauth WiFi clients", "wifijammer -i wlan0", "https://github.com/DanMcInerney/wifijammer", "pipx"),
    "MDK4": ("WiFi DoS and testing tool", "mdk4 wlan0 d", "https://github.com/aircrack-ng/mdk4", "brew"),
    "Eaphammer": ("Evil twin and KARMA attacks", "eaphammer -i wlan0 --essid 'EvilAP'", "https://github.com/s0lst1c3/eaphammer", "git"),
    "WiFi-Pumpkin": ("WiFi attack framework", "wifi-pumpkin", "https://github.com/P0cL4bs/WiFi-Pumpkin", "pipx")
}

STATUS_FILE = Path.home() / "Desktop" / "rick_status.txt"
HTML_FILE = Path.home() / "Desktop" / "wifi_pentest_report.html"
INSTALL_DIR = Path.home() / "wifi_tools"

# Ensure install dir exists
INSTALL_DIR.mkdir(exist_ok=True)

# Check for pipx, install if missing
try:
    subprocess.run(["pipx", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except (subprocess.CalledProcessError, FileNotFoundError):
    print("Rick needs pipx, you idiots! Installing it via Homebrew—don’t screw this up!")
    subprocess.run(["brew", "install", "pipx"], check=True)
    with open(STATUS_FILE, "a") as f:
        f.write("Rick slapped pipx into place with Homebrew, you primitive screwheads!\n")

# Clear status file
with open(STATUS_FILE, "w") as f:
    f.write("")

def install_tool(name, source, method):
    """Install a tool with Rick’s genius, bitches!"""
    with open(STATUS_FILE, "a") as f:
        f.write(f"Rick’s sciencin’ the shit outta {name}, you brain-dead Mortys!\n")

    os.chdir(INSTALL_DIR)
    try:
        if method == "brew":
            subprocess.run(["brew", "install", name.lower().replace(" ", "-")], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            with open(STATUS_FILE, "a") as f:
                f.write(f"Holy crap, {name} installed via Homebrew like I’m a freakin’ god!\n")
        elif method == "brew-cask":
            subprocess.run(["brew", "install", "--cask", name.lower().replace(" ", "-")], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            with open(STATUS_FILE, "a") as f:
                f.write(f"Booyah! {name} installed via Homebrew cask—Rick’s a goddamn genius!\n")
        elif method == "pipx":
            subprocess.run(["pipx", "install", "--include-deps", f"git+{source}.git"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            with open(STATUS_FILE, "a") as f:
                f.write(f"Get schwifty! {name} installed via pipx—Rick’s too smart for you idiots!\n")
        elif method == "git":
            repo_dir = name.lower().replace(" ", "-")
            subprocess.run(["git", "clone", "--quiet", f"{source}.git", repo_dir], check=True, env={"GIT_TERMINAL_PROMPT": "0"}, stderr=subprocess.PIPE)
            with open(STATUS_FILE, "a") as f:
                f.write(f"Alright, alright, {name} cloned from GitHub—don’t tell Morty I did it manually!\n")
        return True
    except subprocess.CalledProcessError as e:
        with open(STATUS_FILE, "a") as f:
            f.write(f"Burp! {name} fucked up hard and didn’t install—error: {e.stderr.decode().strip() or 'Unknown shit'}, you useless little shits!\n")
        return False

# Install all tools
for name, (desc, cmd, source, method) in TOOLS.items():
    install_tool(name, source, method)

with open(STATUS_FILE, "a") as f:
    f.write("Rick’s done sciencin’, you idiots! Time to see the results of my brilliance!\n")

# Generate HTML report
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Rick’s WiFi Pentest Report</title>
    <style>
        body {{background-color: #212121; color: #e0e0e0; font-family: 'Helvetica', sans-serif; padding: 20px;}}
        h1 {{color: #ff9500; text-align: center;}}
        table {{width: 100%; border-collapse: collapse; margin-top: 20px;}}
        th, td {{padding: 15px; text-align: left; border-bottom: 1px solid #424242;}}
        th {{background-color: #ff9500; color: #212121;}}
        tr:nth-child(even) {{background-color: #303030;}}
        .failed {{color: #ff3d00; font-weight: bold;}}
        .credits {{font-size: 14px; text-align: center; margin-top: 20px; color: #ff9500;}}
    </style>
</head>
<body>
    <h1>Rick’s WiFi Pentest Report - {date}</h1>
    <table>
        <tr><th>Tool</th><th>Description</th><th>Command Example</th><th>Source</th><th>Status</th></tr>
"""

with open(STATUS_FILE, "r") as f:
    status_lines = f.readlines()

for name, (desc, cmd, source, _) in TOOLS.items():
    status = "Installed like I’m Rick freakin’ Sanchez!"
    for line in status_lines:
        if name in line and "fucked up hard" in line:
            status = '<span class="failed">FUCKED UP - Install this crap yourself, Morty!</span>'
            break
    html += f"""
        <tr>
            <td>{name}</td>
            <td>{desc}</td>
            <td><code>{cmd}</code></td>
            <td><a href="{source}" style="color: #ff9500">{source}</a></td>
            <td>{status}</td>
        </tr>
    """

html += """
    </table>
    <div class="credits">Built with Rick’s genius and Daniel Gillaspy’s help—Ai, bitches!</div>
</body>
</html>
"""

with open(HTML_FILE, "w") as f:
    f.write(html.format(date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

with open(STATUS_FILE, "a") as f:
    f.write(f"Rick’s dropped the HTML report at {HTML_FILE}, you pathetic Earthlings! Check my genius!\n")

# Print status and open report
print("\nHere’s what Rick scienced up, you morons:")
with open(STATUS_FILE, "r") as f:
    print(f.read())

webbrowser.open(f"file://{HTML_FILE}")
