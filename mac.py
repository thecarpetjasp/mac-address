#!/usr/bin/env python3
import colorama
import mac_vendor_lookup
from colorama import Fore, Style
from mac_vendor_lookup import MacLookup
print ("")
mac_add = input('MAC ADDRESS: ' + Fore.YELLOW)
print (Style.RESET_ALL)
print ("******************************")
print (Fore.YELLOW)
print ("{", MacLookup().lookup(mac_add), "}", sep="")
print (Style.RESET_ALL)
print ("******************************")
