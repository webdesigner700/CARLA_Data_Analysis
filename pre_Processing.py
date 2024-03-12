import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# I will use this file to preprocessing all the heatmap images into python. 

heatmap_directory = "heatMap_Images"

heatmap_images = []

red_means = []

green_means = []

blue_means = []

for filename in os.listdir(heatmap_directory):
    if filename.endswith(".png"):

        image_path = os.path.join(heatmap_directory, filename)
        heatmap_image = Image.open(image_path)

        heatmap_array = np.array(heatmap_image)
        
        # Each pixel value is in the form of intensities in an RGB channel. 
        # That is each pixel value is in the form of [82 88, 202] for example - Red, Green, Blue values
        # All these values for every pixel in the image is stored in the heatmap_array variable.

        heatmap_array = heatmap_array / 255.0
        
        # Normalised Pixel values

        heatmap_images.append(heatmap_array)

heatmap_images = np.array(heatmap_images)

print("Number of heatmap images:", len(heatmap_images))

# .shape is a property of NumPy that returns the shape of the array
# For a 2D image, the shape tuple consists of two values: the height and
#the width. In the case of a color image, the third dimension is the number
# of color channels (3 for RGB).abs

# Each image is stored as a NumPy array in the "heat_images" list. 


# For each of the heatmap images in the "heatmap_images" array, extract the RGB channles and 
# compute the mean values of each of the RGB channels. 

for heatmap_array in heatmap_images: 
    
    # Extracting the RGB channels 
    red_channel = heatmap_array[:,:,0].flatten()
    green_channel = heatmap_array[:,:,1].flatten()
    blue_channel = heatmap_array[:,:,2].flatten()
    
    red_mean = np.mean(red_channel)
    green_mean = np.mean(green_channel)
    blue_mean = np.mean(blue_channel)
    
    red_means.append(red_mean)
    green_means.append(green_mean)
    blue_means.append(blue_mean)
    
print(red_means)
    
#Data 
channels = ['Red', 'Green', 'Blue']
means = [red_means, green_means, blue_means]


# Plot
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

for i, (channel, mean) in enumerate(zip(channels, means)):
    
    channel_mean = np.mean(mean)
    channel_std = np.std(mean)
    print(channel_std)
    axs[i].hist(mean, bins=20, color=channel.lower(), alpha=0.7)
    axs[i].axvline(x = channel_mean, color = 'black', linestyle = '--', label = f'{channel} Mean: {channel_mean:.2f} ± {channel_std:.4f}')
    axs[i].set_xlabel('Mean Values') 
    axs[i].set_ylabel('Frequency')
    axs[i].set_title(f'Distribution of Mean Values for {channel} Channel Intensity')
    axs[i].legend()

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()

# This code will create three seperate histograms for the mean values 
# of the red, green, and the blue channels.

