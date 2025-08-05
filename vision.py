from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")  # Auto-downloads on first run

def detect_objects(image_path):
    results = model(image_path)
    labels = set()
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            labels.add(label)
    return list(labels)
