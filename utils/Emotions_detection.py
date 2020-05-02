from keras.preprocessing.image import img_to_array
import cv2
from keras.models import load_model
import numpy as np

detection_model_path = 'cascades/data/haarcascade_frontalface_default.xml'
emotion_model_path = 'Emotions.h5'

face_detection = cv2.CascadeClassifier(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)
EMOTIONS = ["angry","happy","surprised"]

cv2.namedWindow('face')
camera = cv2.VideoCapture(0)
while True:
    frame = camera.read()[1]
    faces = face_detection.detectMultiScale(frame,scaleFactor=1.4, minNeighbors=1,minSize=(30, 30))
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi = gray[y:y+h, x:x+w]
        roi = frame[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (48, 48))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        preds = emotion_classifier.predict(roi)[0]
        emotion_probability = np.max(preds)
        label = EMOTIONS[preds.argmax()]
        font = cv2.FONT_HERSHEY_SIMPLEX
    	color = (255, 255, 255)
    	stroke = 2
    	cv2.putText(frame, label, (x,y), font, 1, color, stroke, cv2.LINE_AA)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()
