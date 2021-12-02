import os
import re

def initial():
	MobileNetwork = ""
	prefix = ""
	while True:
		flag = True
		print("""
1. Gmobile
2. Mobifone
3. Vietnamobile
4. Viettel
5. Vinaphone

99. Exit
""")
		value = input("Choose: ")
		if value == "1":
			MobileNetwork = "Gmobile"
			while True:
				flag1 = True
				print("""
1. 059 ({} B)
2. 099 ({} B)

0. Back
""".format(os.path.getsize(os.path.join("regularly", MobileNetwork+"-059.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-099.txt"))))
				value = input("Choose: ")
				if value == "1":
					prefix = "059"
				elif value == "2":
					prefix = "099"
				elif value == "0":
					flag = False
				else:
					flag1 = False
				if flag1:
					break
		elif value == "2":
			MobileNetwork = "Mobifone"
			while True:
				flag1 = True
				print("""
1. 070 ({} B)
2. 076 ({} B)
3. 077 ({} B)
4. 078 ({} B)
5. 079 ({} B)
6. 089 ({} B)
7. 090 ({} B)
8. 093 ({} B)

0. Back
""".format(os.path.getsize(os.path.join("regularly", MobileNetwork+"-070.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-076.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-077.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-078.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-079.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-089.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-090.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-093.txt"))))
				value = input("Choose: ")
				if value == "1":
					prefix = "070"
				elif value == "2":
					prefix = "076"
				elif value == "3":
					prefix = "077"
				elif value == "4":
					prefix = "078"
				elif value == "5":
					prefix = "079"
				elif value == "6":
					prefix = "089"
				elif value == "7":
					prefix = "090"
				elif value == "8":
					prefix = "093"
				elif value == "0":
					flag = False
				else:
					flag1 = False
				if flag1:
					break
		elif value == "3":
			MobileNetwork = "Vietnamobile"
			while True:
				flag1 = True
				print("""
1. 056 ({} B)
2. 058 ({} B)
3. 092 ({} B)

0. Back
""".format(os.path.getsize(os.path.join("regularly", MobileNetwork+"-056.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-058.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-092.txt"))))
				value = input("Choose: ")
				if value == "1":
					prefix = "056"
				elif value == "2":
					prefix = "058"
				elif value == "3":
					prefix = "092"
				elif value == "0":
					initial()
				elif value == "0":
					flag = False
				else:
					flag1 = False
				if flag1:
					break
		elif value == "4":
			MobileNetwork = "Viettel"
			while True:
				flag1 = True
				print("""
1. 032 ({} B)
2. 033 ({} B)
3. 034 ({} B)
4. 035 ({} B)
5. 036 ({} B)
6. 037 ({} B)
7. 038 ({} B)
8. 039 ({} B)
9. 086 ({} B)
10. 096 ({} B)
11. 097 ({} B)
12. 098 ({} B)

0. Back
""".format(os.path.getsize(os.path.join("regularly", MobileNetwork+"-032.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-033.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-034.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-035.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-036.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-037.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-038.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-039.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-086.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-096.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-097.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-098.txt"))))
				value = input("Choose: ")
				if value == "1":
					prefix = "032"
				elif value == "2":
					prefix = "033"
				elif value == "3":
					prefix = "034"
				elif value == "4":
					prefix = "035"
				elif value == "5":
					prefix = "036"
				elif value == "6":
					prefix = "037"
				elif value == "7":
					prefix = "038"
				elif value == "8":
					prefix = "039"
				elif value == "9":
					prefix = "086"
				elif value == "10":
					prefix = "096"
				elif value == "11":
					prefix = "097"
				elif value == "12":
					prefix = "098"
				elif value == "0":
					flag = False
				else:
					flag1 = False
				if flag1:
					break
		elif value == "5":
			MobileNetwork = "Vinaphone"
			while True:
				flag1 = True
				print("""
1. 081 ({} B)
2. 082 ({} B)
3. 083 ({} B)
4. 084 ({} B)
5. 085 ({} B)
6. 088 ({} B)
7. 091 ({} B)
8. 094 ({} B)

0. Back
""".format(os.path.getsize(os.path.join("regularly", MobileNetwork+"-081.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-082.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-083.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-084.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-085.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-088.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-091.txt")), os.path.getsize(os.path.join("regularly", MobileNetwork+"-094.txt"))))
				value = input("Choose: ")
				if value == "1":
					prefix = "081"
				elif value == "2":
					prefix = "082"
				elif value == "3":
					prefix = "083"
				elif value == "4":
					prefix = "084"
				elif value == "5":
					prefix = "085"
				elif value == "6":
					prefix = "088"
				elif value == "7":
					prefix = "091"
				elif value == "8":
					prefix = "094"
				elif value == "0":
					flag = False
				else:
					flag1 = False
				if flag1:
					break
		elif value == "99":
			exit()
		else:
			flag = False
		if flag:
			break
	return MobileNetwork, prefix

def update(MobileNetwork, prefix):
	FilePath = os.path.join("regularly", MobileNetwork+"-"+prefix+".txt")
	f = open(FilePath)
	data = list(set(f.read().split("\n")))
	f.close()
	FilePath1 = os.path.join(MobileNetwork, prefix, MobileNetwork+"-"+prefix+".txt")
	f = open(FilePath1)
	writeDATA = f.read().split("\n")
	f.close()
	index = 0
	while True:
		if index >= len(data):
			break
		if re.findall("^"+prefix+"\d{7}$", data[index]):
			try:
				print("[+] " + str(index+1) +") Deleting \"" + data[index] + "\" from " + FilePath1)
				writeDATA.remove(data[index])
			except Exception as e:
				print("==> " + data[index] + ": NOT FOUND!!!")
			index += 1
		else:
			print("[-] Deleting \"" + data[index] + "\" from " + FilePath)
			data.remove(data[index])
	print("==> " + str(len(data+writeDATA)))
	writeDATA = "\n".join(data+writeDATA)
	f = open(FilePath1, "w")
	f.write(writeDATA)
	f.close()
	f = open(FilePath, "w")
	f.write("")
	f.close()

def main():
	MobileNetwork, prefix = initial()
	update(MobileNetwork, prefix)
	

if __name__ == "__main__":
	main()