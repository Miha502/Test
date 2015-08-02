netsh int ip set address "Local Aea Cnnection" static 192.168.254.15 255.255.0.0 192.168.254.1
netsh interface ip set dns "Local Area Connection" static 8.8.8.8
net int ip show config
pause
