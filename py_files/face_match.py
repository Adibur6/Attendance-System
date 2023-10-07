import cv2
import os
import re

# Load the cascade classifier for face detection
def face_match():
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'Haarcascade_frontalface_default.xml')

    # Get the path of the folder containing the images
    
    folder_path = 'db/pictures'
    print(folder_path)

    # Create a dictionary to store the images and their names
    images = {}

    # Read the images from the folder and store them in a dictionary
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            # Get the name of the image

            name = re.sub(r'\..+', '', filename)

            # Read the image and store it in the dictionary

            images[name] = cv2.imread(folder_path + '/'+filename, cv2.IMREAD_GRAYSCALE)


    # Start the webcam
    print(len(images))

    cap = cv2.VideoCapture(0)
    count={}
    i=0

    while i<50:
        # Get a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale( gray,
        scaleFactor=1.05,
        minNeighbors=5,
        minSize=(30, 30),
      
        )

        # Draw a rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Crop the face from the image
            face = gray[y:y+h, x:x+w]

            # Compare the face to the images in the dictionary
            for name, image in images.items():
                result = cv2.matchTemplate(face, image, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, max_loc = cv2.minMaxLoc(result)
            
                if max_val > 0.8:
                    cv2.putText(frame, 'Id: ' + name.split('_')[0], (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                    count[ name.split('_')[0]]=count.get(name.split('_')[0],0)+1
                    
        i+=1
        # Show the frame
        cv2.imshow('Webcam', frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print(count)
    return   max(count, key=count.get)

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

