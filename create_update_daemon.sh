#!/usr/bin/bash

#create cert folder
mkdir -p /home/aetech/raspi-http/EcuDebugCtrl/certs
cd /home/aetech/raspi-http/EcuDebugCtrl/certs
#generate cert
#openssl ecparam -genkey -name prime256v1 -noout -out key.pem
#openssl req -new -x509 -key key.pem -out cert.pem -days 365

cd ..
sudo cp ecudebugcontrol.service /etc/systemd/system/
sudo systemctl daemon-reload 
sudo systemctl enable ecudebugcontrol.service 
sudo systemctl start ecudebugcontrol.service 
sudo systemctl status ecudebugcontrol.service 
