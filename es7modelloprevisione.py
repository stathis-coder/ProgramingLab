prev_months= [8,19,31,41,50,52,60]
#creo un oggetto vuoto che verrà implementato successivamente 
class Model(object):
    def fit(self, data):
        pass
    def predict(self):
        pass
#creo l'oggetto che aggiorna l'oggetto precedente
class IncrementedModel(Model):
    def fit (self, data):
        raise NotImplementedError('questo modello non prevede un fit')
    #creo il metodo predict che prevede l'andamento della funzione
    def predict(self,prev_month):
        if isinstance(prev_months,str):
            raise TypeError('riprovare e inserire una lista con valori numerici')
        if len(prev_month)<2:
            raise Exception('non è possibile predire l andamento delle vendite con solo un mese nella lista')
        #inizializzo la variabile incremento e la pongo = 0
        incrementi=0
        #uso un for per sommare tutti gli incrementi dei mesi
        for i in range(1,len(prev_months)):
            incremento=prev_months[i]-prev_months[i-1]
            incrementi=incrementi+incremento
        #calcolo la media degli incrementi 
        media=incrementi/(len(prev_months)-1)
        #ritorno la media sommata alle vendite dell'ultimo mese registrato per fare la previsione del mese dopo 
        return media + prev_months[-1]
#istanzio il mio oggetto=mi_modello
mio_modello=IncrementedModel()
#stampo la previsione
print(mio_modello.predict(prev_months))

git