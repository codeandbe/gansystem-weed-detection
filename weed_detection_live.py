import cv2
from inference import get_model

# ── Config ────────────────────────────────────────────────────────────────────
API_KEY   = "YOUR_ROBOFLOW_API_KEY"   # My Account → Roboflow API
MODEL_ID  = "gansystem-weed-detection-w1ycn/1"
CONF      = 0.50                      # minimum confidence to show a box
# ─────────────────────────────────────────────────────────────────────────────

model = get_model(model_id=MODEL_ID, api_key=API_KEY)

cap = cv2.VideoCapture(0)             # 0 = default webcam; try 1 or 2 if wrong camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("Press Q to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot read from webcam.")
        break

    results = model.infer(frame, confidence=CONF)[0]

    for pred in results.predictions:
        x1 = int(pred.x - pred.width  / 2)
        y1 = int(pred.y - pred.height / 2)
        x2 = int(pred.x + pred.width  / 2)
        y2 = int(pred.y + pred.height / 2)

        is_weed = pred.class_name.lower() == "weed"
        color   = (0, 0, 220) if is_weed else (0, 180, 0)   # red=weed, green=bean
        label   = f"{pred.class_name}  {pred.confidence:.0%}"

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.rectangle(frame, (x1, y1 - 24), (x1 + len(label) * 9, y1), color, -1)
        cv2.putText(frame, label, (x1 + 4, y1 - 6),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)

    weed_count = sum(1 for p in results.predictions
                     if p.class_name.lower() == "weed" and p.confidence >= CONF)

    cv2.putText(frame, f"Weeds detected: {weed_count}", (16, 36),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 220), 2)

    cv2.imshow("GanSystems — Weed Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
