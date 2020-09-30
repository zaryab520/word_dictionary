# Dictionary

Language in Python which uses an Excel file as the source (database) to show result to users. The program only needs to be English-to-Dari or English-to-Pashto,  its not required to working the other way.
program should first ask the user for the English word, then should prompt for the language that user needs the word to be translated to (Dari/Pashto).
program should also provide another interface (command line) and provide users the ability to add new translations to the dictionary if it does not exist.


# Languages:
python3


# Installation Options

    Install with pip
        $ pip install xlsxwriter
        $ pip install openpyxl

    Download the stronghold binary from Releases tab.
    

# How does it work?
 - The program includes two modules naming 'translate_word.py' and 'add_new_word.py' and an excel sheet as database/source called 'dictionary.xlsx'.
 - translate_word.py consists the translation codes, and add_new_word.py is responsible for adding new word to dictionary.
 - to start with the application run translate_word.py from command line. enter this code >>>python3 translate_word.py
 - The application ask the user to enter English word to transalte, it then prompt the user to choose the language of translation either Dari or pashto
 - If the entered word does not exists in the dictionary it prompt the user if he/she wants to add the word in the Dictionary.
 - If wants to add new word, it calls newdic() function in add_new_word.py the user will be asked to enter the Dari and pashto translation of the word, and then it adds the word to dictionary.


# How to Contribute

    Clone repo and create a new branch: $ git checkout https://github.com/zaryab520/Dictionary -b name_for_new_branch.
    Make changes and test
    Submit Pull Request with comprehensive description of changes

# Donations

This is free, open-source software. If you'd like to support the development of future projects, contact me at +93 779567151

# License 

 © Netlinks | Designed by Zaryab Merzakhil 
