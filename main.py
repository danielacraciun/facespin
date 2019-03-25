import dataset

from sys import argv, exit
from constants import FACE_FOLDER, PICTURE_FOLDER, RESULT_FOLDER
from spin.utils import load_image, save_image
from spin.detection import detect_faces
from spin.face import merge_faces
from merge_face import load_merge_face

def add_test_data():
    db = dataset.connect('sqlite:///people_faces.db')
    table = db['person']
    table.insert(dict(name='marian', facepath=FACE_FOLDER + '/marian.jpg'))

def run():
    add_test_data()

    merge_face = load_merge_face(argv[1], argv[1])
    output_img = PICTURE_FOLDER + "/" + argv[2]

    io_pipe = load_image(output_img)
    detect_pipe = detect_faces(io_pipe)
    merge_pipe = merge_faces(merge_face, detect_pipe)
    save_image(merge_pipe)

if __name__ == '__main__':
    run()
