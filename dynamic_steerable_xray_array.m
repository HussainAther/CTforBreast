function dynamic_steerable_xray_array(num_sources_x, num_sources_y, num_targets)
    % Parameters
    source_spacing = 10; % Spacing between x-ray sources
    target_radius = 20; % Radius at which targets are placed
    source_origin_x = 0;
    source_origin_y = 0;

    % Create Grid of X-Ray Sources
    [X, Y] = meshgrid(source_origin_x:source_spacing:source_origin_x+(num_sources_x-1)*source_spacing, ...
                      source_origin_y:source_spacing:source_origin_y+(num_sources_y-1)*source_spacing);

    % Define Target Points in a Circle
    theta = linspace(0, 2*pi, num_targets+1);
    target_x = target_radius * cos(theta(1:end-1));
    target_y = target_radius * sin(theta(1:end-1));

    % Plot the X-Ray Sources and Targets
    figure;
    hold on;
    plot(X, Y, 'bo', 'MarkerSize', 8, 'LineWidth', 2); % X-Ray Sources
    plot(target_x, target_y, 'rx', 'MarkerSize', 8, 'LineWidth', 2); % Targets

    % Simulate Dynamic Steerable X-Ray Beams
    for i = 1:numel(X)
        % Select the nearest target dynamically
        distances = sqrt((target_x - X(i)).^2 + (target_y - Y(i)).^2);
        [~, nearest_target_idx] = min(distances);
        
        % Dynamic logic to change angle to the nearest target
        target_angle = atan2(target_y(nearest_target_idx) - Y(i), target_x(nearest_target_idx) - X(i));
        beam_length = norm([target_x(nearest_target_idx) - X(i), target_y(nearest_target_idx) - Y(i)]);
        
        % Plot the beam towards the nearest target
        plot([X(i), X(i) + beam_length * cos(target_angle)], [Y(i), Y(i) + beam_length * sin(target_angle)], 'k-', 'LineWidth', 1);
    end

    hold off;
    xlabel('X Coordinate');
    ylabel('Y Coordinate');
    title('Dynamic Array of Addressable, Steerable X-Ray Sources');
    axis equal;
    grid on;
end
