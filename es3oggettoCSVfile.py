#CARO MORICHETTI PER QUESTO ESERCIZIO NON SERVE PIU CHE LO CONTROLLI, SONO RIUSCITO A RISOLVERE IL PROBLEMA
class CSVFile():
    #definisco il metodo init che istanzia l'oggetto
    def __init__(self,name):
        #setto l'attributo nome del file
        self.name = name
    #creo il metodo get_data che che torni i dati del file CSV
    def get_data(self):
        #inizializzo una lista nella quale salvare i valori convertiti
        converted_values = []
        #apro il mio file
        my_file = open(self.name,'r')
        #per ogni riga del mio file:
        for line in my_file:
            #separo la stringa in piu stringhe usando "," come separatore
            elements = line.split(',')
            #escludo l'intestazione
            if elements[0] != 'Date':
                #separo le date dalle vendite
                date = elements[0]
                values = elements[1]
                #converto le vendite da stringhe a valori
                #e le appendo alla lista 
                converted_values.append(float(values))
        #chiudo il mio file
        my_file.close()
        #retorno la lista con i valori numerici
        return converted_values


#test
file = CSVFile("shampoo_sales.csv")
data = file.get_data()
print(data)

    
    