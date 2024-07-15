import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Generate a simple phantom image (e.g., a circle)
def generate_phantom(size):
    phantom = np.zeros((size, size))
    radius = size // 4
    center = size // 2
    for i in range(size):
        for j in range(size):
            if (i - center) ** 2 + (j - center) ** 2 <= radius ** 2:
                phantom[i, j] = 1
    return phantom

# Simulate photon counting
def simulate_photon_counting(image, count_rate):
    noisy_image = np.random.poisson(image * count_rate)
    return noisy_image

# Simple reconstruction using linear programming
def reconstruct_image(counts, size):
    A = np.identity(size ** 2)  # Simple identity matrix as system matrix
    b = counts.flatten()

    # Use linear programming to solve for the image vector
    res = linprog(np.ones(size ** 2), A_eq=A, b_eq=b, bounds=(0, None))
    reconstructed_image = res.x.reshape((size, size))
    return reconstructed_image

# Main function
def main():
    image_size = 64
    count_rate = 1000  # Photon count rate

    # Step 1: Generate a phantom image
    phantom = generate_phantom(image_size)
    plt.figure()
    plt.imshow(phantom, cmap='gray')
    plt.title('Original Phantom Image')
    plt.colorbar()
    plt.show()

    # Step 2: Simulate photon counting
    photon_counts = simulate_photon_counting(phantom, count_rate)
    plt.figure()
    plt.imshow(photon_counts, cmap='gray')
    plt.title('Photon Counts (Simulated)')
    plt.colorbar()
    plt.show()

    # Step 3: Reconstruct the image from photon counts
    reconstructed_image = reconstruct_image(photon_counts, image_size)
    plt.figure()
    plt.imshow(reconstructed_image, cmap='gray')
    plt.title('Reconstructed Image')
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    main()

