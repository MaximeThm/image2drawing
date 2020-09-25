import cv2
import os
from tkinter.filedialog import askdirectory

directory = askdirectory()

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        img_location = os.path.join(directory, filename)
        img = cv2.imread(img_location)

        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        inverted_gray = 255 - gray_image
        blurred_img = cv2.GaussianBlur(inverted_gray, (25, 25), 0)
        inverted_blurred = 255 - blurred_img

        pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

        os.chdir(directory)

        cv2.imwrite(filename, pencil_sketch)

    else:
        continue
