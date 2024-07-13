import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_float
from skimage.metrics import structural_similarity as ssim
from skimage.restoration import denoise_tv_chambolle, denoise_bilateral, wiener

def calculate_dose(image, method='wiener'):
    if method == 'wiener':
        psf = np.ones((5, 5)) / 25  # Example PSF
        restored = wiener(image, psf, 0.1)
    elif method == 'tv':
        restored = denoise_tv_chambolle(image, weight=0.1)
    elif method == 'bilateral':
        restored = denoise_bilateral(image, sigma_color=0.05, sigma_spatial=15)
    else:
        restored = gaussian(image, sigma=1)

    return restored

def compare_images(image1, image2):
    ssim_index, _ = ssim(image1, image2, full=True)
    return ssim_index

# Load example images
original_image = img_as_float(data.camera())
noisy_image = original_image + 0.1 * np.random.normal(loc=0, scale=1, size=original_image.shape)

# Calculate dose using different methods
wiener_image = calculate_dose(noisy_image, method='wiener')
tv_image = calculate_dose(noisy_image, method='tv')
bilateral_image = calculate_dose(noisy_image, method='bilateral')

# Compare images
ssim_wiener = compare_images(original_image, wiener_image)
ssim_tv = compare_images(original_image, tv_image)
ssim_bilateral = compare_images(original_image, bilateral_image)

print(f'SSIM Wiener: {ssim_wiener}')
print(f'SSIM TV: {ssim_tv}')
print(f'SSIM Bilateral: {ssim_bilateral}')

# Plot images
fig, axes = plt.subplots(1, 4, figsize=(15, 5))
ax = axes.ravel()

ax[0].imshow(original_image, cmap='gray')
ax[0].set_title("Original Image")

ax[1].imshow(wiener_image, cmap='gray')
ax[1].set_title(f"Wiener Filter (SSIM: {ssim_wiener:.4f})")

ax[2].imshow(tv_image, cmap='gray')
ax[2].set_title(f"TV Denoising (SSIM: {ssim_tv:.4f})")

ax[3].imshow(bilateral_image, cmap='gray')
ax[3].set_title(f"Bilateral Filter (SSIM: {ssim_bilateral:.4f})")

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()

