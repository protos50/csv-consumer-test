from covid_csv import CovidStats

def run_cli_interface():
    def load_and_count_data(covid_stats):
        """
        Loads the data from the CSV file and counts the total number of records.

        :param covid_stats: an instance of CovidStats
        :return: the total number of records in the CSV file
        """
        covid_stats.load_data()
        covid_stats.count_total_records()
        return covid_stats.get_total_records()


    def show_gender_count(covid_stats): 
        """
        Show the gender count.

        :param covid_stats: an instance of CovidStats
        """
        sex_count = covid_stats.get_sex_count()
        print("\nConteo de geénero: ")
        print(f"Masculino: {sex_count.get('M', 0)}")
        print(f"Femenino: {sex_count.get('F', 0)}")
        print(f"Sin Informar: {sex_count.get('S.I.', 0)}")
        print(f"No binario: {sex_count.get('X', 0)}")
        print(f"Invalid gender format: {sex_count.get('invalid gender format', 0)}")
    
    def show_vaccine_distribution(covid_stats):
        """
        Show the vaccine distribution.

        :param covid_stats: an instance of CovidStats
        """
        print("\nDistribución de vacunas: ")
        for vaccine, count in covid_stats.get_vaccine_distribution().items():
            proportion = (count / covid_stats.get_total_records()) * 100
            print(f"{vaccine}: {proportion:.2f}%")
            
    
    def show_distribution_by_jurisdiccion(covid_stats):
        """
        Show the distribution by jurisdiction.

        :param covid_stats: an instance of CovidStats
        """
        print("\nDistribución de dosis por jurisdicción: ")
        for jurisdiccion, count in covid_stats.get_jurisdiccion_count().items():
            print(f"{jurisdiccion}: {count} dosis")
            
    def show_second_doses_by_jurisdiccion(covid_stats):
        """
        Show the distribution by jurisdiction.

        :param covid_stats: an instance of CovidStats
        """
        print("\nDistribución de dosis por jurisdicción: ")
        for jurisdiccion, count in covid_stats.get_second_doses_jurisdiccion_count().items():
            print(f"{jurisdiccion}: {count} personas recibieron la segunda dosis")


    def show_reforced_olders_count(covid_stats):
        """
        Show the distribution by jurisdiction.

        :param covid_stats: an instance of CovidStats
        """
        print("\nConteo de personas mayores de 60 años que han recibido dosis de refuerzo: ")
        print(f"Personas mayores de 60 años que han recibido dosis de refuerzo: {covid_stats.get_reforced_olders_count()}")
    
    
    def write_invalid_data_to_file(covid_stats, file_name):
        """
        Writes the invalid data to a file.

        :param covid_stats: an instance of CovidStats
        :param file_name: the name of the file to write the invalid data to
        """
        covid_stats.write_invalid_data(file_name)
        print(f"\nRegistros inválidos guardados en {file_name}")
        
      
    def run_analysis(file_name):
        """
        Runs the analysis of the given CSV file.

        The analysis is performed as follows:

        1. Creates an instance of CovidStats with the given file name and chunk size.
        2. Loads and counts the data using the load_and_count_data function.
        3. Runs the functions to do the analysis:
            - show_gender_count: shows the gender count
            - show_vaccine_distribution: shows the vaccine distribution
            - show_distribution_by_jurisdiccion: shows the distribution by jurisdiction
            - show_second_doses_by_jurisdiccion: shows the distribution of second doses by jurisdiction
            - show_reforced_olders_count: shows the count of people over 60 years old who have received a booster dose
            - write_invalid_data_to_file: writes the invalid data to a file named 'invalid_data.csv'
        4. Prints a message indicating that the analysis is complete.

        If the file is not found, it prints an error message. If any other exception occurs, it prints the exception message.

        :param file_name: the name of the CSV file to analyze
        """
        try:
            print("\nBienvenido al sistema de estadísticas de COVID-19.")

            # Create an instance of CovidStats
            covid_stats = CovidStats(file_name, chunk_size=100000)
            # Load and count the data
            total_records = load_and_count_data(covid_stats)
            print(f"\nTotal de registros: {total_records}")
            # Run the functions to do the analysis
            show_gender_count(covid_stats)
            show_vaccine_distribution(covid_stats)
            show_distribution_by_jurisdiccion(covid_stats)
            show_second_doses_by_jurisdiccion(covid_stats)
            show_reforced_olders_count(covid_stats)
            write_invalid_data_to_file(covid_stats, 'invalid_data.csv')

            print("\nGracias por usar el sistema de estadísticas de COVID-19.")
        except FileNotFoundError:
            print("Error: El archivo csv no se encontró. Asegúrate de que el nombre del archivo sea correcto.")
        except Exception as e:
            print(f"Error: {e}")

     
    # Run the main analysis function     
    run_analysis('datos_nomivac_parte1.csv')
    
if __name__ == "__main__":
    run_cli_interface()
