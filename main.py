from pipeline import PipeLine
from transaction import Transaction

from filters.authentication_filter import AuthenticationFilter
from filters.comission_filter import ComissionFilter
from filters.transformation_filter import TransformationFilter
from filters.validation_filter import ValidationFilter
from filters.storage_filter import StorageFilter

def main():
    transaction = Transaction(
    user_id = "001",
    btc_amount = 2, 
    currency = "EUR"

     )
    
    pipeline = PipeLine([
        ValidationFilter(),
        AuthenticationFilter(),
        TransformationFilter(),
        ComissionFilter(),
        StorageFilter()
    ])

    result = pipeline.run(transaction)

    print(f"Transaction Status: {result.status}")
    print(result.__dict__)

if __name__ == "__main__":
    main()
