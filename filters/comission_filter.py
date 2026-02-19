from base_filter import BaseFilter

class ComissionFilter(BaseFilter):

    def process(self, transaction):

        transaction.comission = transaction.converted_amount * 0.02
        transaction.total_amount = transaction.converted_amount + transaction.comission

        return transaction