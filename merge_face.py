import dataset
from spin.models import Image
from spin.detection import detect_faces

def load_merge_face(name, destination):
    """ Loads the two images,
        uses the merge_face to detect the face region
        and then crops that area from the image.
        This allows the image to be altered to merge better. """
    db = dataset.connect('sqlite:///people_faces.db')
    table = db['person']
    person = table.find(name=name)
    persons_with_name = [i for i in person]
    face = Image('merge', path=persons_with_name[0]['facepath'])
    image = Image('merge', path=persons_with_name[0]['facepath'])
    faces = detect_faces(face).faces # force evaluation

    return image.crop(faces[0])
