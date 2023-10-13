from django.shortcuts import render
import json
from django.views import View
from django.views.generic import TemplateView

import asyncio
import cv2
import websockets
from channels.generic.websocket import AsyncWebsocketConsumer



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



class IndexView(View):
    def get(self, request):
        return render(request, 'web_cam.html')

class FrameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Send received data to the WebSocket server
        async with websockets.connect('ws://0.0.0.0:9000/') as websocket:
            await websocket.send(text_data)
            frame_data = await websocket.recv()

            # Process the frame using OpenCV
            frame = cv2.imdecode(bytearray.fromhex(frame_data.split(',')[-1]), cv2.IMREAD_COLOR)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Send the processed frame back to the client
            await self.send({
                'type': 'frame.processed',
                'frame_data': gray_frame.tolist(),
            })

class FrameProcessingView(TemplateView):
    template_name = 'web_page/frame_processing.html'
