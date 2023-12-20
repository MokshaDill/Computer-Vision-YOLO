from ultralytics import  YOLO
import cv2

model = YOLO('../YOLO Weight/yolov8n.pt')
result = model("Images/1.png", show=True)
#result = model("C:\\Users\\moksh\\OneDrive\\Desktop\\Document\\tester folder\\img\\logo1.png", show=True)
cv2.waitKey(0)