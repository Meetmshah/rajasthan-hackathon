import face_recognition
import cv2
from db_utils import *

def db_init():
    init()

def authenticate_person(small_frame, face_locations):
    # authentiate whether person is in the database or not
    face_encodings = face_recognition.face_encodings(
        small_frame, face_locations)
    face_names = []
    data = get_encodings()
    known_faces = [face_encoding[1] for face_encoding in data]
    names = [name[0] for name in data]

    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(
            known_faces, face_encoding)
        name = "Unknown"

        try:
            idx = match.index(True)
            name = names[idx]
        except:
            print("Person not in database!")
        face_names.append(name)

    return face_locations, face_names

def show_bbox(frame, face_locations, face_names):
    while True:
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was
            # scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('image', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def capture_image(cap):
    ret, img = cap.read()
    return img

def find_face(small_frame):
    face_locations = face_recognition.face_locations(small_frame)
    if len(face_locations) == 1:
        return True, face_locations
    else:
        print("Please try again!")
        return False, None


def main():
    db_init()
    cap = cv2.VideoCapture(0)
    ret = False
    while not ret:
        frame = capture_image(cap)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        ret, face_locations = find_face(small_frame)

    face_locations, face_names = authenticate_person(small_frame, face_locations)
    show_bbox(frame, face_locations, face_names)



if __name__ == "__main__":
    main()
