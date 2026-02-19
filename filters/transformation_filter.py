from multiprocessing import process

from filters.base_filter import BaseFilter

class TransformationFilter(BaseFilter):

        #Simulamos u servicio de conversion con datos fijos.
    exchange_rates = {
        "USD": 43000,
        "EUR": 40000,
        "GBP": 35000
        
        }

    def process(self, transaction):

        #Suponemos que el tipo de moneda ya ha sido validado a traves del pipeline y asignamos un valor a la tasa de cambio
        #dentro de la variable rate. 
        rate = self.exchange_rates.get[transaction.currrency]

        transaction.convertes_amount = transaction.btc_amount * rate

        return transaction