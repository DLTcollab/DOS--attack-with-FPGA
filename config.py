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


FullNodeNumber = 10

"""
FullNodeNumber is the number of all full nodes.
"""

Node1 = "https://tuna.iotasalad.org:14265"



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

