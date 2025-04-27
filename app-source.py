import cv2
import zmq
import base64
import time
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename=r'source.log', encoding='utf-8', level=logging.DEBUG)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

cap = cv2.VideoCapture(r'./file_example_MP4_1920_18MG.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    _, buffer = cv2.imencode('.jpg', frame)
    jpg_as_text = base64.b64encode(buffer)
    socket.send(jpg_as_text)
    time.sleep(2)
    logger.info("frame read")
cap.release()
