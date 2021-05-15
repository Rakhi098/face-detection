import cv2 as cv

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
# ( SRC, FRAME writing, no of frame per second size of frame)
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while True:
    ret, frame = cap.read()
    if ret is True:
        # width and height of frame
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        out.write(frame)

        # camera in gray scale
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()
