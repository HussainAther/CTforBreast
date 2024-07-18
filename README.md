# RBRCT: Ray-by-Ray Computed Tomography

## Overview

Welcome to the Ray-by-Ray Computed Tomography (RBRCT) project repository! This project aims to revolutionize breast cancer screening using photon counting technology and Janus sphere-based x-ray steering. Our goal is to enhance diagnostic accuracy while significantly reducing radiation exposure for patients.

## Key Features

- **Photon Counting Technology:** Provides high precision in x-ray photon counting, allowing for lower radiation doses.
- **Janus Sphere-Based X-ray Steering:** Utilizes innovative Janus spheres to steer x-rays efficiently.
- **Advanced Image Reconstruction:** Employs state-of-the-art machine learning algorithms for high-resolution 3D image reconstruction.
- **Noise Reduction and Deconvolution:** Incorporates AI techniques like Wiener filtering for noise reduction and improved image clarity.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries:
  - NumPy
  - Matplotlib
  - Scipy

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/RBRCT.git
    cd RBRCT
    ```

2. Install the required libraries:
    ```bash
    pip install numpy matplotlib scipy
    ```

### Running the Simulation

The main simulation script demonstrates the photon counting and image reconstruction process. To run the simulation:

```bash
python photon_counting_ct_reconstruction.py
```

### Script Description

- `photon_counting_ct_reconstruction.py`: Simulates photon counting and reconstructs a 3D image using machine learning techniques.

### Example Usage

Generate a simple phantom image, simulate photon counting, and perform image reconstruction:

```python
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
```

## Contributions

We welcome contributions from the community! If you have suggestions, improvements, or new features, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact:
- Syed Hussain Ather - [shussainather@gmail.com]

