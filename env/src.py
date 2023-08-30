import cv2
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    imagebg=cv2.imread("Resources/BG.png")
    success, img = cap.read()
    imgScaled = cv2.resize(img, (0, 0),None,0.875,0.875)
    imgScaled=imgScaled[:,80:480]
    cv2.imshow("Image", img)
    cv2.imshow("Imagebg", imagebg)
    cv2.imshow("ImageScaled", imgScaled)
    cv2.waitKey(1)