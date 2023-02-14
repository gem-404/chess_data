#!/usr/bin/env python3

# import dbus
#
# # Connect to the session bus
# session_bus = dbus.SessionBus()
#
# # Get the object representing the currently running Chromium instance
# chromium_obj = session_bus.get_object(
#     "org.chromium.LibCrosService", "/org/chromium/LibCrosService"
# )
#
# # Get the interface for the Chromium object
# chromium_iface = dbus.Interface(
#     chromium_obj, "org.chromium.LibCrosServiceInterface"
# )
#
# # Call the method to get the URL of the current tab
# url = chromium_iface.GetPrimaryURL()
#
# # Print the URL
# print(url)


import subprocess

# Get the output of the shell command
# to retrieve the URL of the current tab in Chromium

# subprocess.run(["notify-send", "message one"])

# output = subprocess.check_output(
#     ["xdotool", "search", "--onlyvisible",
#      "--class", "chromium", "getactivewindow",
#      "getwindowproperty", "_NET_ACTIVE_WINDOW"]).strip()
#
# # Parse the output to get the URL
# url = subprocess.check_output(
#     ["xprop", "-id", output, "WM_CLASS",
#      "WM_NAME", "WM_WINDOW_ROLE", "_NET_WM_PID",
#      "_NET_WM_NAME"])

# Get the output of the `wmctrl` command
# to retrieve the ID of the active window

output = subprocess.check_output(["wmctrl", "-a", "chromium"]).strip()

subprocess.run(["notify-send", str(len(output))])

subprocess.run(["notify-send", output])

# Parse the output to get the ID of the active window
window_id = output.split()[0]

# Get the output of the `xprop` command
# to retrieve the URL of the active window

output = subprocess.check_output(["xprop", "-id",
                                  window_id, "WM_CLASS",
                                  "WM_NAME", "WM_WINDOW_ROLE",
                                  "_NET_WM_PID", "_NET_WM_NAME"])

# Print the URL
# print(output)
# Print the URL

subprocess.run(["notify-send", output])
