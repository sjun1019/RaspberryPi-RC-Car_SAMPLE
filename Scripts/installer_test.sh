###20181117
###20181230 updated

#!/bin/sh

echo 'samplepi' | sudo -S apt update

cd /home/pi

git clone -b dev https://github.com/sjun1019/RaspberryPi-RC-Car_SAMPLE.git

cd /home/pi/RaspberryPi-RC-Car_SAMPLE/Scripts

chmod +x controller.sh

yes|ln -s controller.sh /home/pi/Desktop/controller.sh

cd /home/pi/RaspberryPi-RC-Car_SAMPLE/Scripts/Resources

echo 'samplepi' | sudo -S apt-get install -y ./opencv/OpenCV*.deb

echo 'samplepi' | sudo -S apt-get -y install tightvncserver

PASSWORD="samplepi"
DISPLAY=":1"
VNCSERVER_OPTIONS="-geometry 1280x960 -alwaysshared"
PASSWD_PATH="$HOME/.vnc/passwd"
XSTARTUP_PATH="$HOME/.vnc/xstartup"
VNCSERVER="tightvncserver"
VNCPASSWD="tightvncpasswd"
# NOTE: you can change `tightvncpasswd` by `vncpasswd` if you don't use
#       TightVNC but it won't work in some VNC implementations
NEW_SESSION="exec gnome-session"

vncserver_stop() {
    # Kill server for this display if is running
    $VNCSERVER -clean -kill $DISPLAY
}

vncserver_start() {
    echo "$PASSWORD" | $VNCPASSWD -f > $PASSWD_PATH
    chmod 600 $PASSWD_PATH
    echo "$NEW_SESSION" > $XSTARTUP_PATH
    $VNCSERVER $DISPLAY $VNCSERVER_OPTIONS
}

case "$1" in
    start)
        vncserver_start
    ;;

    stop)
        vncserver_stop
    ;;

    restart)
        vncserver_stop
        vncserver_start
    ;;

    *)
        echo "Usage: $0 <start|stop|restart>"
esac

sed -i "6s/#X-window-manager &/X-window-manager &/" ~/.vnc/xstartup

echo 'samplepi' |  -S chmod +x /etc/init.d/tightvnc ; sudo -S update-rc.d tightvnc defaults

#echo 'samplepi' | sudo -S init 6