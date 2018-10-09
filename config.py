"""
This file is configuration file.
"""


SEED = 'AMRWQP9BUMJALJHBXUCHOD9HFFD9LGTGEAWMJWWXSDVOF9PI9YGJAPBQLQUOMNYEQCZPGCTHGVNNAPGHA'

"""
SEED is defined by user.
It should be iota seed.
"""


ADDRESS = "BXEOYAONFPBGKEUQZDUZZZODHWJDWHEOYY9AENYF9VNLXZHXBOODCOTYXW9MGGINTEJPLK9AGOPTPODVX"

"""
ADDRESS is defined by user.
It should be iota transaction's address.
"""


# Full Node list


fullNodeNumber = 30

"""
FullNodeNumber is the number of all full nodes.
"""

node = [""]*fullNodeNumber

node[0] = "https://tuna.iotasalad.org:14265"
node[1] = "https://potato.iotasalad.org:14265"
node[2] = "https://durian.iotasalad.org:14265"
node[3] = "https://peanut.iotasalad.org:14265"
node[4] = "https://turnip.iotasalad.org:14265"
node[5] = "https://wallet2.iota.town:443"
node[6] = "https://wallet1.iota.town:443"
node[7] = "https://node.deviceproof.org:443"
node[8] = "https://iota-fullnode.de:14267"
node[9] = "http://pnwiota.ddns.net:14700"
node[10]= "https://tangle.heuveling.net"
node[11]= "https://iota.arva.net"
node[12]= "https://node.trustingiot.com:443"
node[13]= "https://nodes.thetangle.org:443"
node[14]= "https://02.hanspetzersnode.org:14267/"
node[15]= "https://dsh.encyclopedia69.com/"
node[16]= "https://nodes.iota.cafe:443"
node[17]= "http://173.249.16.55:18765"
node[18]= "http://macway.ddns.net:14265/"
node[19]= "https://nod3.theshock.de:443"
node[20]= "https://iota-fullnode.de:14267"
node[21]= "https://n1.iotajournal.io:443"
node[22]= "https://trinity.iota-tangle.io:14265/"
node[23]= "https://dsh.encyclopedia69.com/"
node[24]= "http://159.69.179.108:14265"
node[25]= "https://node.iota-talk.de:443"
node[26]= "https://laseriota.com:14267/"
node[27]= "https://iotawallet.cloudcluster.io/"
node[28]= "http://iota.band:14265/"
node[29]= "http://iota1.heidger.eu:14265/"



# attack_init

startMessage = "TESTDOSATTACKSTART"

"""
startMessage is defined by user.
"""

attackType = "nonSolid"

"""
attackType is nonSolid or conflictTransaction.

Other can't work.
"""

nonSolidTransaction = "A99999999999999999999999999999999999999999999999999999999999999999999999999999999"


"""
If attackType is nonSolid , user should define non-solid transaction.
"""


conflictTransactionAddress = ""

"""
If attackType is conflictTransaction , user should define the
 conflict transaction's  address.
"""
conflictTransactionPrivateKey = ""

"""
If attackType is conflictTransaction , user should define the
 conflict transaction's private key.
"""

conflictTransactionValue = -1000

"""
If attackType is conflictTransaction , user should define the conflict transaction's value.
"""
conflictTransactionReceivedAddress = ""

"""
If attackType is conflictTransaction , user should define the conflict transaction's received address.
"""

# attack_end

endMessage = "TESTDOSATTACKEND"

"""
endMessage is defined by user.
"""

