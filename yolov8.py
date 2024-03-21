from ultralytics import YOLO

data_dir = "YOLO_format_images"

model = YOLO("yolov8n.pt")

results = model.train(data = "training_data.yaml", epochs=50, imgsz=416, device = "mps")
