!#/usr/bin/bash

sudo cp ecudebugcontrol.service /etc/systemd/system/
sudo systemctl daemon-reload 
sudo systemctl enable ecudebugcontrol.service 
sudo systemctl start ecudebugcontrol.service 
sudo systemctl status ecudebugcontrol.service 
