from .models import Image
from constants import FACE_FOLDER, PICTURE_FOLDER, RESULT_FOLDER

def load_image(filename):
    """ Loads the images from the source_directory """
    return Image(filename, folder=FACE_FOLDER)

def save_image(image):
    """ Saves the images to the destination_directory """
    image.save(RESULT_FOLDER)
