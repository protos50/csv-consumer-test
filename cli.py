from covid_csv import CovidStats

def run_cli_interface():
    print("\nBienvenido al sistema de estadísticas de COVID-19.")
    covid_stats = CovidStats("modelo_muestra.csv")
    covid_stats.load_data()
    covid_stats.count_sexo()
    
    
    # Accede a los datos usando los métodos getter
    sex_count = covid_stats.get_sex_count()
    invalid_data = covid_stats.get_invalid_data()

    # Imprime los resultados del conteo de género
    print("\nConteo de género: ")
    print(f"Masculino: {sex_count.get('M', 0)}")
    print(f"Femenino: {sex_count.get('F', 0)}")
    
    # Imprime la distribución de vacunas
    print("\nDistribución de vacunas: ")
    covid_stats.count_vaccine_distribution()
            # Calculating the proportion of each vaccine
    for vaccine, count in covid_stats.get_vaccine_distribution().items():
        proportion = (count / len(covid_stats.data)) * 100
        print(f"{vaccine}: {proportion:.2f}%")
    print(f"Total de registros: {len(covid_stats.data)}")
    
    print(f"Registros inválidos: {len(invalid_data)}")
