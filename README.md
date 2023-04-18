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
  - [x] formats (CSV, TXT, data in rows, data in columns)
  - [x] choose splitter of data in upladed file (with this, program knows how to parse the data)
  - [x] validationg uploaded file and casting it into lists (only one curve, correct format, ...)
- [x] adjust parameters of generated chart
  - [x] title
  - [x] legend
  - [x] on/off grid
  - [x] x and y axis description
- [x] adjust parameters of curve in generated chart
  - [x] style of curve and its color
  - [x] style of marker and its color
- [x] drawing chart
  - [x] in the same window
  - [x] redraw on new data
- [x] quit application
- [x] errors in alert windows
