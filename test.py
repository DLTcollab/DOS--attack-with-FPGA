import tool
import iota
from iota import *
from tool import *
from config import *



api = Iota(node[0], seed=SEED)


t = {'trunkTransaction':"EMPLEGXUPQJKUFAOJSSBVRJR9ATRGMBZCXQQQ9PESQST9HXHPIWMLCYDWSNLULXNMUYUKHKMDTJB99999",'branchTransaction':"EMPLEGXUPQJKUFAOJSSBVRJR9ATRGMBZCXQQQ9PESQST9HXHPIWMLCYDWSNLULXNMUYUKHKMDTJB99999"}

send_transfer("","",ADDRESS,0,t,0)

tips = getReferenceTips(api,["MQQXPGHUQXHITYHTMYWPYXGKNAEUGZP9BFISJSF9UESABUYTIWUJQXWZYHPLSBKDEWIUVTA9XVGC99999"]) 


if (len(tips)%2) == 1:
    rTips = {'trunkTransaction':tips[0],'branchTransaction':tips[0]}
    send_transfer("","",ADDRESS,0,rTips,0)
    tip_number = len(tips)
    i = 1
    while i < tip_number :
        trunk_and_branch = {'trunkTransaction':tips[i],'branchTransaction':tips[i+1]}
        send_transfer("","",ADDRESS,0,trunk_and_branch,0)
        i = i + 2


if (len(tips)%2) == 0:
    tip_number = len(tips)
    i = 0
    while i < tip_number :
        trunk_and_branch = {'trunkTransaction':tips[i],'branchTransaction':tips[i+1]}
        send_transfer("","",ADDRESS,0,trunk_and_branch,0)
        i = i + 2






