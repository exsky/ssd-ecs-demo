import cv2
import time
import asyncio

async def capture_from_cam(num=None, freq=None):
    if not num:
        num = 0
    if not freq:
        freq = 30
    try:
        i = freq
        cap =  cv2.VideoCapture(num)
        #cap = cv2.VideoCapture(num, cv2.CAP_GSTREAMER)
        #cap = cv2.VideoCapture(num, cv2.CAP_V4L2)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
        time.sleep(0.5)
        (grabbed, frame) = cap.read()
        while cap.isOpened():
            (grabbed, frame) = cap.read()
            await asyncio.sleep(0.05)
            if not grabbed:
                print('Stop grabbing ...')
                break
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
            # write file and pend for a while
            if i == 0 :
                print('cheese !')
                cv2.imwrite('live.jpg', frame)
                time.sleep(0.05)
                i = freq
            else:
                i = i -1
                #print(i)
        cap.release()
        cv2.destroyAllWindows()
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
        freq = 30
    try:
        i = freq
        cap =  cv2.VideoCapture(num)
        #cap = cv2.VideoCapture(num, cv2.CAP_GSTREAMER)
        #cap = cv2.VideoCapture(num, cv2.CAP_V4L2)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
        time.sleep(0.5)
        (grabbed, frame) = cap.read()
        while cap.isOpened():
            # print('開始擷取 ...')
            (grabbed, frame) = cap.read()
            print(grabbed)
            if not grabbed:
                print('Stop grabbing ...')
                break
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
            # write file and pend for a while
            if i == 0 :
                #print('cheese')
                cv2.imwrite('live.jpg', frame)
                time.sleep(0.05)
                i = freq
            else:
                i = i -1
                #print(i)
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)
