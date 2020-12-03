#creo un metodo che somma tutti i valori di una lista
def list_sum(the_list):
    sum = 0
    for item in the_list:
        sum = sum + item
    return sum
#apro il mio file shampoo sales
my_file = open('shampoo_sales.csv','r')
#definisco un'attributo vuoto dove memorizzerò i valori di sales sotto forma di variabili
converted_values = []
#per ogni riga del mio file 
for line in my_file:
    #separo le date dalle vendite
    elements = line.split(',')
#escludo la prima riga che contiene "Date" e "Sales"
    if elements[0] != 'Date':
        date = elements[0]
        value = elements[1]#prendo tutte le stringhe di sales e le converto in numeri 
        converted_values.append(float(value))
#applico la funzione di prima e stampo la somma dei numeri 
print('somma:', list_sum(converted_values))
#chiudo il file
my_file.close()
#è per me cosi so se il convertimento da stringa a variabile ha funzionato
print(converted_values)