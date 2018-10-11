import random
from tool import *
from config import *




# select full node at random


fullNode = node[random.randint(0 , fullNodeNumber - 1)]

api = Iota( fullNode , seed=SEED ) 

print("Selected full node:" + fullNode)

# search startMessage from fullNode

attackStartTag = api.find_transactions(tags=[startMessage])


while attackStartTag['hashes'] == []:
    attackStartTag = api.find_transactions(tags=[startMessage])
    print(attackStartTag)


# issue subTangle transaction

#tipSet = api.find_transactions()


