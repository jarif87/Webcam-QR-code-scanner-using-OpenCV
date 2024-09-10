import cv2
import webbrowser

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

while True:
    # Capture the video frame by frame
    ret, img = cap.read()
    
    # Detect and decode the QR code
    data, bbox, _ = detector.detectAndDecode(img)
    
    # If a QR code is detected, break the loop
    if data:
        print(f"QR Code detected: {data}")
        a = data
        break

    # Display the result
    cv2.imshow("QRCODE Scanner", img)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Open the URL in the default web browser
webbrowser.open(a)

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
