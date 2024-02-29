import os
import numpy as np
from PIL import Image

# I will use this file to preprocessing all the heatmap images into python. 

heatmap_directory = "heatMap_Images"

heatmap_images = []

for filename in os.listdir(heatmap_directory):
    if filename.endswith(".png"):

        image_path = os.path.join(heatmap_directory, filename)
        heatmap_image = Image.open(image_path)

        heatmap_array = np.array(heatmap_image)

        heatmap_array = heatmap_array / 255.0

        heatmap_images.append(heatmap_array)

heatmap_images = np.array(heatmap_images)

print("Number of heatmap images:", len(heatmap_images))
print("Shape of each heatmap image array:", heatmap_images[1].shape)

# .shape is a property of NumPy that returns the shape of the array
# For a 2D image, the shape tuple consists of two values: the height and
#the width. In the case of a color image, the third dimension is the number
# of color channels (3 for RGB).abs

