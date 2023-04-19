import cv2


def img_Analysis():
    # Load the classifier for face detection
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open the camera and start capturing video
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Draw a rectangle around each detected face and print its position
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            print("Face position: x = %d, y = %d" % (x, y))

        # Display the frame with the detected face
        cv2.imshow('Face detection', frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) == 27:  # 27 is the ASCII code for the 'ESC' key
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()


img_Analysis()
