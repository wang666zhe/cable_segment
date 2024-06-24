from ultralytics import YOLO
 
 
# 加载模型
model = YOLO("runs/segment/data100n-1080/weights/best.pt")   # 设置模型路径

if __name__ == '__main__':
    # 训练模型
    #results = model.train(data='crack-seg.yaml', epochs=100, imgsz=1920, workers=2, batch=4)
    model.predict("assets/13_1.jpg", save=True, conf=0.8, show_conf=False, show_labels=False, show_boxes=False)  # 设置分割图片路径