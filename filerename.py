import os
from option import details
folder = "M-47"
path = details['path']
directory = os.path.join(path, folder)
count = 1
for file in os.listdir(f"{directory}"):
    os.rename(f"{directory}\\{file}", f"{directory}\\M-{count}.jpg")
    count += 1
