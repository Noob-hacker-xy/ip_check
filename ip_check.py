import requests
import os
import pprint
while True:
	def ip():
		ip=str(input("\n\n\nEnter Ip Address(noob-hacker-xy) :  "))
		url=f"https://ipapi.co/{ip}/json/"
		r=requests.get(url)
		pprint.pprint(r.json())
	ip()
