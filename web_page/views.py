from django.shortcuts import render
import json
from django.views import View
from django.views.generic import TemplateView

import asyncio
import cv2
import websockets
from channels.generic.websocket import AsyncWebsocketConsumer

from django.http import JsonResponse
import numpy as np
import os
import time




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


def capture_video(request):
    return render(request, 'web_page/web_cam.html')



def process_video(request):
    if request.method == 'POST':
        # Access the video frames sent from the user
        frames = request.POST.getlist('frames[]')

        # Create a unique directory to save the frames
        timestamp = int(time.time())
        frame_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), str(timestamp))
        os.makedirs(frame_dir, exist_ok=True)

        # Process and save each frame as a PNG image
        for idx, frame_data in enumerate(frames):
            frame = np.fromstring(frame_data, dtype=np.uint8, sep=' ')
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

            # Save the frame as a PNG image with a unique filename
            frame_filename = os.path.join(frame_dir, f'frame_{idx}.png')
            cv2.imwrite(frame_filename, frame)

        return JsonResponse({'status': 'Video frames saved as PNG images.'})

    return JsonResponse({'status': 'Video processing completed.'})
