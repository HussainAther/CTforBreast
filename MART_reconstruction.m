% MART_Reconstruction.m
% This script implements the Multiplicative Algebraic Reconstruction Technique (MART)
% for computed tomography image reconstruction.

%% Initialization
% Define the image size and initialize the image matrix.
image_size = 512;
image = zeros(image_size);

% Define simulated projection data (raysum) for simplicity.
raysum = 50 * ones(image_size, 1);  % Simplified constant raysum for all lines

%% Function Definition
% Define the MART update function within the script or as a separate function file.
function image = mart_update(image, raysum, num_iterations, P)
    [num_rows, num_cols] = size(image);
    for it = 1:num_iterations
        for i = 1:num_cols  % Assuming vertical lines for simplicity
            line_pixels = image(:, i);
            Rt = sum(line_pixels);
            if Rt ~= 0
                correction_factor = (raysum(i) / Rt)^P;
                image(:, i) = line_pixels * correction_factor;
            end
        end
    end
end

%% Execution
% Parameters for the MART algorithm
num_iterations = 5;  % Number of iterations to perform
P = 1.5;  % Power factor, should be between 1 and 2 to avoid chaos

% Execute the MART update function
updated_image = mart_update(image, raysum, num_iterations, P);

%% Visualization
% Display the original and updated images to compare results
figure;
subplot(1, 2, 1);
imagesc(image);
title('Original Image');
colorbar;

subplot(1, 2, 2);
imagesc(updated_image);
title('Updated Image after MART');
colorbar;

