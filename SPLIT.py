import os

PhoneFiles = {
	"Gmobile": ["059", "099"],
	"Mobifone": ["070", "076", "077", "078", "079", "089", "090", "093"],
	"Vietnamobile": ["056", "058", "092"],
	"Viettel": ["032", "033", "034", "035", "036", "037", "038", "039", "086", "096", "097", "098"],
	"Vinaphone": ["081", "082", "083", "084", "085", "088", "091", "094"]
}

def SPLIT(MobileNetwork):
	for prefix in PhoneFiles[MobileNetwork]:
		FilePath = os.path.join(MobileNetwork, prefix, MobileNetwork+"-"+prefix+".txt")
		if os.path.exists(FilePath):
			print("[+] " + FilePath)
			f = open(FilePath)
			data = f.read().split("\n")
			f.close()
			print(os.path.join(MobileNetwork, prefix))
			x = 0
			while True:
				if x >= len(data):
					os.remove(FilePath)
					break
				writeDATA = "\n".join(data[x:x+500000])
				if writeDATA != "":
					f = open(os.path.join(MobileNetwork, prefix, str(x)+"-"+str(x+500000)), "w")
					f.write(writeDATA)
					f.close()
					print("|__ " + str(x)+"-"+str(x+500000))
				x += 500000
		else:
			print("[-] " + FilePath + ": NOT FOUND!!!")

def main():
	for MobileNetwork in PhoneFiles:
		SPLIT(MobileNetwork)

if __name__ == "__main__":
	main()