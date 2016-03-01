# read a sql dump into a db
zcat /path/to/file.sql.gz | mysql -u 'root' -p your_database

mysqldump -P 3306 -h servername.local -u username -p database_name>database_name.sql
cat database_name.sql | mysql -u 'root' -p database_name

# Android: getting app names and downloadig app.apk package
adb shell pm list packages
adb shell pm list packages | grep myapp
adb shell pm path org.name.of.app
adb pull /data/app/bla.apk

# show network connections, traffic, programms and pids
sudo nethogs wlan0

#switch default language in dual audio files
find . -name "*.mkv" -exec mkvpropedit {} --edit track:a1 --set flag-default=0 --edit track:a2 --set flag-default=1 --edit track:s1 --set flag-default=0 --edit track:s2 --set flag-default=1 \;

mkvpropedit myfile.mkv --edit track:a1 --set flag-default=0 --edit track:a2 --set flag-default=1

#list listening processes with executing app
sudo netstat -tulpn


# Docker commands
sudo docker exec -it 49cfc7b12191 bash