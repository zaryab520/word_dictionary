# Dictionary

Language in Python which uses an postgresql as the source (database) to show result to users. The program only needs to be English-to-Dari or English-to-Pashto,  and vice versa.
The user selects the two languages one for the word and the other for the translation, then the user enters the word and hit translate button, the application returns the translation.
If the no translation found, the system provide the user with the ability to add the word and translations.
The system emails the latest words that comes into practice in the English world. Therefore, the user gets notified about the latest updates in English lateratuer.


# Languages:
python3
HTML
Javascript
css

# Framework:
flask

# Installation Options

    Install with pip and sudo apt
        & sudo apt install python3.8
        $ pip install flask
        $ pip install smtplib, ssl
        $ pip install SQLALCHEMY
        $ sudo apt install postgresql postgresql-contrib
    

# How does it work?
 - The application uses postgresql as the Database.
 - After running the application, it will redirect the user to login page, there users enter login details, the user can create an account if does not have account. The application provide the users with the ability to reset their password in case forgot password, which the system emails otp to the users to regenerate their password.
 - Once the user logged in, he/she will be redirected to the main page, there the user can selects the languag and enter the word for translation. 
 - The user can add new words to the dictioanary if not found in the system, pop up will be displayed to add new word by clicking on Add New Word.
 - The application emails the latest words discovered in English world. So, the users will be notified about the latest updates in English language.


# How to Contribute

    Clone repo and create a new branch: $ git checkout https://github.com/zaryab520/Dictionary -b name_for_new_branch.
    Make changes and test
    Submit Pull Request with comprehensive description of changes

# Donations

This is free, open-source software. If you'd like to support the development of future projects, contact me at +93 779567151

# License 

 © Netlinks | Designed by Zaryab Merzakhil 
