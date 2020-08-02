- Update & upgrade
```bash
sudo apt update
sudo apt upgrade -y
```

- System information
```bash
uname -a
# Linux ubuntu-vm-2 5.3.0-1032-gcp #34~18.04.1-Ubuntu SMP Tue Jul 14 22:07:36 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
sudo lshw  # hardware information
```

- Disable touch screen on ubuntu 18.04 xps 15 
```bash
xinput --list  # your touchscreen XID
xinput disable [touchscreen XID]
```

- System restart
```bash
sudo reboot
```

- Create tar archive
```bash
tar -zcvf tar-archive-name.tar.gz source-folder-name
```

- Start VNC Server
```bash
#vncserver -localhost no -geometry 3200x1800 -depth 16 # for hi-res
vncserver -localhost no -geometry 1900x1100 -depth 16
```

- Download from site path 
```bash
wget -xr -np <site path>
```
  
- Restart pulseaudio and alsa
```bash
pulseaudio -k
sudo alsa force-reload
pulseaudio --start
```
