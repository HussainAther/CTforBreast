import cv2
import numpy as np

# Load image
image = cv2.imread('path_to_image', 0)  # Load as grayscale

# Adaptive Histogram Equalization
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
equalized_image = clahe.apply(image)

# Edge Enhancement
edges = cv2.Canny(equalized_image, 100, 200)

# Template Matching with multiple scales
template = cv2.imread('path_to_template', 0)
w, h = template.shape[::-1]
for scale in np.linspace(0.6, 1.4, 20):
    resized_template = cv2.resize(template, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA)
    res = cv2.matchTemplate(equalized_image, resized_template, cv2.TM_CCOEFF_NORMED)
    # Further processing to find and analyze matches

cv2.imshow('Detected Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
