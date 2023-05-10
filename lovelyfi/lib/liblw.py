import requests
import json
import os

class LPUWirelessCLI:
	
	USERNAME = None
	PASSWORD = None
	if os.sys.platform=="linux" or os.sys.platform=="darwin":
		CRED_FILE = f'{os.path.dirname(__file__)}/../lwconfig.json'
	else:
		CRED_FILE = f'{os.path.dirname(__file__)}\\..\\lwconfig.json'

	def __init__(self):
		with open(self.CRED_FILE, 'r') as f:
			dic = json.load(f)
			if dic.get('LWUNAME') == None or dic.get('LWPASS') == None:
				self.config()

			self.USERNAME = dic.get('LWUNAME')
			self.PASSWORD = dic.get('LWPASS')

	def config(self):
		print("[-] WIFI not configured properly. Please enter your credentials.")
		username = str(input("Enter username: "))
		password = str(input("Enter password: "))
		dic = {}
		dic['LWUNAME'] =  username
		dic['LWPASS'] = password
		with open(self.CRED_FILE, 'w') as f:
			json.dump(dic, f)
			print("[+] WIFI configured.")

	def server_configuration(self):
		print("[+] Configuring server")
		url = 'https://internet.lpu.in/24online/servlet/E24onlineHTTPClient'
		headers = {
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
			'Content-Type': 'application/x-www-form-urlencoded',
		}
		cookies = {
			'_RoomNo':'',
			'_Pass': '',
			'_UserName': ''
		}
		data = f'mode=191&isAccessDenied=null&url=null&message=&regusingpinid=&checkClose=1&sessionTimeout=0&guestmsgreq=false&logintype=2&orgSessionTimeout=0&chrome=-1&alerttime=null&timeout=0&popupalert=0&dtold=0&mac=&servername=&temptype=&selfregpageid=&leave=no&macaddress=&ipaddress=&username={self.USERNAME}%40lpu.com&password={self.PASSWORD}&loginotp=false&logincaptcha=false&registeruserotp=false&registercaptcha=false'
		res = requests.post(url=url, headers=headers, cookies=cookies, data=data)
		if 'Wrong username/password' in res.content.decode('utf-8'):
			self.config()
			return
		return res.status_code

	def connect(self):
		print("[+] Connecting...")
		url = f'https://internet.lpu.in/24online/webpages/liverequest.jsp?username={self.USERNAME}@lpu.com&isfirsttime=true&r=1683695896134' 
		headers = {
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
		}
		cookies = {
			'_RoomNo':'',
			'_Pass': '',
			'_UserName': ''
		}
		res = requests.get(url=url, headers=headers, cookies=cookies)
		return res.status_code

	def logout(self):
		print("[-] Logging out.")
		url = 'https://internet.lpu.in/24online/servlet/E24onlineHTTPClient'
		headers = {
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
			'Content-Type': 'application/x-www-form-urlencoded' 

		}
		cookies = {
			'_RoomNo':'',
			'_Pass': '',
			'_UserName': ''
		}

		data = f'mode=193&isAccessDenied=null&url=null&message=&regusingpinid=&checkClose=1&sessionTimeout=0&guestmsgreq=false&logintype=2&orgSessionTimeout=0&chrome=1&alerttime=-11&timeout=0&popupalert=1&dtold=0&mac=&servername=&temptype=&selfregpageid=&leave=no&macaddress=&ipaddress=&loggedinuser={self.USERNAME}%40lpu.com&username={self.USERNAME}%40lpu.com&logout=Logout&saveinfo='
		res = requests.post(url=url, headers=headers, cookies=cookies, data=data)
		return res.status_code