import cv2
import numpy as np
from skimage import exposure

def adaptive_enhancement(image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply adaptive histogram equalization using CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(image)
    
    # Optionally, adjust gamma for further enhancement
    gamma_corrected = exposure.adjust_gamma(enhanced_image, gamma=0.5)
    
    # Display the original and enhanced images
    cv2.imshow('Original Image', image)
    cv2.imshow('Enhanced Image', gamma_corrected)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Path to your mammographic image
image_path = 'path_to_your_image.jpg'
adaptive_enhancement(image_path)

