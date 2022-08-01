import cv2
import os
from option import details
count = 1
folder = "M-16"
path = details['path']
directory = os.path.join(path, folder+"i")
os.mkdir(directory)
for file in os.listdir(f"{path}{folder}"):
    file = f"{path}{folder}\\"+file
    print(file)
    image = cv2.imread(file)
    image = cv2.flip(image, 1)
    cv2.imwrite(f"{directory}\\M-{count}.jpg", image)
    count += 1
