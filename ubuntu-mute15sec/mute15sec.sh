# mute
pactl set-sink-mute 0 1
# wait 15 seconds
sleep 15
# unmute
pactl set-sink-mute 0 0
# create a keyboad shortcut for this script in gnome with
# 1 Open the Activities overview and start typing Keyboard.
# 2 Click on Keyboard to open the panel.
# 3 Select the Shortcuts tab.
# 4 Custom Shortcuts, create an new shortcut name: mute 15 command:/path/to/mute15sec.sh
# 5 click on disable and punch the keyboad shortcut you want to have it under mine is ctrl+alt+m