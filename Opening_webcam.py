import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

  # Save the file with the filename "webcam.py"
  # In the terminal in VS Code, type python webcam.py to run the program on windows 
  # Type python3 webcam.py to run the code on mac
 
