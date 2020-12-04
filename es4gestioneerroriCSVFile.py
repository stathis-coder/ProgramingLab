#creo la classe CSVfile
class CSVFile():
    #creo il metodo che istanzia l'oggetto
    def __init__(self, name):
        #gli attribuisco l'attributo nome
        self.name = name

    #creo un metodo che legge il file e stampa il valore numerico
    def get_data(self):
        #inizializzo una lista dove salvare i valori numerici
        converted_values = []
        #provo ad aprire il file
        try:
            my_file = open(self.name, 'r')
        #se il file  è inesistente stampo il seguente messaggio
        except Exception as e:
            print('Il file "{}" che ho provato ad aprire è inesistente, riprovare con il nome coretto'.format(e))
            #e poi esco dalla funzione perche si presenta un errore unrecoverable
            return None

        #per ogni riga del mio file:
        for line in my_file:
            #separo la stringa in piu stringhe usando "," come divisore
            element = line.split(',')
            #escludo l'intestazione
            if element[0] != 'Date':
                #setto la data e il valore
                date = element[0]
                value = element[1]
                #provo a convertire "value" in valori numerici
                try:
                    value = float(value)
                #se si verifica un errore di tipo stampo il seguente messaggio 
                except TypeError as e:
                    print('cè stato un errore di tipo con la stringa: "{}"'.format(e))
                #se si verifica un errore di altro tipo stampo il seguente messaggio 
                except Exception as e:
                    print('cè stato un errore sconosciuto con la stringa "{}"'.format(e))
                #salto questa linea e continuo col ciclo
                    continue
                #appendo la stringa convertita in valore numerico alla lista converted_values
                converted_values.append(value)
        #chiudo il mio file
        my_file.close()
        #ritorno la lista di valori numerici
        return converted_values
#test
file = CSVFile("shampoo_sales.csv")
data = file.get_data()
print(data)

