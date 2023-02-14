# Get the ID of the active window
window_id=$(xdotool getactivewindow)

# Get the name of the active window
window_name=$(xdotool getwindowname $window_id)

# Check if the window name contains "Mozilla Firefox"
if echo "$window_name" | grep -q "Mozilla Firefox"; then
  # Extract the URL query using the browser extension
  url=$(curl -s "http://localhost:8282/tabcenter/tab?id=$window_id" | jq -r .url)

elif echo "$window_name" | grep -q "Chromium"; then
    url=$(curl -s localhost:4660/json/version | jq -r '.[].webSocketDebuggerUrl' | xargs -I {} curl -s {}/json/activate | jq -r '."url"')
    notify-send "url is $url"
else
  echo "Error: unsupported browser" >&2
  exit 1
fi
