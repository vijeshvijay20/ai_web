# track_windows.py
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck
import time
import json

windows_tracking = {}

def empty_windows_tracking_json():
    windows_tracking.clear()
    print("Emptied windows_tracking.json.")

def track_window_changes():
    screen = Wnck.Screen.get_default()
    screen.force_update()

    while True:
        context = time.strftime('%m/%d/%y %H:%M:%S', time.localtime())
        for window in screen.get_windows():
            window_title = window.get_name()
            if window_title not in windows_tracking:
                windows_tracking[window_title] = []

            windows_tracking[window_title].append(f"Window switched: {context}")
        
        with open('windows_tracking.json', 'w') as json_file:
            json.dump(windows_tracking, json_file, indent=4)
            print("Window changes registered")

        time.sleep(1)

