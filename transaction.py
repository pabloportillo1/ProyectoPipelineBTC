class transaction:
    def __init__(self, user_id, btc_amount, currrency):
        self.user_id = user_id
        self.btc_amount = btc_amount
        self.currency = currrency
        self.converted_amount = None
        self.comission = None
        self.total_amount = None
        self.status = "Created"