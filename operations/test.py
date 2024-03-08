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
    cv2.imwrite(new_folder_path, img)

    print(f"Image saved as: {updated_image_path}")

if _name_ == "_main_":
    if len(sys.argv) != 3:
        print("Usage: python script.py <image_path> <new_folder_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    new_folder_path = sys.argv[2]
    save_image_with_updated_name(image_path, new_folder_path)