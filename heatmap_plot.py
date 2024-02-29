import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.colors as mcolors

heatmap_directory = "heatMap_Images"

heatmap_filename = "000001.png"


heatmap_image_path = os.path.join(heatmap_directory, heatmap_filename)
heatmap_image = Image.open(heatmap_image_path) # Load the variable into a variable of an image type

heatmap_array = np.array(heatmap_image) # The loaded heat map image is turned 
#into a NumPy array.
# Each pixel value is in the form of intensities in an RGB channel. 
# That is each pixel value is in the form of [82 88, 202] for example - Red, Green, Blue values
# All these values for every pixel in the image is stored in the heatmap_array variable.

# Image is preprocessed. That is the values are normalized to teh range of [0,1]
heatmap_array = heatmap_array / 255.0

cmap_custom = 'coolwarm' 
# Color map Intensity transitions from colder to warmer colours

# A custom colourmap is defined. 
#  colormap is applied to the normalized pixel values,
#  mapping them to colors based on their intensity.
# Each normalized intensity value [R_norm, G_norm, B_norm] in the numpy array
#  for a pixel is mapped to a specific color in the colormap.

# ASK WHAT THE COLOUR PALLETE is. THE INTENSITY LABEL CAN BE CREATED ACCORDINGLY

# The heat map is plotted
plt.figure(figsize=(8,6))
plt.imshow(heatmap_array, cmap = cmap_custom) # custom colourmap for heatmap effect

plt.colorbar(label='Eye Gaze Intensity')

# FOR NOW, I CHOSE THE 'coolwarm' lablel because in a heatmap usually, colder
#colours like blue indicate less eye gaze intensity and warmer colours like red
# indidcate higher eye gaze intensity.

# The intensity label referes to the intensity of the pixel values in the 
# image. Each pixel value rerpesents the intensity of each color channel at 
# each pixel location. By adding the label, you are indicating that the 
# colorbar represents the intensity of the pixel values in the heatmap image. 

plt.colorbar() #A colorbar is added for reference
plt.title("Heat Map Plot")
#plt.xlabel('X Axis Label') 
#plt.ylabel('Y Axis Label')  
plt.show()


# A scatter plot can be created to gain more insight into the RGB color 
# distribution. 