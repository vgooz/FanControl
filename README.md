# FanControl
Raspberry Pi FanControl Service

#### Enables fan/cooler that pluged in Raspberry Pi when CPU is too hot and disables it when CPU got cold.

#### Instruction how to install Fan Control python application as executable service for Raspberry Pi with OSMC

1. Download program and place it into /opt folder
```
sudo wget https://raw.githubusercontent.com/vgooz/FanControl/master/fancontrol.py /opt/fancontrol.py`
sudo chmod 774 /opt/fancontrol.py
```
2. Install GPIO python library for Python 2.7
```
sudo apt-get install build-essential
sudo pip install wheel
sudo apt-get install python-dev
sudo pip install rpi.gpio
```
3. Create fancontrol.service file with following text below
```
sudo nano /etc/systemd/system/fancontrol.service
[Unit]
Description=run fan when hot
After=meadiacenter.service
[Service]
#If User and Group are not specified, then by default systemd ExecStart runs as root
User=root
Group=root
Type=simple
ExecStart=/usr/bin/python /opt/fancontrol.py
ExecStop=/usr/bin/pkill -f /opt/fancontrol.py
Restart=always
[Install]
WantedBy=multi-user.target
```
4. Register and enable FanControl service
```
sudo systemctl enable fancontrol
sudo systemctl start fancontrol
sudo systemctl status fancontrol
```
5. Use sysbench for CPU hiting
```
sudo apt-get install sysbench
sysbench --num-threads=4 --test=cpu --cpu-max-prime=200000 --validate run
```
