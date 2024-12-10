from ultralytics import YOLO

model = YOLO("yolov8n.pt")  

model.train(
    data="data.yaml",
    epochs=10,
    batch=4,
    imgsz=416,
    name="surgical_instruments_416",
    val=False,
    device=0
)