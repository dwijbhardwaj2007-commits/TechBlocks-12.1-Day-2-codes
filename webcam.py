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

  # Save the file with the filename "webcam.py" under our main folder, i.e. TechBlocks_Day2.
  # In the terminal in VS Code, type python webcam.py to run the program on windows, OR python3 webcam.py to run it on mac.
 
 
