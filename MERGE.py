import os

PhoneFiles = {
	"Gmobile": ["059", "099"],
	"Mobifone": ["070", "076", "077", "078", "079", "089", "090", "093"],
	"Vietnamobile": ["056", "058", "092"],
	"Viettel": ["032", "033", "034", "035", "036", "037", "038", "039", "086", "096", "097", "098"],
	"Vinaphone": ["081", "082", "083", "084", "085", "088", "091", "094"]
}

def MERGE(MobileNetwork):
	for prefix in PhoneFiles[MobileNetwork]:
		x = 0
		writeDATA = ""
		while True:
			if x >= 10000000:
				break
			FilePath = os.path.join(MobileNetwork, prefix, str(x)+"-"+str(x+500000))
			if os.path.exists(FilePath):
				print("[+] " + FilePath)
				f = open(FilePath)
				writeDATA += "\n"+f.read()
				f.close()
				os.remove(FilePath)
				x += 500000
			else:
				print("[-] " + FilePath + ": NOT FOUND!!!")
				break
		if writeDATA != "":
			f = open(os.path.join(MobileNetwork, prefix, MobileNetwork+"-"+prefix+".txt"), "w")
			f.write(writeDATA[1:])
			f.close()
			print("==> " + os.path.join(MobileNetwork, prefix, MobileNetwork+"-"+prefix+".txt") + "\n")

def main():
	for MobileNetwork in PhoneFiles:
		MERGE(MobileNetwork)

if __name__ == "__main__":
	main()