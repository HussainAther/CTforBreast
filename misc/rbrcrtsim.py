import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to draw a circle representing a sphere
def draw_circle(ax, x, y, radius=0.05):
    circle = patches.Circle((x, y), radius, edgecolor='black', facecolor='none', linewidth=1)
    ax.add_patch(circle)

# Function to draw the x-ray path with deflection
def draw_xray_path(ax, start_x, start_y, angle, length):
    end_x = start_x + length * np.cos(np.radians(angle))
    end_y = start_y + length * np.sin(np.radians(angle))
    ax.plot([start_x, end_x], [start_y, end_y], 'r-', linewidth=1.5)
    return end_x, end_y

# Function to simulate and visualize the RBRCT
def simulate_rbrct(rows=11, cols=11, spacing=0.2, bragg_angle=4):
    fig, ax = plt.subplots(figsize=(10, 10))
    xray_paths = []

    # Draw the array of spheres
    for j in range(rows):
        for i in range(cols):
            x = i * spacing
            y = j * spacing
            draw_circle(ax, x, y)

    # Initialize the x-ray path
    start_x = 0
    start_y = (rows - 1) * spacing  # Top-left corner
    angle = 270 + bragg_angle  # Initial deflection angle

    # Simulate the x-ray deflection through each row
    for j in range(rows - 1):
        end_x, end_y = draw_xray_path(ax, start_x, start_y, angle, spacing)
        xray_paths.append((start_x, start_y, end_x, end_y))
        start_x, start_y = end_x, end_y

    # Visualize the results
    ax.set_aspect('equal', 'box')
    ax.set_xlim(-spacing, (cols - 1) * spacing + spacing)
    ax.set_ylim(-spacing, (rows - 1) * spacing + spacing)
    ax.axis('off')
    plt.title('11x11 Array of Circles with Sequential X-ray Deflection')
    plt.show()

    return xray_paths

# Run the simulation
xray_paths = simulate_rbrct()

