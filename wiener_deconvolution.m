pkg load image;

% Simulate a blurred image
original_image = phantom("Modified Shepp-Logan", 256);
psf = fspecial('motion', 21, 11);  % Example PSF (motion blur)
blurred_image = imfilter(original_image, psf, 'conv', 'circular');

% Add noise to the blurred image
noisy_blurred_image = imnoise(blurred_image, 'gaussian', 0, 0.01);

% Display the original, blurred, and noisy blurred images
figure;
subplot(1, 3, 1);
imshow(original_image, []);
title('Original Image');

subplot(1, 3, 2);
imshow(blurred_image, []);
title('Blurred Image');

subplot(1, 3, 3);
imshow(noisy_blurred_image, []);
title('Noisy Blurred Image');

% Apply Wiener deconvolution
estimated_nsr = 0.01;  % Estimate of the noise-to-signal power ratio
deconvolved_image = deconvwnr(noisy_blurred_image, psf, estimated_nsr);

% Display the deconvolved image
figure;
imshow(deconvolved_image, []);
title('Deconvolved Image using Wiener Filter');

