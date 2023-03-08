import cv2

def face_track():
    faceCascade = cv2.CascadeClassifier('Facetrack/haarcascade_frontalface_default.xml')

    video_capture = cv2.VideoCapture(0)

    # Boolean for face in screen or not 
    face = False

    x = ""

    # Face tracking values 
    faceCoordinatesX = []
    faceCoordinatesY = []
    faceCoordinatesW = []
    faceCoordinatesH = []

    # Potential rezise of the screen, if needed, uncomment line 25.
    #scaling_factor = 0.5

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            faceCoordinatesX.append(x) # Save face tracking values
            faceCoordinatesY.append(y)
            faceCoordinatesW.append(w)
            faceCoordinatesH.append(h)
            print("True")
            print(x)

        # Display helping text and boolean attribute 
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50, 50)  
        fontScale = 2
        colorTrue = (0, 255, 0)  
        colorFalse = (0,0,255)
        thickness = 2
        a = "True"
        b = "False"

        # Check if face is in frame and display text accordingly
        if x in faces != "":
            cv2.putText(frame, a, org, font, 
                        fontScale, colorTrue, thickness, cv2.LINE_AA)
        else: 
            cv2.putText(frame, b, org, font, 
                        fontScale, colorFalse, thickness, cv2.LINE_AA)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()