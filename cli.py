from covid_csv import CovidStats

def run_cli_interface():
    print("\nBienvenido al sistema de estadísticas de COVID-19.")
    covid_stats = CovidStats("modelo_muestra.csv")
    covid_stats.load_data()
    covid_stats.count_sexo()
    
    
    # Accede a los datos usando los métodos getter
    sex_count = covid_stats.get_sex_count()
    invalid_data = covid_stats.get_invalid_data()

    print(f"Conteo de género: {sex_count}")
    print(f"Registros inválidos: {len(invalid_data)}")
