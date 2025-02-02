# Plotly Parliament Charts
A Python package for visualizing parliamentary seat distributions using Plotly. It creates a polar scatter plot where each marker represents a seat, arranged by radius and angle.

## Features
- **Seat Distribution**: Automatically distributes seats across multiple concentric circles (levels).  
- **Modular Design**: Separate files for data generation (`data_utils.py`), plotting utilities (`plot_utils.py`), and the main script (`main.py`).  
- **Customizable Layout**: Fine-tune chart titles, annotations, legend orientation, and background.  
- **Image Overlay**: Easily embed a local image (e.g., a flag or logo) at the center of the plot.

## Directory Structure
- **parliament_plot/__init__.py**: Makes `parliament_plot` a recognized Python package.
- **parliament_plot/data_utils.py**: Handles generation of radii, angles, and seat distributions.
- **parliament_plot/plot_utils.py**: Manages building Plotly figures, layouts, and optional image overlays.
- **parliament_plot/main.py**: Main entry point to bring everything together and display the figure.
- **images/**: Holds any local images you’d like to overlay onto your plot.
- **requirements.txt**: Contains all Python dependencies.
- **README.md**: Documentation for usage and setup.

## Installation
**Step 1: Clone this repository**
```bash
git clone https://github.com/amandaiglesiasmoreno/plotly-parliament-charts.git
cd plotly-parliament-charts
```

**Step 2: Install dependencies** (preferably in a virtual environment)
```bash
pip install -r requirements.txt
```

## Usage
**Step 1: Confirm `__init__.py` presence**  
Make sure your `parliament_plot/` folder contains an `__init__.py` file (it can be empty).

**Step 2: (Optional) Place a local image**  
If you want an image (like a flag) in the center of the plot, place that image in the `images/` folder (or wherever is convenient) and update the path in `main.py`.

**Step 3: Run the script as a module** (from the **project root**):
```bash
python -m parliament_plot.main
```

## Customization
- **Party Names & Seats**: In `main.py`, edit the lists `parties` and `seats` to match your scenario.  
- **Colors**: Update the `colors` list in `main.py` to match each party’s official color or your preferred color scheme.  
- **Levels**: Adjust `min_radius`, `max_radius`, and `num_levels` in `generate_levels()` to control how seats are distributed radially.  
- **Layout**: Modify or expand `setup_layout` in `plot_utils.py` to customize titles, annotations, legend orientation, etc.  
- **Image Overlay**: Change the path and size parameters of `add_local_image_to_plot` if you want a different logo or image size.

## Troubleshooting
- **ModuleNotFoundError**  
  1. Are you in the **project root** directory?  
  2. Use `python -m parliament_plot.main` instead of `python parliament_plot/main.py`.  
  3. Ensure `__init__.py` exists in `parliament_plot/`.

- **Plot Not Showing**  
  - Verify all required packages are installed.  
  - Check that your browser isn’t blocking local pages.  
  - Alternatively, use `fig.write_html("output.html")` to save and open the chart manually.

## License
This project is licensed under the [MIT License](LICENSE).

## Author
[Amanda Iglesias Moreno](https://github.com/amandaiglesiasmoreno)
