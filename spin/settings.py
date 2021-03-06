""" Provides app settings """

from os.path import dirname, join

ROOT_FOLDER = dirname(dirname(__file__))
RESOURCES_FOLDER = join(ROOT_FOLDER, "resources")
IMAGE_CLASSIFIER_FILE = join(RESOURCES_FOLDER, "adaboost_face_detection.xml")
