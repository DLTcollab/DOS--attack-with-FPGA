import tool
import iota
from iota import Iota, Address, TryteString, Transaction
from tool import send_transfer
from config import *


api = Iota(node1, seed=SEED)

re = api.get_node_info()

print(re)

print(re['latestSolidSubtangleMilestone'])








i = 0

while i < 0 :

    trunk_and_branch = {'trunkTransaction':'IFKPAWNVCWOAGSGIVXTFAPESHPKL9GKH9NC9OMVHIBSXZBCEUFQVKVYSBDVEQTYWKOMG9FKCWOKB99999','branchTransaction':nonSolidTransaction}


    send_transfer("YILLKIDATTACK","",ADDRESS,0,trunk_and_branch,0)

    print (i)

    i = i + 1


