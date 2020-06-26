from BLOCK import Block

import json
import hashlib
import datetime
import os



class Blockchain:


    def __init__(self):
        self.chain = []
        self.pending_data = []
        self.difficulty = 4
       

    def genBlock(self):
        genDate = "0/0/0 0:00"
        genBlock = Block({}, genDate)
        self.chain.append(genBlock)

    def lastBlock(self):
        """
        look for the last block that was added
        :return: last block
        """
        return self.chain[len(self.chain) - 1]

    def newBlock(self, newblock):
        
        newblock.index = self.lastBlock().index+1
        newblock.previous_hash = self.lastBlock().hash
        newblock.hash = newblock.calculateHash()
        newblock.mineBlock(self.difficulty)
        self.chain.append(newblock)

    def ChainValidity(self):

        for i in range(0,len(self.chain)):
            if(self.chain[i].hash != self.chain[i].calculateHash()):
                print(f"Chain is not valid. Error in {i} block")
                return False

            if(i > 0 and self.chain[i].previous_hash != self.chain[i-1].hash):
                print("Chain is not valid")
                return False
            #print(str(self.chain[i].hash) +" != "+self.chain[i].calculateHash())
        print("valid chain")
        return True




count = 5
p = Blockchain()
p.genBlock()

for i in range(0,count):
    p.newBlock(Block({'sender':'Divyanshu',
        'reciever':'none',
        'message':f'Block {len(p.chain)} has been added'}))



# for e in p.chain:
#     print(e.__dict__)
#     print()


p.ChainValidity()
os.system('pause')


