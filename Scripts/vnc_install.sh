#!/bin/sh

echo 'raspberrypi' | sudo -S apt-get install tightvncserver

echo -e "samplepi\n samplepi\n n\n" | vncserver

sed -i "6s/#X-window-manager &/X-window-manager &/" ~/.vnc/xstartup

echo 'raspberrypi' | sudo -S cp tightvnc /etc/init.d/tightvnc && sudo -S chmod +x /etc/init.d/tightvnc && sudo -S update-rc.d tightvnc defaults && sudo -S init 6

