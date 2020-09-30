import os
from flask import Flask, flash, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import email, smtplib, ssl
import re
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from login import Login
from new_word import New_Word


def authentication():
    return 'users' in session

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name=request.form.get('uname')
        passw=request.form.get('passw')

        try:
            login = Login.query.filter_by(email= name).filter_by(password= passw).first()

            if login is not None:
                session['users'] = str(login.email)
                return render_template("translate.html")

            else:
                invalid_login = "invalid username or password"
                return render_template("login1.html", invalid=invalid_login)

        except Exception as e:
            return(str(e))

    return render_template("login1.html", invalid="")

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    if request.method == "POST":
        session.pop("users", None)
        return render_template("login1.html")


@app.route("/add",methods=['GET', 'POST'])
def add_new_word():
    if authentication():
        if request.method == 'POST':
            english_word=request.form.get('english_word')
            englishWord = english_word.upper()
            dari_translate=request.form.get('dari_translate')
            pashto_translate=request.form.get('pashto_translate')

            try:
                eng_word = New_Word.query.filter_by(english_word= englishWord).first()

                if eng_word is not None:
                    word_exists = "The word already exists!"
                    return render_template("translate.html", mesg=word_exists)

                else:
                    new_word=New_Word(
                        english_word=englishWord,
                        dari_translate=dari_translate,
                        pashto_translate=pashto_translate
                    )
                    db.session.add(new_word)
                    db.session.commit()

                    # send email to users
                    subject = "New word"
                    body ="Dear user,\n\n New word is added to Language Dictionary learn and use.\
 Stay with us and get updated about the latest words added to English world\n\n\
The word for today:\n"\
+english_word+"             "+dari_translate+"              "+pashto_translate+"\n\n"\
"We care about you, our mission is to help people learn English.\n\n \
Best regards,\n team Language Dictionary"
                    sender_email = "zaroahmad72@gmail.com"
                    password = "Netlinks@123"
                    message = MIMEMultipart()
                    message["From"] = sender_email
                    message["Subject"] = subject
                    message.attach(MIMEText(body, "plain"))
                    text = message.as_string()
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                        server.login(sender_email, password)

                        try:
                            users = db.session.query(Login.email).all()
                            for email in users:
                                server.sendmail(sender_email, email, text)

                        except Exception as e:
                            return(str(e))

                    word_added = "word added successfully"
                    return render_template("translate.html", mesg=word_added)

            except Exception as e:
                return(str(e))

        return render_template("translate.html", mesg="")
    else:
        return render_template("login1.html")


@app.route("/get",methods=['GET', 'POST'])
def translate():
    if authentication():
        if request.method == 'POST':
            english_word= request.form.get("english_word")
            englishWord = english_word.upper()
            foreign_lang = request.form.get("origin_language")
            select = request.form.get("language")

            if foreign_lang == "english" and select == "dari":
                try:
                    english_word=New_Word.query.filter_by(english_word=englishWord).first()
                    if english_word is not None:
                        return render_template("translate.html", translation=english_word.dari_translate)

                    else:
                        return render_template("translate.html", translation="Not found")

                except Exception as e:
                    return(str(e))

            elif foreign_lang == "english" and select == "Pashto":
                try:
                    english_word=New_Word.query.filter_by(english_word=englishWord).first()

                    if english_word is not None:
                        return render_template("translate.html", translation=english_word.pashto_translate)
                    else:
                        return render_template("translate.html", translation="Not found")

                except Exception as e:
                    return(str(e))

            elif foreign_lang == "dari" and select == "english":
                try:
                    dari_translate=New_Word.query.filter_by(dari_translate=englishWord).first()

                    if dari_translate is not None:
                        return render_template("translate.html", translation=dari_translate.english_word)
                    else:
                        return render_template("translate.html", translation="Not found")

                except Exception as e:
                    return(str(e))
            
            elif foreign_lang == "pashto" and select == "english":
                try:
                    pashto_translate=New_Word.query.filter_by(pashto_translate=englishWord).first()

                    if pashto_translate is not None:
                        return render_template("translate.html", translation=pashto_translate.english_word)
                    else:
                        return render_template("translate.html", translation="Not found")

                except Exception as e:
                    return(str(e))

        return render_template("translate.html",translation="")
    else:
        return render_template("login1.html")


@app.route("/forgotpass",methods=['GET', 'POST'])
def forgot_pass():
    if request.method == "POST":
        email_add = request.form.get("email_add")
        session['email'] = str(email_add)
        otp = random.randint(999,9999)
        session['otp'] = str(otp)

        try:
            emailadd = Login.query.filter_by(email= email_add).first()

            if emailadd is None:
                invalid_email = "email does not exists"
                return render_template("forgotpass.html", not_found=invalid_email)

            else:
                # email otp to user
                subject = "Do not reply"
                body ="Please have your one time Password (OTP) to reset your password  " +str(otp)
                sender_email = "zaroahmad72@gmail.com"
                receiver_email = email_add
                password = "Netlinks@123"
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject
                message["Bcc"] = receiver_email
                message.attach(MIMEText(body, "plain"))
                text = message.as_string()
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, text)
                    return render_template("enter_otp.html")

        except Exception as e:
            return(str(e))

    return render_template("forgotpass.html",not_found="")



@app.route("/otp", methods=['GET', 'POST'])
def otp():
    if request.method == "POST":
        entered_otp=request.form.get('otp')
        session_value = session.get('otp')

        if entered_otp == session_value:
            session.pop('otp', None)
            return render_template("resetpass.html")

        else:
            return "incorrect otp, try again"

    return render_template("enter_otp.html")


@app.route("/resetpass", methods=['GET', 'POST'])
def reset_pass():
    if request.method == "POST":
        new_pass=request.form.get('new_pass')
        re_pass=request.form.get('re_pass')
        email = session.get('email')

        if new_pass == re_pass:
            try:
                user_name = Login.query.filter_by(email=email).first()
                user_name.password = str(new_pass)
                db.session.commit()
                session.pop('email',None)
                return render_template("login1.html")

            except Exception as e:
                return(str(e))
        else:
            not_match = "password does not match"
            return render_template("resetpass.html", msg = not_match)

    return render_template("resetpass.html", msg="")



@app.route("/register",methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email=request.form.get('uname')
        password=request.form.get('passw')

        try:
            emailadd = Login.query.filter_by(email= email).first()
            if emailadd is not None:
                email_exist = "This email is already registered"
                return render_template("register.html", response=email_exist)
            
            else:
        
                new_user=Login(
                    email=email,
                    password=password
                )
                db.session.add(new_user)
                db.session.commit()
                #send email to new registered user
                email_add = request.form.get("uname")
                subject = "[Language Dictionary] You have successfully registred"
                body ="Greetings of the day,\n\n Thank you For registering With Language Dictionary!\
 we are here to help you learn English. You will be notified about latest updates in English \
world.\n\n best regards, \n team Language Dictionary "

                sender_email = "zaroahmad72@gmail.com"
                receiver_email = email
                password = "Netlinks@123"
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject
                message["Bcc"] = receiver_email
                message.attach(MIMEText(body, "plain"))
                text = message.as_string()
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, text)
                    registred = "You have successfully registered"
                return render_template("register.html", response=registred)
        except Exception as e:
            return(str(e))

    return render_template("register.html", response="")