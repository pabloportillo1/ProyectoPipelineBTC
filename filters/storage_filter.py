import json
from filters.base_filter import BaseFilter

class StorageFilter(BaseFilter):

    def process(self, transaction):

        with open("data/transactions.json", "r") as file:
            transactions = json.load(file)

        #Agregamos la transaccion realizada a la lista de transacciones conviertiendola 
        # a un diccinoario para hacerlo compatible con JSON.
        transactions.append(transaction.__dict__)

        # Guardamos la transaccion realizada dentro del archivo dandole unn formato mas legible.
        with open("data/transactions.json", "w") as file:
            json.dump(transactions, file, indent = 4)

        transaction.status = "Registered"

        return transaction