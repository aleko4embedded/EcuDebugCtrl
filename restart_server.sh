# Reload systemd unit definitions (only needed if you changed the .service file itself)
sudo systemctl daemon-reload  

# Restart your Flask service
sudo systemctl restart ecudebugcontrol.service

# Check if it's running without errors
sudo systemctl status ecudebugcontrol.service

