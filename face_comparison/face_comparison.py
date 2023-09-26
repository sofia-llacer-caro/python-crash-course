#!/usr/bin/python3
"""
Triple quotes (double or single) are used to define multiline strings.
They are used for documenting the code and commonly referred as docstrings.
For example, at the top of a module, it's good practice to write a few lines on how to use it.
This program compares faces in two images given. It takes two arguments with the paths of images to compare.
Should be executed this way:

python face_compare.py path/to/image1.jpg path/to/image2.jpg

"""
import argparse

import face_recognition

parser = argparse.ArgumentParser(description="Compare the main face of two images")
parser.add_argument("image_1", type=str, help="The first image to compare")
parser.add_argument("image_2", type=str, help="The second image to compare")


def get_distance(one_file, other_file):
    one_image = face_recognition.load_image_file(one_file)
    other_image = face_recognition.load_image_file(other_file)
    one_encoding = face_recognition.face_encodings(one_image)[0]
    other_encoding = face_recognition.face_encodings(other_image)[0]
    return face_recognition.face_distance([one_encoding], other_encoding)[0]


if __name__ == "__main__":
    args = parser.parse_args()
    dist = get_distance(args.image_1, args.image_2)
    print(f"Distance between these two faces is: {dist:.02f}")
