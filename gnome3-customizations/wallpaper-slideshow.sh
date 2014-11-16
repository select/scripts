#!/bin/bash
# http://superuser.com/a/298182/390452
# 
# open 
# gnome-session-properties
# and add this script
#
WP_DIR=/home/YourUserName/Pictures/wallpaper

cd $WP_DIR
while [ 1 ] 
  do
  set -- * 
  length=$#
  random_num=$((( $RANDOM % ($length) ) + 1)) 

  gsettings set org.gnome.desktop.background picture-uri "file://$WP_DIR/${!random_num}"
  # gsettings set org.gnome.desktop.background show-desktop-icons true # had to set this to true once or it did not update
  # gsettings set org.gnome.desktop.background picture-options 'zoom' # you can also set this in the gnome tweak tool
  # echo 'switched wallpaper'
  sleep 600 # 10 minutes, this value is in seconds
done