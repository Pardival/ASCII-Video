import cv2 as cv

cam = cv.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = cam.read()
    # operation on the frame
    ret = cam.set(cv.CAP_PROP_FRAME_WIDTH,320) 
    ret = cam.set(cv.CAP_PROP_FRAME_HEIGHT,240)
    greyFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame', greyFrame)
    if cv.waitKey(1) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()