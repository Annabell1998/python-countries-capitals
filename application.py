"""This code performs a list of countries and their capitals,
in different ways and also allows you to send that list in a message of gmail"""
import os
import sys
from collections import OrderedDict
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
COUNTR_AND_CAP = {}
ORDERED = {}
def welcome():
    """this is for the WELCOME menssage"""
    clear()
    print "**** WELCOME!!! **** ".center(58)
    print "-----------------COUNTRIES AND CAPITASL-------------"
def menu():
    """the menu fuction"""
    print """
    what do you want to do?
      1) insert country 
      2) Countries list
      3) Capitals List 
      4) Countries and Capitals list
      5) Countries and Capitals ordered by Capitals
      6) All by Mail
    For the first option1 you must type "country" or "1",
    for the second "Countries" or "2",
    for the third "Capitals" or "3",
    for the fourth "All" or "4",
    fot the fifth  "AllOrdered" or "5",
    for the sixth "AllMail" or "6", 
    type exit if you want go out."""
    option1 = raw_input("enter the option that you want to choose: ")
    option(option1)
def option(option1):
    """We verify if the entry is correct"""
    option1 = option1.lower()
    if option1 == "country" or option1 == "1":
        clear()
        print "you Choose:'insert country'"
        dictionary()
    elif option1 == "countries" or option1 == "2":
        clear()
        print "You Choose:'Countries list'"
        countries()
    elif option1 == "capitals" or option1 == "3":
        clear()
        print "You Choose:'Capitals List'"
        capitals()
    elif option1 == "all" or option1 == "4":
        clear()
        print "You Choose: 'Countries and Capitals list'"
        alladd()
    elif option1 == "allordered" or option1 == "5":
        clear()
        print "You Choose: 'Countries and Capitals ordened by Capitals'"
        order()
    elif option1 == "allmail" or option1 == "6":
        clear()
        print "You choose: 'All by Mail'"
        mail()
    elif option1 == "exit":
        clear()
        print "See you later, comback soon"
        out()
    else:
        clear()
        print "I don't understand"
        menu()
def dictionary():
    """Here we can add to the dictionary the capitals and countries"""
    country = raw_input("Enter the country: ")
    country = country.capitalize()
    false = True
    while false == True:
        for i in country:
            if i.isdigit() == False:
                false = False
            else:
                print "only word please"
                dictionary()
                false = True
    cool = True
    while cool == True:
        capitals1 = raw_input("Enter the capital: ")
        capitals1 = capitals1.capitalize()
        for app in capitals1:
            if app.isdigit() == False:
                COUNTR_AND_CAP[country] = capitals1
                cool = False
            else:
                print "only Words please"
                cool = True
                break
    yes = True
    while yes == True:
        choose = raw_input("do you wish to keep entering countries and capitals? Y/N ")
        if choose == "Y" or choose == "y":
            yes = False
            dictionary()
            break
        elif choose == "N" or choose == "n":
            clear()
            print "Okay let's go to the menu"
            yes = False
            menu()
            break
        else:
            print "You can only enter Y/N"
            yes = True
def countries():
    """ print the list of Countries"""
    if COUNTR_AND_CAP == {}:
        print "You don't have countries or capitals"
        dictionary()
    else:
        print "The countries are:"
        for i in COUNTR_AND_CAP:
            print i
        raw_input("return to the menu, press enter")
        clear()
        menu()
def capitals():
    """pirnt the list of Capitals"""
    if COUNTR_AND_CAP == {}:
        print "You don't have countries or capitals"
        dictionary()
    else:
        print "The capitals are:"
        for i in COUNTR_AND_CAP:
            print COUNTR_AND_CAP[i]
        raw_input("return to the menu, press enter")
        clear()
        menu()
def alladd():
    """print the capitals and countries"""
    if COUNTR_AND_CAP == {}:
        print "You don't have countries or capital"
        dictionary()
    else:
        print "The Country".center(18), "The capital:".center(18)
        for i in COUNTR_AND_CAP:
            print i.center(18), COUNTR_AND_CAP[i].center(18)
        raw_input("return to the menu, press enter")
        clear()
        menu()
def order():
    """ print the capitals and the countries in order by the capitals"""
    if COUNTR_AND_CAP == {}:
        print "You don't have Countries or Capitals"
        dictionary()
    else:
        print "the Capitals".center(20), "The country :".center(20)
        ordered = OrderedDict(sorted(COUNTR_AND_CAP.items(), key=lambda x: x[1:]))
        for k, ann in ordered.items():
            print k.center(20), ann.center(20)
            ORDERED[k] = ann
        raw_input("return to the menu,press enter")
        clear()
        menu()
def mail():
    """Send the mail"""
    fromaddr = raw_input("Enter Your E-mail: ")
    password = getpass.getpass("Password: ")
    toaddrs = raw_input("Enter the email address of the recipient: ")
    body = "Countries\t******************\tCapitals\n"
    for msg in COUNTR_AND_CAP:
        body = body + str(msg).center(20) +str(COUNTR_AND_CAP[msg]).center(43) + "\n"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    msg['Subject'] = "Countries and Capitals"
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddrs, text)
        server.quit()
        raw_input("<<<<<<<<<Your message was sent>>>>>>>")
        menu()
    except smtplib.SMTPAuthenticationError:
        raw_input("Your password or email not accepted")
        mail()

def clear():
    """clean the screen"""
    os.system("reset")
def out():
    """go out of the programm"""
    sys.exit()
welcome()
menu()

