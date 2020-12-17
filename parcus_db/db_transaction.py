from typing import Dict, Tuple, List
from pydantic import BaseModel
from models.transaction_models import TransactionIn 



    

DB_transaction = Dict[int, List[TransactionIn]]

DB_transaction = {12345678: [],
23456789: []
}

def get_transaction(id_usuario: int):
    if id_usuario in DB_transaction.keys():
        return DB_transaction[id_usuario]
    else:
        return None



def add_transaction(transaction:TransactionIn):
    DB_transaction[transaction.id_usuario].append(transaction)
    





