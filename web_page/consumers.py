import cv2
from channels.generic.websocket import AsyncWebsocketConsumer

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Handle WebSocket disconnect
        pass

    async def receive(self, text_data):
        frame_data = text_data
        frame = cv2.imdecode(bytearray.fromhex(frame_data.split(',')[-1]), cv2.IMREAD_COLOR)

        # Perform OpenCV operations on the frame here
        # Example: you can convert it to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Send the processed frame back to the client
        await self.send({
            'type': 'frame.processed',
            'frame_data': gray_frame.tolist()
        })
