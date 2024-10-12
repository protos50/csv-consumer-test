from covid_csv import CovidStats

def main():
    # Aquí podrías agregar lógica para que el usuario seleccione el archivo CSV, si lo deseas.
    covid_stats = CovidStats("modelo_muestra.csv")
    covid_stats.load_data()
    covid_stats.count_sexo()
    covid_stats.write_invalid_data("datos_invalidos.csv")

if __name__ == "__main__":
    main()
