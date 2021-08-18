from hashlib import sha256
import time

def _SHA256(val):
    return sha256(val.encode()).hexdigest()

def mine(transactions,previous_hash,difficulty):
    prefix_zeros = "0"*difficulty
    nonce = 0
    while True:
        nonce += 1
        val = transactions + previous_hash + str(nonce)
        hash = _SHA256(val)
        if(hash.startswith(prefix_zeros)):
            print(f"Nonce bulunuyor : {nonce}")
            return hash

def main():
    difficulty = 6
    transactions = "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"
    previous_hash = "000000000000000000060971da2108d0541e846a1135e98909a4f0e06c230b28"
    start_time = time.time()
    print("Mining bulunuyor...")
    hash = mine(transactions,previous_hash,difficulty)
    total_time = str(time.time() - start_time)
    print(f"Mining {total_time} saniyede bulundu")
    print(f"Hash : {hash}")
    
main()
    
    