import os
from ex5 import CaesarCipher, VigenereCipher, loadEncryptionSystem
import cleanUp
import json
import sys

fileOutput = False

def compare_files_by_suffix(dir_path, suffix_a, suffix_b):
    file_groups = {}
    Failed = 0
    Differed = 0
    for filename in os.listdir(dir_path):
        base_name, extension = os.path.splitext(filename)
        if extension in (f".{suffix_a}", f".{suffix_b}"):
            base_name_parts = [base_name[:5], base_name[5:]]
            if len(base_name_parts) == 2:
                group_key = base_name_parts[1]
                file_groups.setdefault(group_key, []).append(os.path.join(dir_path, filename))

    for group_key, filenames in file_groups.items():
        if len(filenames) == 2:
            global fileOutput
            fileOutput = True
            with open(filenames[0], 'rb') as file_a, open(filenames[1], 'rb') as file_b:
                if file_a.read() == file_b.read():
                    pass
                    #print(f"Files for '{group_key:4}' are identical.")     #   <---- uncomment if you want
                else:
                    print(f"Files for '{group_key:4}' differ!")             #   <---- comment if you want
                    Differed += 1
        else:
            print(f"File '{group_key:4}': Has not been generated!")         #   <---- comment if you want
            Failed += 1
    counter = (Differed, Failed)
    return counter


def main():
    cleanUp.clean()
    output = open('output.txt', 'w')
    sys.stdout = output
    print("Test Results")
    count = []


    ######################################### TEST 1
    path = os.path.join('.', 'vigenere')
    loadEncryptionSystem(path, 'vigenere')
    Title('encrypting with vigenere (encrypt = true)', 'enc', 'out', True)
    count.append(compare_files_by_suffix(path, 'out', 'enc'))



    ######################################### TEST 2
    path = os.path.join('.', 'vigenere_encrypted')
    loadEncryptionSystem(path, 'vigenere')
    Title('decrypting with vigenere (encrypt = false)', 'vigenere', 'out')
    count.append(compare_files_by_suffix(path, 'out', 'vigenere'))


    ######################################### TEST 3,4,5
    for i in range(1,4):
        path = os.path.join('.', 'caesar_enc' + str(i))
        loadEncryptionSystem(path, 'caesar')
        Title(f'decrypting with caesar Folder {i} (encrypt = true)', 'caesar', 'out')
        count.append(compare_files_by_suffix(path, 'out', 'caesar'))




    ######################################### TEST 6
    path = os.path.join('.', 'caesar')
    values = [-18,9,-8,20]
    for i in range(1,5):
        dict_c = {"type": "Caesar",
        "encrypt": "True",
        "key": values[i-1]}
        with open(os.path.join('caesar', 'config.json'), 'w') as f:
            json.dump(dict_c, f, indent=4)
        # loadEncryptionSystem('caesar', 'c' + str(i))
    Title(f'encrypting with caesar (encrypt = true)', 'enc', 'out')
    count.append(compare_files_by_suffix(path, 'out', 'enc'))

    sys.stdout = sys.__stdout__ 
    output.close()

    breaks = 50
    print('_'*breaks, end='\n\n')
    print('Summary:')
    if not fileOutput:
        print("No Files are being generated! (no output)")
        print("Possible problem might be your code is not making new files.")
        print("Make sure your code handles dir_path correctly")
    
    else:
        if sum([x[0] + x[1] for x in count]) == 0:
            print("PASSED ALL TESTS!!!")
        else:
            for i,x in enumerate(count):
                print(f'Failed: {x[0]} from Test {i+1}')
                if x[1] != 0:
                    print(f'{x[1]} Files from Test {i+1} failed to generate (no output)')
                print()
   
    print('_'*breaks, end='\n\n')
    print('For more info check "output.txt"')
    print("Line 22,24 control showing passed/failed tests. Do as you wish!")
    print('GOOD LUCK!!!')
    print('_'*breaks, end='\n\n')


def Title(name, new, old, isFirst = False):
    print('\n'*10) if not isFirst else print()
    print('_'*100)
    print(f"Results of Testing {name}\n")
    print(f'Your files end with <filename>.{new}\nCorrect files end with <filename>.{old}')
    print('v'*100)


if __name__ == '__main__':
    main()