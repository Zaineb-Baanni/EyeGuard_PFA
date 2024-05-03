import cv2
import numpy as np
import numpy as npy
import face_recognition as face_rec
import os
def resize(img, size):
    height, width = img.shape[:2]  # Extraction de la hauteur et de la largeur de img.shape
    new_width = int(width * size)
    new_height = int(height * size)
    dimensions = (new_width, new_height)
    return cv2.resize(img, dimensions, interpolation=cv2.INTER_AREA)
path = 'students_images'
studentsimg = []
studentsname = []
mylist = os.listdir(path)
#print(mylist)
for cl in mylist :
    curimg = cv2.imread(f'{path}\{cl}')
    studentsimg.append(curimg)
    studentsname.append(os.path.splitext(cl)[0])
#print(studentsname)

def findEncoding(images) :
    encoding_list = []
    for img in images :
        img = resize(img, 0.50)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodeimg = face_rec.face_encodings(img)[0]
        encoding_list.append(encodeimg)
    return encoding_list
encode_list = findEncoding(studentsimg)

vid = cv2.VideoCapture(0)

while True :
    success, frame = vid.read()
    smaller_frames = cv2.resize(frame, (0,0), None, 0.25, 0.25)
    frames = cv2.cvtColor(smaller_frames, cv2.COLOR_BGR2RGB)

    faces_in_frame = face_rec.face_locations(frames)
    encode_in_frame = face_rec.face_encodings(frames, faces_in_frame)

    for encodeFace, faceloc in zip(encode_in_frame, faces_in_frame) :
        matches = face_rec.compare_faces(encode_list, encodeFace)
        facedis = face_rec.face_distance(encode_list, encodeFace)
        matcheindex = np.argmin(facedis)


        if matches[matcheindex] :
            name = studentsname[matcheindex].upper()
            y1, x1, y2, x2 = faceloc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(frame, (x1, y1),(x2,y2),(0, 255, 0), 3)
            cv2.rectangle(frame, (x1, y2-25), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        else:
            name = 'inconnue'
            y1, x1, y2, x2 = faceloc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cv2.rectangle(frame, (x1, y2 - 25), (x2, y2), (0, 0, 255), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow('video',frame)
        cv2.waitKey(1)












