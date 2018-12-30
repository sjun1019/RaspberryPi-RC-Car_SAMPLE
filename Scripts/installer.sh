###20181117
###20181230 updated

#!/bin/sh

echo "All password will change to 'samplepi'"

echo pi:samplepi | /usr/sbin/chpasswd

apt update

cd /home/pi

git clone https://github.com/sjun1019/RaspberryPi-RC-Car_SAMPLE.git

cd /home/pi/RaspberryPi-RC-Car_SAMPLE/Scripts

chmod +x controller.sh

yes|ln -i controller.sh /home/pi/Desktop/controller.sh

cd /home/pi/RaspberryPi-RC-Car_SAMPLE/Scripts/Resources

apt-get install -y ./opencv/OpenCV*.deb

apt-get install -y python3-dev

apt-get -y install tightvncserver

mkdir /home/pi/.vnc

cp passwd /home/pi/.vnc/passwd

vncserver -p /home/pi/.vnc/passwd

cp tightvnc /etc/init.d/tightvnc ; sudo -S chmod +x /etc/init.d/tightvnc ; sudo -S update-rc.d tightvnc defaults

sed -i "6s/#X-window-manager &/X-window-manager &/" /home/pi/.vnc/xstartup

CONFIG=/boot/config.txt

get_config_var() {
    lua - "$1" "$2" <<EOF
local key=assert(arg[1])
local fn=assert(arg[2])
local file=assert(io.open(fn))
local found=false
for line in file:lines() do
  local val = line:match("^%s*"..key.."=(.*)$")
  if (val ~= nil) then
    print(val)
    found=true
    break
  end
end
if not found then
   print(0)
end
EOF
}

set_config_var() {
    lua - "$1" "$2" "$3" <<EOF > "$3.bak"
local key=assert(arg[1])
local value=assert(arg[2])
local fn=assert(arg[3])
local file=assert(io.open(fn))
local made_change=false
for line in file:lines() do
  if line:match("^#?%s*"..key.."=.*$") then
    line=key.."="..value
    made_change=true
  end
  print(line)
end

if not made_change then
  print(key.."="..value)
end
EOF
 mv "$3.bak" "$3"
}

if [ ! -e /boot/start_x.elf ]; then
return 1
fi
 sed $CONFIG -i -e "s/^startx/#startx/"
 sed $CONFIG -i -e "s/^fixup_file/#fixup_file/"

set_config_var start_x 1 $CONFIG
CUR_GPU_MEM=$(get_config_var gpu_mem $CONFIG)
if [ -z "$CUR_GPU_MEM" ] || [ "$CUR_GPU_MEM" -lt 128 ]; then
    set_config_var gpu_mem 128 $CONFIG
fi

cat >> /etc/modules << EOF
bcm2835-v4l2
EOF

echo "Done.. reboot"

init 6
