import csv

class CovidStats:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = []
        self.invalid_data = []
        self.sex_count = {}
        self.vaccine_distribution = {}
        
    # Getters methodfor accessing the attributes
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
        valid_genders = {'F', 'M'}  # Valid genders as a set
        
        for row in self.data:
            gender = row["sexo"]
            
            if gender in valid_genders:
                self.sex_count[gender] = self.sex_count.get(gender, 0) + 1
            else:
                self.invalid_data.append(row)

    
    def count_vaccine_distribution(self):
        """
        Counts how many people have received each type of vaccine and calculates
        the proportion of each vaccine type with respect to the total.
        """
        total_vaccines = 0

        for row in self.data:
            vaccine_type = row["vacuna"]
            self.vaccine_distribution[vaccine_type] = self.vaccine_distribution.get(vaccine_type, 0) + 1
            total_vaccines += 1

            
        
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
