import cv2


def face_detect_with_webcam():

    # Load the cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'Haarcascade_frontalface_default.xml')


    # Start the webcam
    cap = cv2.VideoCapture(0)

    while True:
    # Get a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw a rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, 'Name: Adib, Detected', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.putText(frame, 'ID: 1804055', (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Show the frame
        cv2.imshow('Webcam', frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()