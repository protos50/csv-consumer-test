import gi
import os
from covid_csv import CovidStats  # Asegúrate de tener importado tu archivo que maneja la lógica de CovidStats

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GUI:
    def __init__(self):
        self.window = Gtk.Window()
        self.window.set_title("COVID-19 Vaccine Analysis")
        self.window.set_default_size(800, 600)
        self.window.connect("destroy", Gtk.main_quit)

        self.vbox = Gtk.VBox(spacing=10)
        self.window.add(self.vbox)

        self.label = Gtk.Label(label="Welcome to the COVID-19 Vaccine Analysis App!")
        self.vbox.pack_start(self.label, False, False, 0)

        # ComboBox for CSV file selection
        self.csv_files = self.get_csv_files()
        self.csv_combo = Gtk.ComboBoxText()
        for file in self.csv_files:
            self.csv_combo.append_text(file)
        self.csv_combo.set_active(0)  # Select the first file by default
        self.vbox.pack_start(self.csv_combo, False, False, 0)

        # Button to start the analysis
        self.analysis_button = Gtk.Button(label="Start Analysis")
        self.analysis_button.connect("clicked", self.start_analysis)
        self.vbox.pack_start(self.analysis_button, False, False, 0)

        # Button to count by gender
        self.gender_count_button = Gtk.Button(label="Count by Gender")
        self.gender_count_button.connect("clicked", self.count_by_gender)
        self.vbox.pack_start(self.gender_count_button, False, False, 0)

        self.result_label = Gtk.Label(label="Results will be displayed here.")
        self.vbox.pack_start(self.result_label, False, False, 0)

        self.window.show_all()

        self.covid_stats = None

    def get_csv_files(self):
        """Retrieve a list of CSV files in the current directory."""
        return [file for file in os.listdir() if file.endswith('.csv')]

    def start_analysis(self, widget):
        """Initialize CovidStats with the selected file and load data."""
        selected_file = self.csv_combo.get_active_text()
        if selected_file:
            self.covid_stats = CovidStats(selected_file)
            self.covid_stats.load_data()
            self.result_label.set_text(f"Data loaded from {selected_file}.")

    def count_by_gender(self, widget):
        """Perform gender count analysis and display the results."""
        if self.covid_stats:
            self.covid_stats.count_sexo()
            result_text = f"Females: {self.covid_stats.sex_count.get('F', 0)}, Males: {self.covid_stats.sex_count.get('M', 0)}"
            self.result_label.set_text(result_text)
        else:
            self.result_label.set_text("Please load a CSV file first.")

    def run(self):
        Gtk.main()

# Solo se ejecuta si este archivo es el principal
if __name__ == "__main__":
    gui = GUI()
    gui.run()
