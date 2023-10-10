import time, os, json
import pygetwindow as gw

# Initialize variables
current_window = None
windows_tracking ={}
def empty_windows_tracking_json():
    if os.path.exists('windows_tracking.json'):
        with open('windows_tracking.json', 'w') as json_file:
            json.dump([], json_file)
            print("Emptied windows_tracking.json.")

def get_current_window():
    global current_window
    try:
        # Get the currently focused window
        current_window = gw.getActiveWindow()
        return current_window.title
    except Exception as e:
        # Handle exceptions (e.g., no window in focus)
        return None

def track_window_changes():
    start= True
    global current_window  # Add this global declaration
    while start:
        new_window =  gw.getActiveWindow()
        
        # Check if the current window has changed
        if new_window and new_window != current_window:
            # print(f"Window Changed: {new_window}")
            current_window = new_window
            windows_tracking[time.strftime('%m/%d/%y %H:%M:%S', time.localtime())]= "Window switched: {} -> {}".format(new_window, current_window)
            with open('windows_tracking.json', 'w') as json_file:
                    json.dump(windows_tracking, json_file, indent=4)
                    print("Window change registered") 
        # Sleep for a short interval (e.g., 1 second)
        time.sleep(1)

# track_window_changes()
