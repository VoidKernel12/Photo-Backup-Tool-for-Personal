#!/bin/bash

# ANSI Colors
GREEN='\033[92m'
CYAN='\033[96m'
RED='\033[91m'
RESET='\033[0m'

clear
echo -e "${CYAN}[+] Updating package lists...${RESET}"
pkg update -y && pkg upgrade -y

echo -e "${CYAN}[+] Installing Python and Git...${RESET}"
pkg install python git -y

echo -e "${CYAN}[+] Installing required Python libraries (pyfiglet)...${RESET}"
pip install pyfiglet

echo -e "${GREEN}[✔] Installation Completed Successfully!${RESET}"
echo -e "${YELLOW}[!] Run the tool using: python tool.py${RESET}"
