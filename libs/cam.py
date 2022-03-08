import cv2
import asyncio

async def show_frame(num=None):
    if not num:
        num = 0
    try:
        cap = cv2.VideoCapture(num)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
        (grabbed, frame) = cap.read()
        while cap.isOpened():
            (grabbed, frame) = cap.read()
            if grabbed:
                cv2.imshow('frame', frame)
                await asyncio.sleep(0.01)
                if cv2.wait(1) == ord('q'):
                    break
            else:
                print('Stop grabbing ...')
                break
    except Exception as e:
        print(e)
