# Tkinter application for drawing charts (TkGraf)

Goal of this application is to provide user interface to load data that will be drawn into chart. Generated chart can be modified and downloaded as image.

# Installation

1. Clone github repo

   ```sh
   git clone https://github.com/matejkrenek/tkGraf.git matejkrenek-tkGraf
   ```

2. Install requirements

- For requirements there is `requirements.txt` file where are all the requirements of this project. You can download requirements into your virtual environment and globally with following command:
  ```sh
  pip install -f requirements.txt
  ```

3. Running application

   ```sh
   python main.py
   ```

# Tasks

- [x] load file
- [] formats (CSV, TXT, data in rows, data in columns)
- [] choose splitter of data in upladed file (with this, program knows how to parse the data)
- [] validationg uploaded file and casting it into lists (only one curve, correct format, ...)
- [] adjust parameters of generated chart
- [] title
- [] legend
- [] on/off grid
- [] x and y axis description
- [] adjust parameters of curve in generated chart
- [] style of curve and its color
- [] style of marker and its color
- [] drawing chart
- [] in the same window
- [] redraw on new data
- [] quit application
- [] errors in alert windows
