import cv2
from ultralytics import YOLO

model = YOLO("runs/detect/surgical_instruments_416/weights/best.pt")

video_path = "data/video.mp4"

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error opening video.")
    exit()

fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

resize_width, resize_height = 640, 480

output_path = "output_video.avi"
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, fps, (resize_width, resize_height))

class_colors = {
    0: (255, 0, 0),  
    1: (0, 255, 0),   
    2: (0, 0, 255),   
    3: (255, 255, 0)  
}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_resized = cv2.resize(frame, (resize_width, resize_height))

    results = model(frame_resized, stream=True)

    for result in results:
        boxes = result.boxes.xyxy
        scores = result.boxes.conf
        classes = result.boxes.cls

        for box, score, cls in zip(boxes, scores, classes):
            x_min, y_min, x_max, y_max = map(int, box)
            label = f"{model.names[int(cls)]} {score:.2f}"

            color = class_colors.get(int(cls), (255, 255, 255))  

            cv2.rectangle(frame_resized, (x_min, y_min), (x_max, y_max), color, 2)
            cv2.putText(
                frame_resized,
                label,
                (x_min, y_min - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

    cv2.imshow("Real-Time Detection", frame_resized)

    out.write(frame_resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()