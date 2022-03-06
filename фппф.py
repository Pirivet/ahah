import cv2

vid = cv2.VideoCapture(0)

while(True):
    is_working, frame = vid.read()

    if not is_working:
        print('е удалось получить доступ к камере')
        break
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hsv_low = (0, 30, 110)
    hsv_high = (70, 220, 360)
    mask = cv2.inRange(frame, hsv_low, hsv_high)
    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    frame[mask != 0] = [0, 0, 0]

    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()










