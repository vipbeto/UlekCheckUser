#!/bin/bash
set -x
apt update && apt upgrade -y && apt install python3 git -y
git clone https://github.com/UlekBR/UlekCheckUser.git
chmod +x /root/UlekCheckuser/checkuserMenu.sh
sudo ln -s /root/UlekCheckuser/checkuserMenu.sh /usr/local/bin/ulekCheckuser

