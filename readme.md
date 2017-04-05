curl -L https://downloads.raspberrypi.org/raspbian_lite_latest > raspbian_lite_latest.zip
unzip raspbian_lite_latest.zip
diskutil unmountDisk /dev/disk4
sudo dd bs=1m if=2016-03-25-28r-lite.img of=/dev/disk4


# resize file system
raspi-config
apt-get update
apt-get install python-falcon
echo brighty > /etc/hosts
nohup sh -c "curl -L https://raw.githubusercontent.com/chrisdpa/noise/master/po.py | sudo python &"
