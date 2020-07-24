- Create tar archive
```bash
tar -zcvf tar-archive-name.tar.gz source-folder-name
```

- Start VNC Server
```
#vncserver -localhost no -geometry 3200x1800 -depth 16 # for hi-res
vncserver -localhost no -geometry 1900x1100 -depth 16
```

- download from site path 
```
wget -xr -np <site path>
```
  
- restart pulseaudio and alsa
```
pulseaudio -k
sudo alsa force-reload
pulseaudio --start
```
