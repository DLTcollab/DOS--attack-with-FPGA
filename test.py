import tool
import iota
from iota import Iota, Address, TryteString, Transaction
from tool import send_transfer



default_address="BXEOYAONFPBGKEUQZDUZZZODHWJDWHEOYY9AENYF9VNLXZHXBOODCOTYXW9MGGINTEJPLK9AGOPTPODVX"








i = 0

while i < 3 :

    trunk_and_branch = {'trunkTransaction':'IFKPAWNVCWOAGSGIVXTFAPESHPKL9GKH9NC9OMVHIBSXZBCEUFQVKVYSBDVEQTYWKOMG9FKCWOKB99999','branchTransaction':'NRVXBKNNUSASDRRFVHPNDCEOXOYGFGDTJIZKHOZRARVOFGOYUASGFZSAILVNORUQFAZURLQLBBNGA9999'}


    send_transfer("YILLKIDATTACK","",default_address,0,trunk_and_branch,0)

    print (i)

    i = i + 1


