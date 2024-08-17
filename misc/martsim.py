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

# Function to simulate and visualize the RBRCT with MART adjustments
def simulate_rbrct_with_mart(rows=11, cols=11, spacing=0.2, bragg_angle=4, iterations=5):
    fig, ax = plt.subplots(figsize=(10, 10))
    pixel_grid = np.ones((rows, cols))  # Initialize pixel grid with ones (initial uniform estimate)
    ray_sums = np.zeros(rows)  # Initialize ray sums

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

    # Simulate the x-ray deflection through each row and calculate initial ray sums
    for j in range(rows - 1):
        end_x, end_y = draw_xray_path(ax, start_x, start_y, angle, spacing)
        ray_sums[j] = np.sum(pixel_grid[j, :])  # Sum of pixels along the current row (ray)
        start_x, start_y = end_x, end_y

    # Apply the MART algorithm for a given number of iterations
    for _ in range(iterations):
        for j in range(rows - 1):
            # Calculate the adjustment ratio for the current ray
            target_sum = np.random.uniform(0.8, 1.2) * ray_sums[j]  # Simulated target sum
            current_sum = np.sum(pixel_grid[j, :])
            adjustment_ratio = target_sum / current_sum

            # Adjust pixel values along the ray
            pixel_grid[j, :] *= adjustment_ratio

    # Visualize the final adjusted pixel grid
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(pixel_grid, cmap='gray', interpolation='nearest', extent=[0, cols, 0, rows])
    ax.set_title('Final Adjusted Pixel Grid After MART')
    plt.show()

    return pixel_grid

# Run the simulation with MART adjustments
final_pixel_grid = simulate_rbrct_with_mart()

