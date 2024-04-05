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
            with open(filenames[0], 'r') as file_a, open(filenames[1], 'r') as file_b:
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
    script_dir = os.path.dirname(os.path.realpath(__file__))
    cleanUp.clean()
    output_path = os.path.join(script_dir, 'output.txt')
    output = open(output_path, 'w')
    sys.stdout = output
    print("Test Results")
    count = []
    test_passed = []


    ######################################### TEST 1
    path = os.path.join(script_dir, 'vigenere')
    loadEncryptionSystem(path, 'vigenere')
    Title('encrypting with vigenere (encrypt = true)', 'enc', 'out', 'vigenere', 1, True)
    count.append(compare_files_by_suffix(path, 'out', 'enc'))
    test_passed.append(sum(count[-1]) == 0)
    print(f"PASSED TEST NUMBER {len(test_passed)}") if test_passed[-1] else 0



    ######################################### TEST 2
    path = os.path.join(script_dir, 'vigenere_encrypted')
    loadEncryptionSystem(path, 'vigenere')
    Title('decrypting with vigenere (encrypt = false)', 'vigenere', 'out', 'vigenere_encrypted', 2)
    count.append(compare_files_by_suffix(path, 'out', 'vigenere'))
    test_passed.append(sum(count[-1]) == 0)
    print(f"PASSED TEST NUMBER {len(test_passed)}") if test_passed[-1] else 0


    ######################################### TEST 3,4,5
    for i in range(1,4):
        path = os.path.join(script_dir, 'caesar_enc' + str(i))
        loadEncryptionSystem(path, 'caesar')
        Title(f'decrypting with caesar Folder {i} (encrypt = false)', 'caesar', 'out', f'caesar_enc{i}', i+2)
        count.append(compare_files_by_suffix(path, 'out', 'caesar'))
        test_passed.append(sum(count[-1]) == 0)
        print(f"PASSED TEST NUMBER {len(test_passed)}") if test_passed[-1] else 0




    ######################################### TEST 6
    path = os.path.join(script_dir, 'caesar')
    values = [-18,9,-8,20]
    for i in range(1,5):
        dict_c = {"type": "Caesar",
        "encrypt": "True",
        "key": values[i-1]}
        with open(os.path.join(script_dir, 'caesar', 'config.json'), 'w') as f:
            json.dump(dict_c, f, indent=4)
        loadEncryptionSystem(path, 'c' + str(i))
    Title(f'encrypting with caesar (encrypt = true)', 'enc', 'out', 'caesar', 6)
    count.append(compare_files_by_suffix(path, 'out', 'enc'))
    test_passed.append(sum(count[-1]) == 0)
    print(f"PASSED TEST NUMBER {len(test_passed)}") if test_passed[-1] else 0


    sys.stdout = sys.__stdout__ 
    output.close()

    breaks = 50
    print('_'*breaks, end='\n\n')
    print('Summary:\n')
    if not fileOutput:
        print("No Files are being generated! (no output)")
        print("Possible problem might be your code is not making new files.")
        print("Make sure your code handles dir_path correctly")
    
    else:
        if all(test_passed):
            print("PASSED ALL TESTS!!!")
            with open(output_path, 'w') as f:
                f.write(get_text_passed())
        else:
            for i,x in enumerate(count):
                print(f'Failed: {x[0]} from Test {i+1}') if not test_passed[i] else print(f"PASSED TEST {i+1}")
                if x[1] != 0:
                    print(f'{x[1]} Files from Test {i+1} failed to generate correctly (no output)')
                print()
            print('_'*breaks, end='\n\n')
            print("If you got 'Files failed to generate' :")
            print("Check the test's folder to see what is wrong with your files")
            print('Might be wrong name, wrong file handling or wrong file reading')
            print("In decrypted tests make sure you are reading the .enc files!!!\n")
   
    print('_'*breaks, end='\n\n')
    print('For more info check "output.txt"')
    print("Lines 28, 30, 33 control printing passed/failed tests. Do as you wish!")
    print('GOOD LUCK!!!')
    print('_'*breaks, end='\n\n')


def Title(name, new, old, folder_name, test_number, isFirst = False):
    print('\n'*10) if not isFirst else print()
    print('_'*100)
    print(f"Results of Testing {name}\n")
    print(f'Your files should end with <filename>.{new}\nFiles that end with <filename>.{old} are premade with correct output')
    print(f"Test {test_number} Folder is '{folder_name}'\n")
    print('v'*100)



def get_text_passed():
    text = ""
    text += r".______      ___           _______.     _______. _______  _______  "
    text += '\n'
    text += r"|   _  \    /   \         /       |    /       ||   ____||       \ "
    text += '\n'
    text += r"|  |_)  |  /  ^  \       |   (----`   |   (----`|  |__   |  .--.  |"
    text += '\n'
    text += r"|   ___/  /  /_\  \       \   \        \   \    |   __|  |  |  |  |"
    text += '\n'
    text += r"|  |     /  _____  \  .----)   |   .----)   |   |  |____ |  '--'  |"
    text += '\n'
    text += r"| _|    /__/     \__\ |_______/    |_______/    |_______||_______/ "
    text += '\n'
    text += r"                                                                   "
    text += '\n'
    text += r"     ___       __       __                                         "
    text += '\n'
    text += r"    /   \     |  |     |  |                                        "
    text += '\n'
    text += r"   /  ^  \    |  |     |  |                                        "
    text += '\n'
    text += r"  /  /_\  \   |  |     |  |                                        "
    text += '\n'
    text += r" /  _____  \  |  `----.|  `----.                                   "
    text += '\n'
    text += r"/__/     \__\ |_______||_______|                                   "
    text += '\n'
    text += r"                                                                   "
    text += '\n'
    text += r".___________. _______     _______.___________.    _______.         "
    text += '\n'
    text += r"|           ||   ____|   /       |           |   /       |         "
    text += '\n'
    text += r"`---|  |----`|  |__     |   (----`---|  |----`  |   (----`         "
    text += '\n'
    text += r"    |  |     |   __|     \   \       |  |        \   \             "
    text += '\n'
    text += r"    |  |     |  |____.----)   |      |  |    .----)   |            "
    text += '\n'
    text += r"    |__|     |_______|_______/       |__|    |_______/             "
    text += '\n'
    return text











if __name__ == '__main__':
    main()
