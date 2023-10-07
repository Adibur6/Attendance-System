import cv2
import os

def face_capture(name,id):


    # Load the cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'Haarcascade_frontalface_default.xml')

    # Get the name of the user from the terminal
    internaldb="db/pictures"
    

    # Create a directory with the user's name
    if not os.path.exists(internaldb):
        os.makedirs(internaldb)

    # Start the webcam
    cap = cv2.VideoCapture(0)

    i = 0
    while i < 50:
        # Get a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw a rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Crop the face from the image
            face = gray[y:y+h, x:x+w]

            # Save the face to the directory with the user's name
            cv2.imwrite(internaldb+'/' + id+'_'+ str(i) + '.png', face)
            i += 1

        # Show the frame
        cv2.imshow('Webcam', frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()
