from filters.base_filter import BaseFilter

class ValidationFilter(BaseFilter):

    def process(self, transaction):

        if not transaction.user_id:
            transaction.status = "Failed: Missing user ID"
            raise ValueError("User ID is required.")
        
        if transaction.btc_amount <= 0:
            transaction.status = "Failed: Invalid BTC amount"
            raise ValueError("BTC amount must be greater than 0.")
        
        if transaction.currency not in ["USD", "EUR", "GBP"]:
            transaction.status = "Failed: Unsupported currency"
            raise ValueError("Currency must be in USD, EUR, or GBP.")
        
        return transaction