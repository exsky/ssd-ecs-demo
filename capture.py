import cv2

def capture_from_cam(num=None):
    if not num:
        num = 0
    try:
        camera = cv2.VideoCapture(num)
        (grabbed, frame) = camera.read()
    except Exception as e:
        print(e)

def record_from_cam(num=None):
    if not num:
        num = 0
    try:
        cap = cv2.VideoCapture(num)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
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

def main():
    record_from_cam(0)
    #while True:
    #    capture_from_cam()

if __name__ == '__main__':
    main()
