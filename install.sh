#!/bin/bash
vermelho="\e[31m"
verde="\e[32m"
amarelo="\e[33m"
azul="\e[34m"
roxo="\e[38;2;128;0;128m"
reset="\e[0m"

rm -rf /root/UlekCheckUser/
rm -f /usr/local/bin/ulekCheckuser
pkill -9 -f "/root/UlekCheckUser/checkuser.py"

apt update && apt upgrade -y && apt install python3 git -y
git clone https://github.com/UlekBR/UlekCheckUser.git
chmod +x /root/UlekCheckUser/checkuserMenu.sh
ln -s /root/UlekCheckUser/checkuserMenu.sh /usr/local/bin/ulekCheckuser

clear
echo -e "Para iniciar o menu digite: ${verde}ulekCheckuser${reset}"
