import numpy as np
import matplotlib.pyplot as plt

def mart_reconstruction(sinogram, initial_image, iterations):
    """
    Perform MART reconstruction on a given sinogram.

    Args:
    sinogram (2D numpy array): The sinogram data (projections at different angles).
    initial_image (2D numpy array): Initial guess for the image reconstruction.
    iterations (int): Number of iterations to run the MART algorithm.

    Returns:
    2D numpy array: Reconstructed image.
    """
    reconstructed_image = np.copy(initial_image)
    for _ in range(iterations):
        for angle_idx, projection in enumerate(sinogram):
            # Simulate projection
            simulated_projection = np.sum(reconstructed_image, axis=0)
            update_ratio = projection / simulated_projection
            update_matrix = np.tile(update_ratio, (reconstructed_image.shape[0], 1))
            reconstructed_image *= update_matrix
    
    return reconstructed_image
