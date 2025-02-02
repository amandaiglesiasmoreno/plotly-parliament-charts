from .data_utils import (
    generate_levels,
    generate_points,
    generate_radii_theta
)
from .plot_utils import (
    create_parliament_chart,
    setup_layout,
    add_local_image_to_plot
)

def main():
    # Data for parties and their seat counts
    parties = ['NI', 'ESN', 'PfE', 'ECR', 'EPP', 'Renew', 'Greens/EFA', 'S&D', 'The Left']
    seats = [28, 25, 86, 80, 188, 75, 53, 136, 46]
    
    # Assign colors to parties
    colors = ['#999999', '#13517e', '#253082', '#196ca8', '#3399ff', '#ffd700', '#57b45f', '#f0001c', '#b71c1c']
    
    # Define levels (radius values)
    num_levels = 10
    levels = generate_levels(num_levels, min_radius=0.3, max_radius=1.3)

    # Generate points per level
    total_seats = sum(seats)
    points_per_level = generate_points(levels, total_seats)

    theta_start, theta_end = -60, 240
    # Generate radii and theta values
    radii_sorted, theta_sorted = generate_radii_theta(levels, points_per_level, theta_start, theta_end)

    # Create the parliament chart
    fig = create_parliament_chart(parties, seats, colors, radii_sorted, theta_sorted, marker_size=7)

    # Set up the layout for the chart
    title = "European Parliament Composition (2024-2029)"
    subtitle = "Seats Distribution by Political Groups in the European Parliament"
    footer = "Data source: en.wikipedia.org"
    setup_layout(fig, title, subtitle, footer)

    fig = add_local_image_to_plot(fig,'images/european-union.png', x=0.5, y=0.5, sizex=0.125, sizey=0.125)

    # Show the figure
    fig.show()

if __name__ == "__main__":
    main()