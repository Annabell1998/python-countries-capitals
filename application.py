# Aqui escribe tu codigo
import os
import sys
from collections import OrderedDict
from smtplib import SMTP
import getpass
#LIST = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","","o","p","q","r","s","t","u","v","w","x","y","z"," "]
COUNTR_AND_CAP = {}
ORDERED = {}
def welcome():
	clear()
	print "**** WELCOME!!! **** ".center(58)
	print "-----------------COUNTRIES AND CAPITASL-------------"
def menu():
	print """ 
	what do you want to do?
	  1) insert Country 
	  2) Countries list
	  3) Capitals List 
	  4) Countries and Capitals list
	  5) Countries and Capitals ordered by Capitals
	For the first option you must type "Country" or "1",
	for the second "Countries" or "2",
	for the third "Capitals" or "3",
	for the fourth "All" or "4",
	fot the fifth  "AllOrdered" or "5",
	for the sixth "AllMail" or "6", 
	type exit if you want go out."""
	OPTION = raw_input("enter the option that you want to choose: ")
	option(OPTION)
def option(OPTION):
	OPTION = OPTION.lower()
	if OPTION == "country" or OPTION == "1":
		clear()
		print "you Choose:'insert Country'"
		dictionary()
	elif OPTION == "countries" or OPTION == "2":
		clear()
		print "You Choose:'Countries list'"
		countries()
	elif OPTION == "capitals" or OPTION == "3":
		clear()
		print "You Choose:'Capitals List'"
		capitals()
	elif OPTION == "all" or OPTION == "4":
		clear()
		print "You Choose: 'Countries and Capitals list'"
		All()
	elif OPTION == "allordered" or OPTION == "5":
		print "You Choose: 'Countries and Capitals ordened by Capitals'"
		order()
	elif OPTION == "exit":
		clear()
		print "See you later, comback soon"
		exit()
	elif OPTION == "allmail" or OPTION == "6":
		mail()
	else: 
		clear()
		print "I don't understand"
		menu()
def dictionary():
	COUNTRY = raw_input("Enter the country: ")
	COUNTRY = COUNTRY.title()
	if str(COUNTRY).isalpha() == True or " " in COUNTRY:
		true = True
		while true == True:
			CAPITALS = raw_input ("Enter the capital: ")
			CAPITALS = CAPITALS.title()
			if str(CAPITALS).isalpha() == True or " " in CAPITALS:
				COUNTR_AND_CAP[COUNTRY] = CAPITALS
				true = False
			else: 
				print "only Words please"
				true = True
	else:
		print "only word please"
		dictionary()
	yes = True
	while yes == True:
		CHOOSE = raw_input("do you wish to keep entering countries and capitals? Y/N ")
		if CHOOSE == "Y" or CHOOSE == "y":
			yes = False
			dictionary()
			break
		elif CHOOSE == "N" or CHOOSE == "n":
			clear()
			print "Okay let's go to the menu"
			yes == False
			menu()
			break
		else:
			print "You can only enter Y/N"
			yes = True
def countries():
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
	if COUNTR_AND_CAP == {}:
		print "You don't have countries or capitals"
		dictionary()
	else:
		print "The Capitals are:"
		for i in COUNTR_AND_CAP:
			print COUNTR_AND_CAP[i]
		raw_input("return to the menu, press enter")
		clear()
		menu()
def All():
	if COUNTR_AND_CAP == {}:
		print "You don't have countries or capital"
		dictionary()
	else:
		print "The Country".center(18),"The capital:".center(18)
		for i in COUNTR_AND_CAP:
			print i.center(18),COUNTR_AND_CAP[i].center(18)
		raw_input("return to the menu, press enter")
		clear()
		menu()
def order():
	#print "We are Working... Sorry"
	if COUNTR_AND_CAP == {}:
		print "You don't have Countries or Capitals"
		dictionary()
	else:
		print "the Capitals".center(20), "The Country :".center(20)
		ordered = OrderedDict(sorted(COUNTR_AND_CAP.items(), key=lambda x: x[1:]))
    	for k , v in ordered.items():
        	print k.center(20), v.center(20)
        	ORDERED[k]=v
    	raw_input("return to the menu,press enter")
    	clear()
    	menu()
def mail():
	if COUNTR_AND_CAP == {}:
		print "You don't have Countries or Capitals"
		dictionary()
	else:
		try:
			EnviarCorreo = SMTP()
			EnviarCorreo.connect("smtp.gmail.com", 587)
			EnviarCorreo.ehlo()
			EnviarCorreo.starttls()
			EnviarCorreo.ehlo()
			Direccion_Remi = raw_input("Enter your e-mail: ")
			password = getpass.getpass("Enter Your Password: ")
			Direccion_Desti = raw_input("Enter the email address of the recipient: ")
			Asunto_Mensaje = raw_input("Subject: ")
			EnviarCorreo.login(Direccion_Remi, password)
			Cabecera = 'To:' + Direccion_Desti + '\n'     
			Cabecera += 'From: ' + Direccion_Remi + '\n'
			Cabecera += 'Subject: ' + Asunto_Mensaje + '\n'+'\n'
			CuerpoMensaje = All() + '\n' + '\n'
			EnviarCorreo.sendmail(Direccion_Remi, Direccion_Desti, Cabecera + CuerpoMensaje)
			print ""
			#smtpserver.close()
			mail()
		except smtplib.SMTPAuthenticationError:
			print "Username or Password not accepted."


def clear():
	os.system("reset")
def exit():
	sys.exit()
welcome()
menu()