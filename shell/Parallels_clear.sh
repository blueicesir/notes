#!/bin/bash
#!/bin/bash
PASSWORD=你的root 密码
rm -rf ~/Library/Preferences/com.parallels.*
rm -rf ~/Library/Preferences/Parallels/
echo $PASSWORD | sudo -S rm -rf /Library/Preferences/Parallels/licenses.xml
echo "del /Library/Preferences/Parallels/licenses.xml ok!"
echo $PASSWORD | sudo -S rm -rf /private/var/db/Parallels/
echo "del /private/var/db/Parallels/ ok!"
echo $PASSWORD | sudo -S rm -rf /private/var/.Parallels_swap/
echo "del /private/var/.Parallels_swap/ ok!"
echo $PASSWORD | sudo -S rm -rf /private/var/root/Library/Preferences/com.parallels.*
echo "del /private/var/root/Library/Preferences/com.parallels.* ok!"
dscacheutil -flushcache
exit 



# other version 
rm -rfd /users/~you~/library/preferences/com.parallels*
rm -rfd /users/~you~/library/preferences/parallels/*
rm -rfd /users/~you~/library/preferences/parallels
sudo -s rm -rfd /private/var/db/parallels/stats/*
sudo -s rm -rfd /private/var/db/parallels/stats
sudo -s rm -rfd /private/var/db/parallels
sudo -s rm -rfd /library/logs/parallels.log
sudo -s rm -rfd /library/preferences/parallels/*
sudo -s rm -rfd /library/preferences/parallels
sudo -s rm -rfd /private/var/db/parallels
sudo -s rm -rfd /private/var/.parallels_swap
sudo -s rm -rfd /private/var/db/receipts/com.parallels*’
sudo -s rm -rfd /private/tmp/qtsingleapp-*-lockfile
sudo -s rm -rfd /private/tmp/com.apple.installer*/*
sudo -s rm -rfd /private/tmp/com.apple.installer*
sudo -s rm -rfd /private/var/root/library/preferences/com.parallels.desktop.plist
dscacheutil -flushcache
sudo rm -fr ~/Library/Logs/parallels.log
sudo rm -fr /Library/Preferences/Parallels/
sudo rm -fr ~/Library/Preferences/Parallels
sudo rm -fr /private/var/.Parallels_swap
sudo rm -fr /private/var/db/Parallels/Stats
sudo rm -fr /private/tmp/qtsingleapp-Parall-c0ce-0-lockfile
sudo rm -fr ~/Library/Preferences/com.parallels 


