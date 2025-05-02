from ultralytics import YOLO

model=YOLO("YOLO11n.pt")

import cv2
cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break
    #Run YOLO11s on the frame

    results=model(frame)

    #Display the results
    for result in results:
        for box in result.boxes:
            x1,y1,x2,y2=map(int,box.xyxy[0])  #Get bounding box
            conf=box.conf[0]  #Confidence score
            label=model.names[int(box.cls[0])]

            #draw bounding box and label
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(frame, f"{label}: {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow("YOLOv11 Real-Time Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()