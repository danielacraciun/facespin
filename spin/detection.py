import cv2

from .models import Face
from .settings import IMAGE_CLASSIFIER_FILE

CLASSIFIER = cv2.CascadeClassifier(IMAGE_CLASSIFIER_FILE)

def detect_faces(image):
    """ Detect faces in the provided image """
    faces = CLASSIFIER.detectMultiScale(image.cv_image)

    if len(faces) == 0:
        return image

    faces[:, 2:] += faces[:, :2]
    image.faces = [Face(*face) for face in faces]
    return image
