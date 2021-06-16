- Run as windows service
```
nssm.exe install "<my service>" "path\to\<my service>.bat"

nssm.exe <start|restart|status> "<my service>"
nssm.exe <stop|remove> "<my service>"
```

- SSH Server on Windows 10

  You can install OpenSSH Server by launching Windows Settings and then navigating to Apps > Optional features, clicking Add a feature, selecting OpenSSH Server, and clicking Install.
  launched PowerShell as Administrator, and entered the following commands to see the status of the service, start the service, and then verify that the service was running:

```ps
Get-Service sshd # ← sshd is the OpenSSH service
Start-Service sshd # ← Starts the sshd service
Get-Service sshd  # ← Verifies that the sshd service is running

# As I wanted the SSH service to start every time the system booted up, I entered:
Set-Service -Name sshd -StartupType 'Automatic'

# To check and make sure that the port for the SSH server was open, I entered:
Get-NetFirewallRule -Name *ssh*

# If you have any other firewall or security tools running, you will also need to configure them to allow for SSH connections.
# I then checked that my SSH server was operational by connecting to the Windows system that I was currently on by going back to the command console and entering:
ssh user@localhost
ssh user@hostip

# Finally, I verified that I was able to copy a file from a remote system to my local system by entering:
scp user@10.0.0.167:/TestFile CopyOfFile
```


