import plotly.graph_objects as go
import base64

def create_parliament_chart(parties, seats, colors, radii_sorted, theta_sorted, marker_size=10):
    """
    Create a Plotly figure to visualize the distribution of parliament seats.

    Parameters:
    - parties (list of str): Names of the political parties.
    - seats (list of int): Number of seats allocated to each party.
    - colors (list of str): Colors associated with each party, corresponding to their visualization.
    - radii_sorted (list of float): Radii values (distances from the origin) for the points, sorted by angle and radius.
    - theta_sorted (list of float): Angular positions (in degrees) for the points, sorted by angle and radius.
    - marker_size (int, optional): Size of the markers representing the seats (default is 10).

    Returns:
    - plotly.graph_objects.Figure: A Plotly figure visualizing the seat distribution.
    """
    fig = go.Figure()
    party_start_idx = 0
    
    for i, party in enumerate(parties):
        party_end_idx = party_start_idx + seats[i]
        
        fig.add_trace(go.Scatterpolar(
            r=radii_sorted[party_start_idx:party_end_idx],
            theta=theta_sorted[party_start_idx:party_end_idx],
            mode='markers',
            marker=dict(
                size=marker_size,
                color=colors[i],
            ),
            name=party,
            legendgroup=party,
            hovertemplate='Party: ' + party + '<br>Seats: ' + str(seats[i]) + '<extra></extra>'
        ))
        
        party_start_idx = party_end_idx

    return fig

def setup_layout(fig, title, subtitle, footer, legend_orientation=None):
    """
    Set up the layout for the Plotly figure, including subtitle and footer.
    
    Parameters:
    - fig: The Plotly figure object to update.
    - title: The title of the figure.
    - subtitle: The subtitle of the figure.
    - footer: The footer of the figure.
    - legend_orientation: (Optional) Orientation of the legend ('h' for horizontal, 'v' for vertical).
    """
    # Define annotation position
    annotation_position = -0.0885 if legend_orientation == 'h' else -0.10
    # annotation_position = -0.0850 if legend_orientation == 'h' else -0.1125
    
    layout = dict(
        title=title,
        showlegend=True,
        polar=dict(
            radialaxis=dict(showline=False, showticklabels=False),
            angularaxis=dict(showline=False, showticklabels=False),
            bgcolor='white'
        ),
        height=600,
        width=700,
        font=dict(
            family="Poppins, sans-serif",
        ),
        annotations=[
            dict(
                x=annotation_position, y=1.1, xref='paper', yref='paper',
                text=subtitle, showarrow=False,
                font=dict(size=14, color='grey'),
                xanchor='left'
            ),
            dict(
                x=annotation_position, y=-0.05, xref='paper', yref='paper',
                text=footer, showarrow=False,
                font=dict(size=12, color='grey'),
                xanchor='left'
            )
        ]
    )
    
    # Add legend settings if orientation is provided
    if legend_orientation:
        layout['legend'] = dict(
            orientation=legend_orientation,
            yanchor='bottom',
            y=0.1 if legend_orientation == 'h' else 1,
            xanchor='center',
            x=0.5
        )
    
    fig.update_layout(**layout)

def add_local_image_to_plot(fig, image_path, xref='paper', yref='paper', x=0.5, y=0.5, 
                            xanchor='center', yanchor='middle', sizex=0.5, sizey=0.5, layer='above'):
    """
    Add a local image to a Plotly visualization.

    Parameters:
    - fig (plotly.graph_objects.Figure): The Plotly figure to which the image will be added.
    - image_path (str): The path to the local image file.
    - xref (str, optional): Reference for the x-axis. Default is 'paper' (relative to the figure).
    - yref (str, optional): Reference for the y-axis. Default is 'paper' (relative to the figure).
    - x (float, optional): The x-coordinate of the image center. Default is 0.5 (center of the figure).
    - y (float, optional): The y-coordinate of the image center. Default is 0.5 (center of the figure).
    - xanchor (str, optional): Horizontal alignment of the image ('left', 'center', 'right'). Default is 'center'.
    - yanchor (str, optional): Vertical alignment of the image ('top', 'middle', 'bottom'). Default is 'middle'.
    - sizex (float, optional): The width of the image (in coordinate units). Default is 0.5.
    - sizey (float, optional): The height of the image (in coordinate units). Default is 0.5.
    - layer (str, optional): Whether to place the image 'above' or 'below' the plot. Default is 'below'.
    """
    # Encode the image as a Base64 string
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    image_data = f'data:image/png;base64,{encoded_image}'
    
    fig.update_layout(
        images=[
            dict(
                source=image_data,
                xref=xref,
                yref=yref,
                x=x,
                y=y,
                xanchor=xanchor,
                yanchor=yanchor,
                sizex=sizex,
                sizey=sizey,
                layer=layer
            )
        ]
    )
    return fig