import random
import string
from ex5 import CaesarCipher, VigenereCipher, loadEncryptionSystem
import time

abc_count = ord('z') - ord('a') + 1

def make_string():
    storage = string.whitespace[:3] + string.digits + string.ascii_letters + string.punctuation
    text = "".join([random.choice(storage) for i in range(random.randint(0,200))])
    return text

def main(test_count):
    start = time.time()
    Passed = True
    # Testing Ceasar 
    for i in range(test_count):
        if i % 100 == 0:
            key = random.randint(-30,30)
            cypher = CaesarCipher(key)
        elif i % 10 == 0:
            shift = random.randint(-30,30)
            key += shift
            cypher.key_shift(shift)
        
        original = make_string()
        encrypted = cypher.encrypt(original)
        decrypted = cypher.decrypt(encrypted)
        updated = CaesarCipher(key)
        if encrypted != updated.encrypt(original) or cypher.encrypt('a') != chr(ord('a') + (key%abc_count)):
            Passed = False
            print('_'*80)
            print("#"*10 + " "*5 + "You are not shifting the keys correctly!" + " "*5 + "#"*10)
            print('_'*80)
            break
        if decrypted != original:
            Passed = False
            print("#"*10 + " "*5 + "FAILED Caesar" + " "*5 + "#"*10, end ='\n\n')
            print(f"Key: ({key})\n")
            print("#"*10 + " "*5 + "Original Text" + " "*5 + "#"*10)
            print('_'*50)
            print(original)
            print('_'*50, end ='\n\n\n')
            print("#"*10 + " "*5 + "Encrypted Text" + " "*5 + "#"*10)
            print('_'*50)
            print(encrypted)
            print('_'*50, end ='\n\n\n')
            print("#"*10 + " "*5 + "Decrypted Text" + " "*5 + "#"*10)
            print('_'*50)
            print(decrypted)
            print('_'*50, end ='\n\n\n')
            break
    if not Passed:
        return
    
    # Testing Vigenere
    for i in range(test_count):
        if i % 10 == 0:
            n = random.randint(1,100)
            keys = [random.randint(-30,30) for _ in range(n)]
            cypher = VigenereCipher(keys)
        
        original = make_string()
        encrypted = cypher.encrypt(original)
        decrypted = cypher.decrypt(encrypted)
        if decrypted != original:
            Passed = False
            print("#"*10 + " "*5 + "FAILED Vigenere" + " "*5 + "#"*10, end ='\n\n')
            print(f"Keys: {keys}\n")
            print("#"*10 + " "*5 + "Original Text" + " "*5 + "#"*10)
            print('_'*50)
            print(original)
            print('_'*50, end ='\n\n\n')
            print("#"*10 + " "*5 + "Encrypted Text" + " "*5 + "#"*10)
            print('_'*50)
            print(encrypted)
            print('_'*50, end ='\n\n\n')
            print("#"*10 + " "*5 + "Decrypted Text" + " "*5 + "#"*10)
            print('_'*50)
            print(decrypted)
            print('_'*50, end ='\n\n\n')
            break
    end = time.time()
    if Passed:
        print('_'*50)
        print("#"*10 + " "*5 + "PASSED ALL" + " "*5 + "#"*10)
        print('_'*50)
        print("Passed the random generated tests!")
        print(f"It took {end - start:.4f} seconds to run")
        print("Might as well increase test size! -- test_count = 1000 by deafult")
        print('_'*50)
        


if __name__ == "__main__":
    test_count = 1000
    main(test_count)