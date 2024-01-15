import os

# get strings from file
def getstrings(file):
	# open input file in binary mode + create an output file
	with open(file, "rb") as f_in, open(f"{file}_strings", "wb") as f_out:
		while True:
			# read chunk of data from input file
			chunk = f_in.read(1024)
			if not chunk:
				break
			# perform bitwise XOR op on each byte + write result to output file
			encrypted_chunk = bytes(byte ^ 0x39 for byte in chunk)
			f_out.write(encrypted_chunk)
	# open output file in binary mode + return its content
	with open(f"{file}_strings", "rb") as d:
		s = d.read()
		return s

# view hexdump
def hexdumP():
	os.system("ls --color -alF")
	file=input("\nfilename: ")
	aka=input("[+] hit enter to analyze or Q to exit the program [+]")
	os.system(f"hexdump -C {file} | less")

# view strings
def stringZ():
	os.system("ls --color -alF")
	file=input("\nfilename: ")
	aka=input("[+] hit enter to begin or Q to exit the program [+]")
	os.system(f"strings - -n 3 {file} | less")

# calculate SHA256 hash of file
def sha_file():
	os.system("ls --color -alF")
	file=input("filename: ")
	os.system(f"shasum -a 256 {file}")

# calculate MD5 hash of file
def md5_file():
	os.system("ls --color -alF")
	file=input("filename: ")
	os.system(f"md5 {file}")

def random_hash():
	i = input("MD5/SHA256: ")
	if i in ["md5", "sha256"]:
		os.system(f"cat /dev/urandom | strings -n 10 | head -n 1 | {i}sum")
	else:
		print("[!] incorrect option [!]")

# saving output of getstrings()
def save_strings():
	os.system("ls --color -alF")
	file=input("filename: ")
	os.system(f"file {file}")
	getstrings(file)
	print(f"saved strings to {file}_strings")

# fast file analysis (extract strings, looks for keywords related to various tools)
def fast_analysis():
	various = False
	lolbas = False
	winfun = False
	os.system("ls --color -alF")
	file = input("filename: ")
	data = getstrings(file)
	lines = data.split(b'\n')
	for line_num, line in enumerate(lines, start=1):
		if any(keyword in line for keyword in [b"/dev/urandom", b"/dev/random", b"random", b"urandom"]):
			various = True
			print(f"various tools detected in line {line_num}")
		elif any(keyword in line for keyword in [b"/dev/", b"strings", b"cat", b"/bin", b"/var/lib", b"grep", b"echo", b"curl", b"wget", b"nocat", b"sh", b"bash", b"zsh"]):
			lolbas = True
			print(f"LOLBAS tools detected in line {line_num}: {line}")
		elif any(keyword in line for keyword in [b"cmd.exe", b"powershell.exe", b"calc.exe", b".exe", b".ps1", b"whoami", b".hta"]):
			winfun = True
			print(f"Windows functions detected in line {line_num}")

# main func
def main():
	print("""
                                            
                             ,----,         
                           .'   .`|         
                        .'   .'   ;         
  __  ,-.             ,---, '    .' __  ,-. 
,' ,'/ /|             |   :     ./,' ,'/ /| 
'  | |' | ,--.--.     ;   | .'  / '  | |' | 
|  |   ,'/       \    `---' /  ;  |  |   ,' 
'  :  / .--.  .-. |     /  ;  /   '  :  /   
|  | '   \__\/: . .    ;  /  /--, |  | '    
;  : |   ," .--.; |   /  /  / .`| ;  : |    
|  , ;  /  /  ,.  | ./__;       : |  , ;    
 ---'  ;  :   .'   \|   :     .'   ---'     
       |  ,     .-./;   |  .'               
        `--`---'    `---'                   

                                            
1 - hexdump
2 - strings
3 - SHA256 hash
4 - MD5 hash
5 - random SHA256/MD5 value
6 - extract strings
7 - fast analysis

""")
	a=int(input("choose an option from above: "))
	if a == 1:
		hexdumP()
	elif a == 2:
		stringZ()
	elif a == 3:
		sha_file()
	elif a == 4:
		md5_file()
	elif a == 5:
		random_hash()
	elif a == 6:
		save_strings()
	elif a == 7:
		fast_analysis()
	else:
		print(f"[!] {a} is not an option [!]")

# call main
if __name__ == "__main__":
	main()

