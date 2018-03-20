from db_utils import *
import face_recognition

init()
remake_table()

# Load a sample picture and learn how to recognize it.
harsh_image = face_recognition.load_image_file("./img/harsh.jpg")
harsh_face_encoding = face_recognition.face_encodings(harsh_image)[0]
meet_image = face_recognition.load_image_file("./img/meet.jpg")
meet_face_encoding = face_recognition.face_encodings(meet_image)[0]
maharshi_image = face_recognition.load_image_file("./img/maharshi.jpg")
maharshi_face_encoding = face_recognition.face_encodings(maharshi_image)[0]
niraj_image = face_recognition.load_image_file("./img/niraj.jpg")
niraj_face_encoding = face_recognition.face_encodings(niraj_image)[0]

insert_record('Harsh', harsh_face_encoding, 1)
insert_record('Maharshi', maharshi_face_encoding, 2)
insert_record('Meet', meet_face_encoding, 3)
insert_record('Niraj', niraj_face_encoding, 3)

fcommit()
