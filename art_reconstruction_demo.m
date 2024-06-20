function reconstructed_image = ART(image_size, projections, angles, iterations)
    reconstructed_image = ones(image_size);
    [num_angles, num_projections] = size(projections);

    for iter = 1:iterations
        for i = 1:num_angles
            proj = projections(i, :);
            sim_proj = sum(imrotate(reconstructed_image, angles(i), 'bilinear', 'crop'), 1);
            ratio = proj ./ (sim_proj + 1e-6);  % Avoid division by zero
            backproj_ratio = repmat(ratio, image_size(1), 1);
            rotated_backproj = imrotate(backproj_ratio, -angles(i), 'bilinear', 'crop');
            reconstructed_image = reconstructed_image .* rotated_backproj;
        end
        % Normalize
        reconstructed_image /= max(reconstructed_image(:));
    end
end

% Example usage
angles = linspace(0, 179, 180);  % Angles for projections
image_size = [256, 256];
original_image = phantom("Modified Shepp-Logan", 256);
projections = radon(original_image, angles);
reconstructed_image = ART(image_size, projections, angles, iterations=50);

figure;
imshow(reconstructed_image, []);
title('Reconstructed Image using ART');

