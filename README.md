# COVID-19 Vaccination Data Analysis

This repository contains a project for analyzing COVID-19 vaccination data using CSV files. It is developed in Python and allows the analysis to be executed through a GTK-3 based graphical user interface (GUI) or a command-line interface (CLI).

## Project Structure

The project contains the following key files and directories:

- main.py: Contains the main menu for selecting the interface (CLI or GUI).
- gui.py: Code for the GTK-based graphical interface.
- cli.py: Code for the command-line interface.
- covid_csv.py: Implements the CSV data analysis functions.

### Usage Instructions
  
#### Using the Command-Line Interface (CLI)
1. Run the following command in the terminal:
  ```sh
  python3 main.py
  ```
2. Select option 2 to use the command-line interface.
3. Choose the CSV file to analyze. If no files are in the directory, the user will be notified.
4. The analysis results will be displayed in the terminal.

#### Using the Graphical User Interface (GUI)
1. Run the command:
  ```sh
  python3 main.py
  ```
2. Select option 1 to open the GUI.
3. In the window, select the CSV file from the ComboBox and click on "Load and Analyse Data."
4. The results will be displayed in the graphical interface once the analysis is complete.

### Analysis Results

The project performs the following operations:

- Gender Distribution: Counts how many people of each gender have received the vaccine.
- Vaccinations by Type: Determines the number and proportion of people who received each type of vaccine.
- Doses by Jurisdiction: Groups data by province and counts the administered doses.
- Special Request:
  - Number of people who received the second dose in each jurisdiction.
  - Number of people over 60 years old who received a booster dose.

The resulting executable can be found in the `dist` folder. As long as you have GTK 3 installed on your system, this executable will work properly.

### Download the Executable for linux systems with GTK
You can download the GUI executable from the latest release using the link below:
- [Download the GUI executable]([https://github.com/protos50/csv-consumer-test/releases/edit/v0.1](https://github.com/protos50/csv-consumer-test/releases/tag/v0.1))

This link will take you to the release page, where you can download the compiled version of the app from the `dist` folder.
