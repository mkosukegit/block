import hashlib
import json
import datetime

class Block:
    def __init__(self, index, time_stamp, prev_hash, input_data):
        self.index = index
        self.time_stamp = time_stamp
        self.prev_hash = prev_hash
        self.input_data = input_data
        self.diff = 4
        self.now_hash = self.calc_hash()
        self.nonce = None
    
    def calc_hash(self):
        data = {
            'index' : self.index,
            'timestamp' : self.time_stamp,
            'prevhash' : self.prev_hash,
            'inputdata' : self.input_data,
            'diff' : self.diff
        }
        
        json_txt = json.dumps(data,sort_keys=True)
        return hashlib.sha256(json_txt.encode('ascii')).hexdigest()
        
    def mining(self, transaction):
        nonce = 0
        self.input_data.append(transaction)
        self.now_hash = self.calc_hash()
        
        while True:
            nonce_joined = self.now_hash + str(nonce)
            calced = hashlib.sha256(nonce_joined.encode('ascii')).hexdigest()
            if calced[:self.diff:].count('0') == self.diff:
                break
            nonce += 1
        return nonce
        
def main():
    block_chain = []
    
    new_block = Block(0, datetime.datetime.now().isoformat(), '-', ["取引データ"])
    block_chain.append(new_block)
    
    
    for i in range(5):
        new_block = Block(i+1,datetime.datetime.now().isoformat(), block_chain[i].now_hash, ["取引データ" + str(i+1)])
        block_chain.append(new_block)
    
    for block in block_chain:
        print("---ブロック---")
        print(block.index)
        print(block.time_stamp)
        print(block.prev_hash)
        print(block.input_data)
        print(block.now_hash)
        

main()