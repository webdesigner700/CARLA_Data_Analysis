import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

heatmap_directory = "heatMap_Images"

heatmap_filename = "000001.png"


heatmap_image_path = os.path.join(heatmap_directory, heatmap_filename)
heatmap_image = Image.open(heatmap_image_path) # Load the variable into a variable of an image type

image_array = np.array(heatmap_image)

# Extract the RGB Channels

red_channel = image_array[:,:,0].flatten()
green_channel = image_array[:,:,1].flatten()
blue_channel = image_array[:,:,2].flatten()
# Here, array slicing is used to extract the red channel from the image array.abs
# The slicing syntax [:,:,0] selects all rows and columns in the numpy array and 
#only selects the first channel('0'). In a Numpy array representing an RGB image
#, the channels are typically ordered as 0 - Red, 1 - Green, 2 - Blue. 
#image_array[:,:,0] selects the red channel from the image array. 

# The flatten() method flattens the 2D array representing the red channel into a 1D array. 
# The flatten operation concatenates all the rows of a 2D array into a 1D array. 

# Compute summary statistics

red_mean = np.mean(red_channel)
green_mean = np.mean(green_channel)
blue_mean = np.mean(blue_channel)

# The mean represents the average intensity value within ech colour channel. 

red_std = np.std(red_channel)
green_std = np.std(green_channel)
blue_std = np.std(blue_channel)

# In this context, the standard deviation measures the spread of the itensity
# values within each RGB colour channel. 

# next we plot histograms to visualize the distributions of each colour channel

plt.figure(figsize=(10, 6))

# the above line of code creates a new figure for plotting with a specified size

plt.subplot(3, 1, 1)

# The above line creates a subplot within the given figure. 
# Subplots are smaller axes that can be arranged in rows and columns
# within a larger figure. '3' indicates the number of rows in the subplot
#grid. '1' indicates the number of columns in the suboplot grid. 
# '1', the last parameter indicates that we are working with the first subplot 
# in the grid. 

plt.hist(red_channel, bins = 50, color='red', alpha = 0.7)

# here, a histogram plot of the red channel intensity values is created.
# bins = 50 represents the number of intervals/bins into which the range of \
# intensity values will be divided into. 
# The alpha value specifies the transparency of the bars in the histogram plot.

plt.axvline(red_mean, color = 'k', linestyle = 'dashed', linewidth = 1)

# This line adds a vertical line to the plot at the postion corresponding 
# to the mean intensity of the red channel. 

plt.title('Red Channel Histogram')
plt.xlabel('Intensity')
plt.ylabel('Frequency')

plt.subplot(3, 1, 2)
plt.hist(green_channel, bins=50, color='green', alpha=0.7)
plt.axvline(green_mean, color='k', linestyle='dashed', linewidth=1)
plt.title('Green Channel Histogram')
plt.xlabel('Intensity')
plt.ylabel('Frequency')

plt.subplot(3, 1, 3)
plt.hist(blue_channel, bins=50, color='blue', alpha=0.7)
plt.axvline(blue_mean, color='k', linestyle='dashed', linewidth=1)
plt.title('Blue Channel Histogram')
plt.xlabel('Intensity')
plt.ylabel('Frequency')

plt.title('Blue Channel Histogram')
plt.xlabel('Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

#print("Red Channel Mean:", red_mean)
#print("Green Channel Mean:", green_mean)
#rint("Blue Channel Mean:", blue_mean)
#rint("Red Channel Standard Deviation:", red_std)
#rint("Green Channel Standard Deviation:", green_std)
#rint("Blue Channel Standard Deviation:", blue_std)


# FOR THE RED CHANNEL FOR EXAMPLE, TAKE THE MEAN VALUE FOR ALL THE 178 IMAGES 
# AND PLOT IT ON A HISTOGRAM

# Based on these histograms, make inferences



