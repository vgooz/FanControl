# FunControl
Raspberry Pi FunControl Service

#### Instruction how to install Fun Control python application as executable service for Raspberry Pi with OSMC

1. Download program and place it into /opt folder
```
sudo wget https://raw.githubusercontent.com/vgooz/FunControl/master/funcontrol.py /opt/funcontrol.py`
sudo chmod 774 /opt/funcontrol.py
```
2. Install GPIO python library for Python 2.7
```
sudo apt-get install build-essential
sudo pip install wheel
sudo apt-get install python-dev
sudo pip install rpi.gpio
```
3. Create funcontrol.service file with following text below
```
sudo nano /etc/systemd/system/funcontrol.service
[Unit]
Description=run fan when hot
After=meadiacenter.service
[Service]
#If User and Group are not specified, then by default systemd ExecStart runs as root
User=root
Group=root
Type=simple
ExecStart=/usr/bin/python /opt/funcontrol.py
ExecStop=/usr/bin/pkill -f /opt/funcontrol.py
Restart=always
[Install]
WantedBy=multi-user.target
```
4. Register and enable FunControl service
```
sudo systemctl enable funcontrol
sudo systemctl start funcontrol
sudo systemctl status funcontrol
```
5. Use sysbench for CPU hiting
```
sudo apt-get install sysbench
sysbench --num-threads=4 --test=cpu --cpu-max-prime=200000 --validate run
```
