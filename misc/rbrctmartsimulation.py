import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_circle(ax, x, y, radius=0.05):
    """Draw a circle representing a Janus sphere."""
    circle = patches.Circle((x, y), radius, edgecolor='black', facecolor='none', linewidth=1)
    ax.add_patch(circle)

def draw_xray_path(ax, start_x, start_y, angle, length):
    """Draw the X-ray path and return the end coordinates."""
    end_x = start_x + length * np.cos(np.radians(angle))
    end_y = start_y + length * np.sin(np.radians(angle))
    ax.plot([start_x, end_x], [start_y, end_y], 'r-')
    return end_x, end_y

def adjust_ray_path(ray, adjustment_factor):
    """Apply the MART adjustment to the ray path."""
    return ray * adjustment_factor

def simulate_mart_algorithm(rows=11, cols=11, spacing=0.2, bragg_angle=4, adjustment_factor=0.98):
    """Simulate the MART algorithm with localized adjustments."""
    fig, ax = plt.subplots(figsize=(10, 10))

    # Draw the Janus sphere array
    for i in range(rows):
        for j in range(cols):
            x = j * spacing
            y = i * spacing
            draw_circle(ax, x, y)

    # Initialize the first ray path
    start_x = 0
    start_y = spacing * (rows - 1)  # Start from the top-left corner
    angle = 270 - bragg_angle  # Initial angle (90 degrees for downward, minus Bragg angle)
    length = spacing

    # Iterate over rows, adjusting the ray path with MART algorithm
    for i in range(rows):
        end_x, end_y = draw_xray_path(ax, start_x, start_y, angle, length)
        
        # Apply the MART adjustment to the angle based on the current ray path
        angle = adjust_ray_path(angle, adjustment_factor)

        # Update start position for the next ray
        start_x, start_y = end_x, end_y

    ax.set_aspect('equal', 'box')
    ax.set_xlim(-spacing, (cols - 1) * spacing + spacing)
    ax.set_ylim(-spacing, (rows - 1) * spacing + spacing)
    ax.axis('off')
    plt.title('RBRCT Simulation with MART Algorithm Adjustments')
    plt.show()

# Run the simulation
simulate_mart_algorithm()

