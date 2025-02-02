import numpy as np
import math

def generate_levels(num_levels, min_radius=0.0, max_radius=1.0):
    """
    Generate evenly spaced radius values (levels) between a minimum and maximum radius.

    Parameters:
    - num_levels (int): The number of levels to generate.
    - min_radius (float): The minimum radius value (default is 0.0).
    - max_radius (float): The maximum radius value (default is 1.0).

    Returns:
    - list: A list of evenly spaced radius values between `min_radius` and `max_radius`.
    """
    return np.linspace(min_radius, max_radius, num_levels).tolist()


def generate_points(levels, total_seats):
    """
    Distribute total seats across levels (interpreted as radii) 
    proportionally to their circumferences, using floats for precision 
    and adjusting for rounding errors.

    Parameters:
    - levels (list of float): Radii of the circles.
    - total_seats (int): Total number of seats to distribute.

    Returns:
    - list of int: Number of seats assigned to each circle.
    """
    # Calculate circumferences
    circumferences = [2 * math.pi * r for r in levels]
    total_circumference = sum(circumferences)
    
    # Distribute seats proportionally using floats
    proportional_points = [(circumference / total_circumference) * total_seats for circumference in circumferences]
    
    # Convert to integers and track the residuals
    points_per_level = [int(p) for p in proportional_points]
    residuals = [p - int(p) for p in proportional_points]
    
    # Adjust for rounding errors to match total_seats
    while sum(points_per_level) < total_seats:
        max_index = residuals.index(max(residuals))
        points_per_level[max_index] += 1
        residuals[max_index] = 0  # Prevent double adjustments

    return points_per_level

def generate_radii_theta(levels, points_per_level, theta_start, theta_end):
    """
    Generate radii and theta values for points to be plotted in a polar scatter plot.

    Parameters:
    - levels (list of float): A list of radius values (one for each level) defining the distance of each level from the origin.
    - points_per_level (list of int): A list indicating the number of points to generate for each corresponding level.
    - theta_start (float): The starting angle (in radians) for the angular range of the points.
    - theta_end (float): The ending angle (in radians) for the angular range of the points.

    Returns:
    - tuple: Two lists:
        - radii_sorted (list of float): The radii of the points, sorted first by angle and then by radius.
        - theta_sorted (list of float): The angular positions of the points, sorted first by angle and then by radius.
    """
    radii = []
    theta = []

    for level, count in zip(levels, points_per_level):
        level_theta_values = np.linspace(theta_start, theta_end, count, endpoint=True)
        radii.extend([level] * count)  # Same radius for all points at this level
        theta.extend(level_theta_values)  # Add theta values for this level

    # Sort radii and theta by angle (theta), then by radius
    radii_theta_sorted = sorted(zip(radii, theta), key=lambda x: (x[1], x[0]))
    radii_sorted, theta_sorted = zip(*radii_theta_sorted)

    return radii_sorted, theta_sorted