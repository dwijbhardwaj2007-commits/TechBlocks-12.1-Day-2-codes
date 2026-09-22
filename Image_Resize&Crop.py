import cv2
image = cv2.imread("myphoto.jpg")
if image is None:
    print("Could not find the image")
    exit()

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

resized = cv2.resize(image, (500, 300))

cropped = resized[50:250, 100:400]
cv2.imshow("Resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("final_photo.jpg", cropped)

print("Done! Cropped image saved as final_photo.jpg")

#Save any image with the name myphoto.jpg inside the main folder or it would show image not found
