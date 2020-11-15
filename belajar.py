import  os
os.ayatem("clear")
def banner():
print("""
#############
tutorial 01
############
""")

main():
os.system("clear")
banner()
print("1.hack facebook")
print("2.install bahan")
print("0.Exit")
pilih = input("pilih nomor: ")
if pilih == "1":
os.system("git clone https://github.com/irul-ID/MBF")
os.system("cd MBF")
os.system("pyhton2 MBF.py")
elif pilih == "2":
os.system("pip2 install requests")
os.system("pip2 install nechanize")
elif pilih == "0":
exit()

main()
