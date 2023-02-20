#!/bin/bash

# #!/bin/bash
#
# # Get the PID of the active window
# pid=$(xdotool getactivewindow getwindowpid)
#
# # Get the name of the process associated with the active window
# process_name=$(cat /proc/$pid/comm)
#
# # Check if the process name matches a supported browser
# if [ "$process_name" = "firefox" ]; then
#   # Get the URL of the active tab in Firefox
#   url=$(xdotool search --pid "$pid" --class "Firefox" getwindowname | awk -F ' - ' '{print $1}')
#
# elif [ "$process_name" = "chromium" ]; then
#   # Get the URL of the active tab in Chromium
#   url=$(xdotool search --pid "$pid" --class "Chromium" getwindowname | awk -F ' - ' '{print $2}')
#   newurl=$(curl -s localhost:4695/json/version | jq -r '.[].webSocketDebuggerUrl' | xargs -I {} curl -s {}/json/activate | jq -r '."url"')
#
# else
#   # Return an error message if the browser is not supported
#   echo "Error: unsupported browser ($process_name)" >&2
#   exit 1
#
# fi

file=/home/ephantus/chess_data/games.txt

# check how many lines $file currently has.
lines_in_file=`cat $file | wc -l`

args=`xclip -selection clipboard -o`

# Reads whatever is in the clipboard and appends it in the games.txt file.

echo "$args" >> $file


last_line=`tail -1 $file`

new_lines=`cat $file | wc -l`

if [ "$new_lines" -ge "$lines_in_file" ]; then

    # we will need to check if a game was added by using a notify-send
    notify-send "Added a game" "Game $last_line was added..."

fi

