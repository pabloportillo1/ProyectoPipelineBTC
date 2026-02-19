import json
from filters.base_filter import BaseFilter

class AuthenticationFilter(BaseFilter):

    def process (self, transaction):

        #Esta linea de codigo abre el archivo users.json que contiene nuestra base de datos de usuariios y lo lee con "r".
        with open ("data/users.json", "r") as file:
            #Carga los los IDs y nombres de la base de datos en la variable users utilizando json.load(file).
            users = json.load(file)

            if transaction.user_id not in users:
                transaction.status = "Failed: User not found"
                raise ValueError("User ID not found in the system.")
            
            return transaction


