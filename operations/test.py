#!/usr/bin/python3
import os
import sys

import cv2


def save_image_with_updated_name(image_path, new_folder_path):
    if not os.path.exists(image_path):
        print("Image path does not exist.")
        return

    img = cv2.imread(image_path)
    image_name, image_ext = os.path.splitext(os.path.basename(image_path))
    updated_image_path = os.path.join(os.path.dirname(image_path), f"output{image_ext}")
    cv2.imwrite(updated_image_path, img)

    print(f"Image saved as: {updated_image_path}")


if __name__ == "__main__":
    path = os.path.join(os.getcwd(), "images")
    imgPath = os.path.join(path, "input.jpg")
    # print(temp)
    save_image_with_updated_name(imgPath, path)
