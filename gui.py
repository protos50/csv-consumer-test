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
        self.analysis_button = Gtk.Button(label="Load and Analyze Data")
        self.analysis_button.connect("clicked", self.start_analysis)
        self.vbox.pack_start(self.analysis_button, False, False, 0)

        # Analysis buttons
        self.add_analysis_buttons()

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
            self.covid_stats = CovidStats(selected_file, chunk_size=100000)
            self.covid_stats.load_data()
            self.covid_stats.count_total_records()
            self.result_label.set_text(f"Data loaded from {selected_file}. Total records: {self.covid_stats.get_total_records()}")
        else:
            self.result_label.set_text("Please select a CSV file to load.")

    def add_analysis_buttons(self):
        """Add buttons for various analysis functionalities."""
        buttons_info = [
            ("Count by Gender", self.count_by_gender),
            ("Vaccine Distribution", self.show_vaccine_distribution),
            ("Doses by Jurisdiction", self.show_distribution_by_jurisdiccion),
            ("Second Doses by Jurisdiction", self.show_second_doses_by_jurisdiccion),
            ("Boosters for Older Adults", self.show_reforced_olders_count),
            ("Save Invalid Data", self.save_invalid_data)
        ]

        for label, callback in buttons_info:
            button = Gtk.Button(label=label)
            button.connect("clicked", callback)
            self.vbox.pack_start(button, False, False, 0)

    def count_by_gender(self, widget):
        """Perform gender count analysis and display the results."""
        if self.covid_stats:
            sex_count = self.covid_stats.get_sex_count()
            result_text = (
                f"Females: {sex_count.get('F', 0)}\n"
                f"Males: {sex_count.get('M', 0)}\n"
                f"No Informado: {sex_count.get('S.I.', 0)}\n"
                f"No Binario: {sex_count.get('X', 0)}\n"
                f"Invalid: {sex_count.get('invalid gender format', 0)}"
            )
            self.result_label.set_text(result_text)
        else:
            self.result_label.set_text("Please load a CSV file first.")

    def show_vaccine_distribution(self, widget):
        """Show vaccine distribution and display the results."""
        if self.covid_stats:
            result_text = "Distribución de vacunas:\n"
            for vaccine, count in self.covid_stats.get_vaccine_distribution().items():
                proportion = (count / self.covid_stats.get_total_records()) * 100
                result_text += f"{vaccine}: {proportion:.2f}%\n"
            self.result_label.set_text(result_text)
        else:
            self.result_label.set_text("Please load a CSV file first.")

    def show_distribution_by_jurisdiccion(self, widget):
        """Show distribution by jurisdiction and display the results."""
        if self.covid_stats:
            result_text = "Distribución de dosis por jurisdicción:\n"
            for jurisdiccion, count in self.covid_stats.get_jurisdiccion_count().items():
                jurisdiccion_name = "Sin Informar" if jurisdiccion == "S.I." else jurisdiccion
                result_text += f"{jurisdiccion_name}: {count} dosis\n"
            self.result_label.set_text(result_text)
        else:
            self.result_label.set_text("Please load a CSV file first.")

    def show_second_doses_by_jurisdiccion(self, widget):
        """Show second doses by jurisdiction and display the results."""
        if self.covid_stats:
            result_text = "Distribución de segundas dosis por jurisdicción:\n"
            for jurisdiccion, count in self.covid_stats.get_second_doses_jurisdiccion_count().items():
                jurisdiccion_name = "Sin Informar" if jurisdiccion == "S.I." else jurisdiccion
                result_text += f"{jurisdiccion_name}: {count} personas\n"
            self.result_label.set_text(result_text)
        else:
            self.result_label.set_text("Please load a CSV file first.")

    def show_reforced_olders_count(self, widget):
        """Show booster count for older adults and display the results."""
        if self.covid_stats:
            count = self.covid_stats.get_reforced_olders_count()
            self.result_label.set_text(f"Personas mayores de 60 años con refuerzo: {count}")
        else:
            self.result_label.set_text("Please load a CSV file first.")

    def save_invalid_data(self, widget):
        """Save invalid data to a file and notify the user."""
        if self.covid_stats:
            file_name = 'invalid_data.csv'
            self.covid_stats.write_invalid_data(file_name)
            if self.covid_stats.get_invalid_data():
                self.result_label.set_text(f"Registros inválidos guardados en {file_name}")
            else:
                self.result_label.set_text("No hay registros inválidos para guardar.")
        else:
            self.result_label.set_text("Please load a CSV file first.")

    def run(self):
        Gtk.main()

# Solo se ejecuta si este archivo es el principal
if __name__ == "__main__":
    gui = GUI()
    gui.run()
