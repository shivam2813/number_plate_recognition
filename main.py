import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

indian_plate_pattern = re.compile(r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$')

def ocr_on_plate(img, x, y, w, h):
    roi = img[y:y + h, x:x + w]
    roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(roi_gray, config=custom_config)
    return text.strip()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in plates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        plate_text = ocr_on_plate(frame, x, y, w, h)
        cv2.putText(frame, f'Plate: {plate_text}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        if indian_plate_pattern.match(plate_text):
            cv2.imwrite(f'images/captured_plate_{plate_text}.jpg', frame)

    cv2.imshow('License Plate Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
