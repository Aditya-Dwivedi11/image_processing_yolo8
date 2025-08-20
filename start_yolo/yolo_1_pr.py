from ultralytics import YOLO
import cv2 as c


model = YOLO("../yolo-weights/yolov8n.pt")

# rb = model("images/schl_bus.png", show=True, save=True)
# rbi = model("images/bikes.png", show=True)
# rc1 = model("images/cars1.png", show=True)
# rc2= model("images/cars2.png", show=True)
# rc3 = model("images/cars3.png", show=True)
# rc4= model("images/cars4.png", show=True)
# c.waitKey(0)

# model.load_weights("yolov8n.h5")

rb = model("images/schl_bus.png", show=True,)
rbi = model("images/bikes.png", show=True)
rc1 = model("images/cars1.png", show=True)
rc2= model("images/cars2.png", show=True)
rc3 = model("images/cars3.png", show=True)
rc4= model("images/cars4.png", show=True)
c.waitKey(0)
