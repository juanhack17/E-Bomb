#!/usr/bin/python
import smtplib
import time
import os
import getpass
import sys

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def bomb():
	os.system('clear')
	print bcolors.OKGREEN + '''
                                                          c=====e
                                                             H
   ____________                                         _,,__H____
  (__((__((___()     <- Su EMAIL                       //|       |
 (__((__((___()()_____________________________________// |E-Boomb|
(__((__((___()()()------------------------------------'  |_______|   
__________________________________________________________________   
Si no funciona: Control + C para salir
''' + bcolors.ENDC


os.system('clear')
try:
	file1 = open('Banner.txt', 'r')
	print(' ')
	print bcolors.OKGREEN + file1.read() + bcolors.ENDC
	file1.close()
except IOError:
	print('Banner File not found')

#Input
print(bcolors.WARNING  + '''

 
                            
      [1]   Gmail    [1]    
                            
      [2]   Yahoo    [2]    
                            
     [3]   Outlook    [3]   
                            
  
''' + bcolors.ENDC )
try:
	server = raw_input(bcolors.OKGREEN + '[+] Elije servicio de mensajeria: \n' + bcolors.ENDC)
	user = raw_input(bcolors.OKGREEN + '[+] Tu Email: \n' + bcolors.ENDC)
	pwd = getpass.getpass(bcolors.OKGREEN + '[+] Password: ' + bcolors.ENDC)
	to = raw_input(bcolors.OKGREEN + '[+] Victima: \n' + bcolors.ENDC)
	subject = raw_input(bcolors.OKGREEN + '[+] Titulo (opcional): \n' + bcolors.ENDC)
	body = raw_input(bcolors.OKGREEN + '[+] Mensaje: \n' + bcolors.ENDC)
	nomes = input(bcolors.OKGREEN + '[+] Numero de repeticiones: \n' + bcolors.ENDC)
	no = 0
	message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print bcolors.FAIL + '\nOPERACION CANCELADA \n Si esa no era tu ' + bcolors.ENDC
	sys.exit()

#Gmail

if server == '1' or server == 'gmail' or server == 'Gmail':
	bomb()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + ''' [+] Nombre de usuario incorrecto , comprueba que tu cuenta acepta dispositivos desconocidos
		Hecha un vistazo: https://myaccount.google.com/lesssecureapps ''' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + '[+] Exelente enviados ' + str(no+1) + ' emails [+]' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nOPERACION CANCELADA \n Si esa no era tu ' + bcolors.ENDC
			sys.exit()
		except:
			print "Failed to Send "
	server.close()
	
#Yahoo
elif server == '2' or server == 'Yahoo' or server == 'yahoo':
	server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
	bomb()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + '''[+] Nombre de usuario incorrecto , comprueba que tu cuenta acepta dispositivos desconocidos
		Hecha un vistazo: https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps
		''' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + '[+] Exelente enviados ' + str(no + 1) + ' emails [+]' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nOPERACION CANCELADA \n Si esa no era tu ' + bcolors.ENDC
			sys.exit()
		except:
			print "Failed to Send"
	server.close()
	
#Hotmail/Outlook
elif server == '3' or server == 'outlook' or server == 'Outlook' or server == 'Hotmail' or server == 'hotmail':
	server = smtplib.SMTP("smtp-mail.outlook.com", 587)
	bomb()
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + 'Tu Username o Password es incorrecta, por favor intentalo usando unas credenciales correctas' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + '[+] Exelente enviados ' + str(no + 1) + ' emails [+]' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nOPERACION CANCELADA \n Si esa no era tu ' + bcolors.ENDC
			sys.exit()
		except smtplib.SMTPAuthenticationError:
			print '\n ERROR: Informacion no correcta.'
			sys.exit()
		except:
			print "Failed to Send "
	server.close()
	
else:
	print 'Solo disponible en Outlook , Gmail y Yahoo'
	sys.exit()
