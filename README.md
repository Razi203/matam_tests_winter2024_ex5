# matam_tests_winter2024_ex5

***MAKE SURE TO CHECK IN YOUR LOOPS THAT YOU ARE NOT READING A FOLDER BUT A FILE***
```
if os.path.isfile(file_path):
...
...
```

## Your Friendly Guide For Testing

All of the tests were randomly generated!   

If you notice any mistakes send me a message / open an issue in github or you can make pull request.    

Good Luck!


## steps:
1. Move/Copy your 'ex5.py' to inside of the Tests folder (your file should be in the same directory as all of the supplied files and folders)
    ```
    Tests/
    |__caesar/
    |__caesar_enc1/
    .
    .
    .
    |__cleanUp.py
    |__testRun.py
    |__ex5.py
    ```
2. Run [testRun.py](testRun.py) using your IDE or using ```python3 testRun.py```

3. You'll get a summary in the console and an 'output.txt' file with details in mere seconds :)

___

- To turn off Failed Tests printing in 'output.txt' go to line 24 and comment it

- TO turn on Passed Tests printing in 'output.txt' go to line 22 and uncomment it

* If you want to turn off a folder of tests, comment the the corresponding lines in the main function. Each folder is initialized with a path so it can be easily identified.

**~Clean up**: if you want to remove your outputs from the folders, use the 'cleanUp.py' script provided. 
can be used by IDE or ```python3 cleanUp.py```

## Random Test Generator
New Update: Added [randomTests.py](Tests/randomTests.py) which generates a custom amount of tests (1000 by default) that generate random keys (Random lists for Vigenere and random shifts for Caesar) and validates whether decrypting an encryption returns the original string or not!

**TO RUN:-** simply run `randomTests.py`, make sure your `ex5.py` is in the same directory.


## Tests Explanation
The supplied tests **ONLY** test the *loadEncryptionSystem(...)* function.  
There are dummy files with the targeted files to make sure only the wanted ones are being encrypted/decrypted.

Each folder is meant to test a different functionality:

caesar - encrypting files using caesar

caesar_enc\<i> - decrypting files using caesar, each folder with a different key

vigenere - encrypting files using vigenere

vigenere_encrypted - decrypting files using vigenere

___

The keys in each folder don't match the ones in other folders, i.e each folder is complelety independent

***-Error Files-*** are the files metioned before to test that no other files are being encrypted/decrypted
