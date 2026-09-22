import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = (100, 50, 50)
    upper = (130, 255, 255)

    mask = cv2.inRange(hsv, lower, upper)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Original", frame)

    cv2.imshow("Mask", mask)

    cv2.imshow("Detected Color", result)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# Keep a blue thing in front of the camera, the wholw window would be black and only th blue colour would show up. This is masking using HSV
