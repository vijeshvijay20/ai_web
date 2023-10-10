from django.shortcuts import render
import json
# from track_windows import track_window_changes

def index_view(request):
    # Your view logic here
    return render(request, 'web_page/index.html')

def yolov8_tracking(request):
    # Read JSON data from the file
    with open('objects_detected_yv8.json', 'r') as json_file:
        data = json.load(json_file)
    # Pass the data to the template
    return render(request, 'web_page/Yolov8_Tracking.html', {'data': data})

def object_tracked(request):
    with open('objects_detected.json', 'r') as json_file:
        data = json.load(json_file)        
    context = {
        'data': data,
    }
    return render(request, 'web_page/object_tracking.html',context)

def windows_tracking(request):
    # Read JSON data from the file
    with open('windows_tracking.json', 'r') as json_file:
        data = json.load(json_file)

    # Pass the data to the template
    return render(request, 'web_page/windows_tracking.html', {'data': data})

def noise_tracking(request):
    # Read JSON data from the file
    with open('noise_data.json', 'r') as json_file:
        data = json.load(json_file)

    # Pass the data to the template
    return render(request, 'web_page/noise_tracking.html', {'data': data})

def noise_plot(request):
    # You don't need to pass any data to this view.
    return render(request, 'web_page/noise_plot.html')

def head_eye_tracking(request):
    # Read JSON data from the file
    with open('head_pose_data.json', 'r') as json_file:
        data = json.load(json_file)

    # Pass the data to the template
    return render(request, 'web_page/head_eye_tracking.html', {'data': data})
# def detect_windows(request):
#     track_window_changes()
#     return render(request, 'web_page/window_trac.html')

