import cv2
import time
import asyncio

async def capture_from_cam(num=None):
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
                await asyncio.sleep(0.05)
                if cv2.waitKey(1) == ord('q'):
                    break
            else:
                print('Stop grabbing ...')
                break
    except Exception as e:
        print(e)

def record_from_cam(num=None):
    if not num:
        num = 0
    try:
        cap = cv2.VideoCapture(num)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
    except Exception as e:
        print(e)

    # 使用 XVID encoding
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while cap.isOpened():
        (grabbed, frame) = cap.read()
        if not grabbed:
            print('Stop grabbing ...')
            break
        out.write(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def cap_from_cam(num=None, freq=None):
    if not num:
        num = 0
    if not freq:
        freq = 200
    try:
        cap =  cv2.VideoCapture(num)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
    except Exception as e:
        print(e)

    while cap.isOpened():
        cap = cv2.VideoCapture(num)
        (grabbed, frame) = cap.read()
        if not grabbed:
            print('Stop grabbing ...')
            break
        for i in range(freq):
            cv2.imshow('frame', frame)
            # write file and pend for a while
            if i == freq - 1 :
                cv2.imwrite('live.jpg', frame)
                time.sleep(0.01)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

