import csv

class CovidStats:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = []
        self.invalid_data = []
        self.sex_count = {}
        self.vaccine_distribution = {}
        self.jurisdiccion_count = {}
        self.second_doses_jurisdiccion_count = {}
        self.reforced_olders_count = 0
        
    # Getters method for accessing the attributes
    def get_file_name(self):
        return self.file_name
    
    def get_data(self):
        
        return self.data
    
    def get_invalid_data(self):
        
        return self.invalid_data

    def get_sex_count(self):
        return self.sex_count
        
    def get_vaccine_distribution(self):
        return self.vaccine_distribution
    
    def get_jurisdiccion_count(self):
        return self.jurisdiccion_count
    
    def load_data(self):
        """
        Reads the CSV file specified in the constructor and loads its content into the
        data attribute. The data attribute is a list of dictionaries, where each dictionary
        represents a row in the CSV file. The keys of the dictionary are the headers of the
        CSV file, and the values are the values in the CSV file for the given row.

        :return: None
        """
        with open(self.file_name, "r") as csvFile:
            headers = csvFile.readline().strip().split(",") 
               
            for line in csvFile:
                row_data = dict(zip(headers, line.strip().split(",")))
                self.data.append(row_data)             
    


    def count_sexo(self):
        """
        Counts the number of people in each gender and stores the result in the
        sex_count attribute. The sex_count attribute is a dictionary where the
        keys are the genders and the values are the number of people in each gender.

        Also, it stores the rows with invalid gender in the invalid_data attribute.
        """
        valid_genders = {'F', 'M', 'S.I.'}  # Valid genders as a set
        
        for row in self.data:
            gender = row["sexo"]
            
            if gender in valid_genders:
                self.sex_count[gender] = self.sex_count.get(gender, 0) + 1
            else:
                self.invalid_data.append(row)

    
    def count_vaccine_distribution(self):
        """
        Counts the number of people for each vaccine type and stores the result in the
        vaccine_distribution attribute. The vaccine_distribution attribute is a
        dictionary where the keys are the vaccine types and the values are the number of
        people for each vaccine type.
        """
        total_vaccines = 0

        for row in self.data:
            vaccine_type = row["vacuna"]
            self.vaccine_distribution[vaccine_type] = self.vaccine_distribution.get(vaccine_type, 0) + 1
            total_vaccines += 1

    def count_doses_by_jurisdiccion(self):              
        """
        Counts the number of people in each jurisdiccion_residencia and stores the result in the
        jurisdiccion_count attribute. The jurisdiccion_count attribute is a dictionary where the
        keys are the jurisdiccion_residencia and the values are the number of people in each jurisdiccion_residencia.
        """
        for row in self.data:
            jurisdiccion = row["jurisdiccion_residencia"]
            self.jurisdiccion_count[jurisdiccion] = self.jurisdiccion_count.get(jurisdiccion, 0) + 1

       
    def count_second_doses_by_jurisdiccion(self):
        """
        Counts the number of people who have received the second dose in each jurisdiccion_residencia and stores the result in the
        second_doses_jurisdiccion_count attribute. The second_doses_jurisdiccion_count attribute is a dictionary where the keys are the
        jurisdiccion_residencia and the values are the number of people in each jurisdiccion_residencia who have received the second dose.
        """
        for row in self.data:
            if row["orden_dosis"] == '2':  
                jurisdiccion = row["jurisdiccion_residencia"]
                self.second_doses_jurisdiccion_count[jurisdiccion] = self.second_doses_jurisdiccion_count.get(jurisdiccion, 0) + 1

        # Imprimir el resultado
        for jurisdiccion, count in self.second_doses_jurisdiccion_count.items():
            print(f"{jurisdiccion}: {count} personas recibieron la segunda dosis")

    def count_reforced_doses_by_age(self):
        """
        Counts the number of people that have received a refuerzo dose and are older than 60 years old.
        The result is stored in the reforced_olders_count attribute.
        """
        for row in self.data:
            grupo_etario = row["grupo_etario"]
            doses_name = row["nombre_dosis_generica"]
            
            is_grater_60 = (grupo_etario.startswith('60') or grupo_etario.startswith('70') or grupo_etario.startswith('80') or grupo_etario.startswith('90'))
            if doses_name == 'Refuerzo' and is_grater_60:
                self.reforced_olders_count += 1

        print(f"Personas mayores de 60 años que han recibido dosis de refuerzo: {self.reforced_olders_count}")

        
    def write_invalid_data(self, output_file):
        if self.invalid_data:
            headers = self.invalid_data[0].keys()  # Usa las keys del primer diccionario para obtener las headers  
            
            with open(output_file, 'w', newline='') as csvFile:
                writer = csv.DictWriter(csvFile, fieldnames=headers)
                writer.writeheader()  # Escribe la cabecera en el nuevo archivo CSV
                writer.writerows(self.invalid_data)  # Escribe todos los registros con errores
            print(f"Datos inválidos guardados en: {output_file}")
        else:
            print("No se encontraron datos inválidos para guardar.")
