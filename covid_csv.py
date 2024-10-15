import csv

class CovidStats:
    def __init__(self, file_name, chunk_size=10000):
        self.file_name = file_name
        self.chunk_size = chunk_size
        self.total_records = 0
        #self.data = []
        self.invalid_data = []
        self.sex_count = {}
        self.vaccine_distribution = {}
        self.jurisdiccion_count = {}
        self.second_doses_jurisdiccion_count = {}
        self.reforced_olders_count = 0
        
    # Getters method for accessing the attributes
    def get_file_name(self):
        return self.file_name
    '''
    def get_data(self):
        return self.data
    '''
    def get_invalid_data(self):
        return self.invalid_data

    def get_sex_count(self):
        return self.sex_count
        
    def get_vaccine_distribution(self):
        return self.vaccine_distribution
    
    def get_jurisdiccion_count(self):
        return self.jurisdiccion_count
    
    def get_second_doses_jurisdiccion_count(self):
        return self.second_doses_jurisdiccion_count
    
    def get_reforced_olders_count(self):
        return self.reforced_olders_count
    
    def get_invalid_data(self):
        return self.invalid_data
    
    def get_total_records(self):
        return self.total_records

    def count_total_records(self):
        """
        Counts the total number of records in the CSV file.

        This method reads the CSV file and stores the total number of records
        in the total_records attribute. It then prints the total number of
        records to the console.

        :return: None
        """
        with open(self.file_name, "r") as csvFile:
            self.total_records = sum(1 for _ in csvFile) - 1  # -1 to exclude the header
    
    def load_data(self):
        """
        Loads the data from the CSV file and processes it in chunks.

        This method processes the CSV file in chunks of a specified size
        (default is 10000) to avoid loading all the data into memory at once.
        It reads the file line by line and stores each row in a dictionary
        which is then appended to a list. When the list reaches the specified
        chunk size, it is processed and reset to empty. This process is repeated
        until all the data has been processed.

        The processed data is stored in the data attribute as a list of dictionaries.
        """
        with open(self.file_name, "r") as csvFile:
            headers = csvFile.readline().strip().split(",")
            chunk = []
            
            for line in csvFile:
                row_data = dict(zip(headers, line.strip().split(",")))
                chunk.append(row_data)
                
                if len(chunk) >= self.chunk_size:
                    #self.data.extend(chunk)  # save the chunk in the list data
                    self.process_chunk(chunk)  # process the chunk
                    chunk = []  # reset the chunk
                    
            # Procesa el último chunk si hay datos restantes
            if chunk:
                #self.data.extend(chunk)
                self.process_chunk(chunk)         
    
    def process_chunk(self, chunk):
        """
        Processes a chunk of data and updates the corresponding attributes.

        This method receives a list of dictionaries (chunk) and processes it by
        calling the corresponding methods to update the attributes of the
        CovidStats object. The methods called are:

        - count_sexo: updates the sex_count attribute
        - count_vaccine_distribution: updates the vaccine_distribution attribute
        - count_doses_by_jurisdiccion: updates the jurisdiccion_count attribute
        - count_second_doses_by_jurisdiccion: updates the second_doses_jurisdiccion_count attribute
        - count_reforced_doses_by_age: updates the reforced_olders_count attribute

        :param chunk: a list of dictionaries
        """
        self.count_sexo(chunk)
        self.count_vaccine_distribution(chunk)
        self.count_doses_by_jurisdiccion(chunk)
        self.count_second_doses_by_jurisdiccion(chunk)
        self.count_reforced_doses_by_age(chunk)



    def count_sexo(self, chunk):
        """
        Counts the number of people for each gender and stores the result in the
        sex_count attribute. The sex_count attribute is a dictionary where the keys are the
        genders and the values are the number of people for each gender.

        :param chunk: a list of dictionaries
        """
        valid_genders = {'F', 'M', 'S.I.', 'X'}  # Valid genders as a set
        for row in chunk:
            gender = row["sexo"]
            
            if gender in valid_genders:
                self.sex_count[gender] = self.sex_count.get(gender, 0) + 1
            else:
                self.sex_count["invalid gender format"] = self.sex_count.get("invalid gender format", 0) + 1
                self.invalid_data.append(row)

    
    def count_vaccine_distribution(self, chunk):
        """
        Counts the number of people vaccinated for each vaccine type and stores the result in the
        vaccine_distribution attribute. The vaccine_distribution attribute is a dictionary where the
        keys are the vaccine types and the values are the number of people vaccinated with each vaccine type.
        """
        total_vaccines = 0
        for row in chunk:
            vaccine_type = row["vacuna"]
            self.vaccine_distribution[vaccine_type] = self.vaccine_distribution.get(vaccine_type, 0) + 1
            total_vaccines += 1

    def count_doses_by_jurisdiccion(self, chunk):              
        """
        Counts the number of people for each jurisdiccion_residencia and stores the result in the
        jurisdiccion_count attribute. The jurisdiccion_count attribute is a dictionary where the keys are the
        jurisdiccion_residencia and the values are the number of people for each jurisdiccion_residencia.
        """
        for row in chunk:
            jurisdiccion = row["jurisdiccion_residencia"]
            if jurisdiccion == 'S.I.':
                self.invalid_data.append(row)
            self.jurisdiccion_count[jurisdiccion] = self.jurisdiccion_count.get(jurisdiccion, 0) + 1

       
    def count_second_doses_by_jurisdiccion(self, chunk):
        """
        Counts the number of people who have received a second dose in each jurisdiccion_residencia
        and stores the result in the second_doses_jurisdiccion_count attribute. The
        second_doses_jurisdiccion_count attribute is a dictionary where the keys are the
        jurisdiccion_residencia and the values are the number of people who have received a
        second dose in each jurisdiccion_residencia.
        """
        for row in chunk:
            if row["orden_dosis"] == '2':  
                jurisdiccion = row["jurisdiccion_residencia"]
                if jurisdiccion == 'S.I.':
                    self.invalid_data.append(row)
                self.second_doses_jurisdiccion_count[jurisdiccion] = self.second_doses_jurisdiccion_count.get(jurisdiccion, 0) + 1

    def count_reforced_doses_by_age(self, chunk):
        """
        Counts the number of people who have received a refuerzo dose and are over 60 years old.
        
        The count is stored in the reforced_olders_count attribute.
        """
        for row in chunk:
            grupo_etario = row["grupo_etario"]
            doses_name = row["nombre_dosis_generica"]
            
            is_grater_60 = (grupo_etario.startswith('60') or grupo_etario.startswith('70') or grupo_etario.startswith('80') or grupo_etario.startswith('90'))
            if doses_name == 'Refuerzo' and is_grater_60:
                self.reforced_olders_count += 1

        
    def write_invalid_data(self, output_file):
        """
        Writes the invalid data to a file.

        :param output_file: the name of the file to write the invalid data to
        """
        if self.invalid_data:
            headers = self.invalid_data[0].keys()  # Usa las keys del primer diccionario para obtener las headers  
            
            with open(output_file, 'w', newline='') as csvFile:
                writer = csv.DictWriter(csvFile, fieldnames=headers)
                writer.writeheader()  # Escribe la cabecera en el nuevo archivo CSV
                writer.writerows(self.invalid_data)  # Escribe todos los registros con errores
