# Aqui escribe tu codigo
import os
import sys
from operator import itemgetter
#LIST = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","","o","p","q","r","s","t","u","v","w","x","y","z"," "]
COUNTR_AND_CAP = {}
def welcome():
	clear()
	print "**** WELCOME!!! **** "
def menu():
	print """ 
	what do you want to do?
	  1) insert Country 
	  2) Countries list
	  3) Capitals List 
	  4) Countries and Capitals list
	  5) Countries and Capitals ordered by Capitals
	For the first option you must type "Country",
	for the second "Countries",
	for the third "Capitals",
	for the fourd "All"
	fot the last "AllOrdered",
	type exit if you want go out."""
	OPTION = raw_input("enter the option that you want to choose: ")
	option(OPTION)
def option(OPTION):
	OPTION = OPTION.lower()
	if OPTION == "country":
		clear()
		print "you Choose:'insert Country'"
		dictionary()
	elif OPTION == "countries":
		clear()
		print "You Choose:'Countries list'"
		countries()
	elif OPTION == "capitals":
		clear()
		print "You Choose:'Capitals List'"
		capitals()
	elif OPTION == "all":
		clear()
		print "You Choose: 'Countries and Capitals list'"
		All()
	elif OPTION == "allordered":
		print "You Choose: 'Countries and Capitals ordened by Capitals'"
		order()
	elif OPTION == "exit":
		clear()
		print "See you later, comback soon"
		exit()
	else: 
		clear()
		print "I don't understand"
		menu()
def dictionary():
	COUNTRY = raw_input("Enter the country: ")
	if str(COUNTRY).isalpha() == True or " " in COUNTRY:
		true = True
		while true == True:
			CAPITALS = raw_input ("Enter the capital: ")
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
		print "the Country and the capital:"
		for i in COUNTR_AND_CAP:
			print i," = ",COUNTR_AND_CAP[i]
		raw_input("return to the menu, press enter")
		clear()
		menu()
def order():
	print "We are Working... Sorry"
	#if COUNTR_AND_CAP == {}:
	#print "You don't have Countries or Capitals"
	#dictionary()
	#else:
	#print "the Capital and the Country :"
	#items = COUNTR_AND_CAP.items()
	#items.sort(key = itemgetter(1), reverse=True)
	#for i in items:
	#print i," = ",
	#for i in COUNTR_AND_CAP:
	#print i 
	raw_input("return to the menu, press enter")
	clear()
	menu()

def clear():
	os.system("reset")
def exit():
	sys.exit()
welcome()
menu()