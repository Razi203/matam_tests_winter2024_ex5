import os

def remove_files_by_suffix(dir_path, suffix):
    for filename in os.listdir(dir_path):
        if filename.endswith(suffix):
            file_path = os.path.join(dir_path, filename)
            try:
                os.remove(file_path)
                #print(f"Removed file: {filename}")
            except OSError as e:
                pass
                print(f"Error deleting {filename}: {e}")


def clean():
    script_dir = os.path.dirname(os.path.realpath(__file__))

    path = os.path.join(script_dir, 'vigenere')
    remove_files_by_suffix(path, 'enc')

    path = os.path.join(script_dir, 'vigenere_encrypted')
    remove_files_by_suffix(path, 'vigenere')

    for i in range(1,4):
        path = os.path.join(script_dir, 'caesar_enc' + str(i))
        remove_files_by_suffix(path, 'caesar')

    path = os.path.join(script_dir, 'caesar')
    remove_files_by_suffix(path, 'enc')


if __name__ == '__main__':
    clean()