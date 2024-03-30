import os
from ex5 import CaesarCipher, VigenereCipher, loadEncryptionSystem
import json
import sys

def compare_files_by_suffix(dir_path, suffix_a, suffix_b):
    file_groups = {}
    counter = 0
    for filename in os.listdir(dir_path):
        base_name, extension = os.path.splitext(filename)
        if extension in (f".{suffix_a}", f".{suffix_b}"):
            base_name_parts = [base_name[:5], base_name[5:]]
            if len(base_name_parts) == 2:
                group_key = base_name_parts[1]
                file_groups.setdefault(group_key, []).append(os.path.join(dir_path, filename))

    for group_key, filenames in file_groups.items():
        if len(filenames) == 2:
            with open(filenames[0], 'rb') as file_a, open(filenames[1], 'rb') as file_b:
                if file_a.read() == file_b.read():
                    pass
                    #print(f"Files for '{group_key}' are identical.")   #   <---- uncomment if you want
                else:
                    print(f"Files for '{group_key}' differ!")           #   <---- comment if you want
                    counter += 1
        else:
            print(f"Group '{group_key}': Not enough files for comparison.")
    return counter


def main():
    output = open('output.txt', 'w')
    sys.stdout = output
    print("Test Results")
    count = []

    path = os.path.join('.', 'vigenere')
    loadEncryptionSystem(path, 'vigenere')
    Title('encrypting with vigenere (encrypt = true)', True)
    count.append(compare_files_by_suffix(path, 'out', 'enc'))


    path = os.path.join('.', 'vigenere_encrypted')
    loadEncryptionSystem(path, 'vigenere')
    Title('decrypting with vigenere (encrypt = false)')
    count.append(compare_files_by_suffix(path, 'out', 'vigenere'))

    for i in range(1,4):
        path = os.path.join('.', 'caesar_enc' + str(i))
        loadEncryptionSystem(path, 'caesar')
        Title(f'decrypting with caesar Folder {i} (encrypt = true)')
        count.append(compare_files_by_suffix(path, 'out', 'caesar'))


    path = os.path.join('.', 'caesar')
    values = [-18,9,-8,20]
    for i in range(1,5):
        dict_c = {"type": "Caesar",
        "encrypt": "True",
        "key": values[i-1]}
        with open(os.path.join('caesar', 'config.json'), 'w') as f:
            json.dump(dict_c, f, indent=4)
        loadEncryptionSystem('caesar', 'c' + str(i))
    Title(f'encrypting with caesar (encrypt = true)')
    count.append(compare_files_by_suffix(path, 'out', 'enc'))

    sys.stdout = sys.__stdout__ 
    output.close()

    print('#'*20)
    print('Summary:')
    print("PASSED ALL TESTS!!!") if sum(count) == 0 else [print(f'Failed: {x} from Test {i}') for i,x in enumerate(count)]
    print('#'*20)
    print('For more info check "output.txt"')
    print("Line 22,24 control showing passed/failed tests. Do as you wish!")
    print('GOOD LUCK!!!')
    print('#'*20)


def Title(name, isFirst = False):
    print('\n'*10) if not isFirst else print()
    print('#'*100)
    print(f"Results of Testing {name}")
    print('#'*100)


if __name__ == '__main__':
    main()