import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def create_circle(image_shape, center, radius, intensity):
    """ Create a circular shape in the image """
    for x in range(image_shape[0]):
        for y in range(image_shape[1]):
            if (x - center[0]) ** 2 + (y - center[1]) ** 2 < radius ** 2:
                image[x, y] = intensity
    return image

def create_image():
    """ Generate a synthetic medical image with simple geometric shapes """
    image_shape = (256, 256)
    background_intensity = 30  # Background intensity
    image = np.full(image_shape, background_intensity, dtype=np.uint8)

    # Add shapes
    image = create_circle(image, (100, 100), 50, 255)  # Add a bright 'tumor'
    image = create_circle(image, (160, 160), 20, 200)  # Add a smaller 'tumor'

    # Convert to PIL Image and save
    pil_image = Image.fromarray(image)
    pil_image.save('synthetic_medical_image.png')
    
    # Display the image
    plt.imshow(image, cmap='gray')
    plt.title('Synthetic Medical Image')
    plt.axis('off')  # Turn off axis numbers and ticks
    plt.show()

if __name__ == '__main__':
    create_image()

