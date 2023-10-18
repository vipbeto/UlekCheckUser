#!/bin/bash
set -x
apt update && apt upgrade -y && apt install python3 git -y
git clone https://github.com/UlekBR/UlekCheckUser.git
chmod +x /root/UlekCheckUser/checkuserMenu.sh
ln -s /root/UlekCheckUser/checkuserMenu.sh /usr/local/bin/ulekCheckuser

