class Transaction:
    
    def __init__(self, user_id, btc_amount, currency):
        self.user_id = user_id
        self.btc_amount = btc_amount
        self.currency = currency
        self.converted_amount = None
        self.comission = None
        self.total_amount = None
        self.status = "Created"