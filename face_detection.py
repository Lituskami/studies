import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('C:/Users/migka/OneDrive/Documentos/studies/studies/eu.jpeg')

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    #rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

   
    scale_percent = 50  # Adjust this percentage as needed
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    resized_image = cv2.resize(image, (width, height))

    cv2.imshow('Resized Face Detection', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not found or could not be read.")
