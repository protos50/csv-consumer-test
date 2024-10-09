

with open("modelo_muestra.csv", "r" ) as csvFile:
    for index, line in enumerate(csvFile):
        print(line.strip().split(","))
        #print(line.replace("\n", ""))
