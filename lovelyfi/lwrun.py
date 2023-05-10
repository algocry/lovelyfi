from .lib import liblw
import sys

client = liblw.LPUWirelessCLI()

def print_help():
	print("LPU Wifi auto connector")
	print("Version 0.1")
	print("Commands: ")
	print("	1. help : to see this message")
	print("	2. connect : auto login to wifi")
	print("	3. disconnect : auto logout")
	print(" 4. config : to change saved username and password of the wifi")

def main():
	if len(sys.argv) < 2: 
		print("Please provide an arguement to interact or pass help")
		exit(0)

	elif sys.argv[1] == "connect":
		if (client.server_configuration() == 200):
			status_code = client.connect()
			if status_code == 200:
				print("[+] Connection successfull")
			else: print(f"[-] Connection failed with status code {status_code}")
	elif sys.argv[1] == "disconnect":
		status_code = client.logout()
		if status_code == 200:
			print("[-] Logged out successfully")
		else: print("[-] Logging out failed with status code {status_code}")

	elif sys.argv[1] == "config":
		client.config()

	else:
		print_help()