import os
import os
import colorama
from colorama import Fore, Style

os.system("sudo pip3 install -r requirements.txt")
os.system("sudo chmod +x mac.py")
os.system("sudo mv mac.py /usr/bin/mac")
os.system("clear")

print ("Setup complete.")
print ("Type", Fore.YELLOW + "mac", Style.RESET_ALL + "anywhere in your terminal to run this program.")
print ("")
print (Fore.GREEN + "You can now delete this folder")
