import numpy as np
import cv2
import pdb
from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def main():
    face_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/3.3.0_2/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    while(True):
        ret, img = cap.read()
        if ret:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces) == 2:
                img = face_swap(faces, img)
            if len(faces) > 2:
                img = face_swap_all(faces, img)

            cv2.imshow('img', img)
        else:
            print('Can\'t capture')
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def face_swap_all(faces, img):
    for two_faces in pairwise(faces):
        img = face_swap(two_faces, img)
    return img


def face_swap(faces, img):
    (f1_x, f1_y, f1_w, f1_h) = faces[0]
    (f2_x, f2_y, f2_w, f2_h) = faces[1]

    face1 = img[f1_y:f1_y + f1_h, f1_x:f1_x + f1_w]
    face2 = img[f2_y:f2_y + f2_h, f2_x:f2_x + f2_w]

    face1_scaled = cv2.resize(face1, (f2_w, f2_h), interpolation=cv2.INTER_CUBIC)
    face2_scaled = cv2.resize(face2, (f1_w, f1_h), interpolation=cv2.INTER_CUBIC)

    img[f1_y:f1_y + f1_h, f1_x:f1_x + f1_w] = face2_scaled
    img[f2_y:f2_y + f2_h, f2_x:f2_x + f2_w] = face1_scaled

    return img


def face_zoom(faces, img):
    (x, y, w, h) = faces[0]
    img = img[y:y + h, x:x + w]

    img = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
    return img


if __name__ == '__main__':
    main()
