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

% Test initialization
image_size = 10;  % Smaller size for testing
image = zeros(image_size);
raysum = 50 * ones(image_size, 1);

% Test function with small data
try
    updated_image = mart_update(image, raysum, 1, 1.5);
    disp('Test completed successfully.');
catch err
    disp(['Error occurred: ', err.message]);
end

