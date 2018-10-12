from config import *
from tool import *

api = Iota(node[0], seed=SEED)


# attack end

tips = api.get_transactions_to_approve(depth=2)

send_transfer(endMessage,"",ADDRESS,0,tips,0)

print("End message : " + endMessage)
