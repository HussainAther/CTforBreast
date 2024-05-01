function intensity = simulate_xray_interaction_with_sphere(xray_position, sphere_position, sphere_radius)
    % Calculate distance between X-ray source and sphere center
    distance = norm(xray_position - sphere_position);
    
    % Check if X-ray source is inside the sphere
    if distance < sphere_radius
        intensity = 0;  % X-ray absorbed by the sphere
    else
        % Otherwise, calculate intensity after passing through the sphere
        intensity = 1 / distance;  % Example inverse square law
    end
endfunction


function reconstructed_image = MART_algorithm(intensity_data, initial_image_guess, iterations)
    current_image = initial_image_guess;
    
    for iter = 1:iterations
        for i = 1:length(intensity_data)
            % Update pixel value based on MART equation
            current_image(i) *= intensity_data(i) / sum(current_image);
        endfor
    endfor
    
    reconstructed_image = current_image;
endfunction

function image = generate_tumor_phantom(image_shape, tumor_position, tumor_radius)
    % Create an empty image
    image = zeros(image_shape);
    
    % Generate a circular tumor region
    for i = 1:image_shape(1)
        for j = 1:image_shape(2)
            if norm([i - tumor_position(1), j - tumor_position(2)]) <= tumor_radius
                image(i, j) = 1;
            endif
        endfor
    endfor
endfunction
