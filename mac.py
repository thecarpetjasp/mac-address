#!/usr/bin/env python3
import colorama
import mac_vendor_lookup
from colorama import Fore, Style
from mac_vendor_lookup import MacLookup
def split(word):
    return [char for char in word]

while True:
    try:
        print ("")
        mac_add = input('MAC ADDRESS: ' + Fore.YELLOW)
        print (Style.RESET_ALL)
        result = (MacLookup().lookup(mac_add))
        result_list = split(result)
        for a in range(0, len(result_list) + 2):
            print ("*", end="")
        print (Fore.YELLOW)
        print ("{", result, "}", sep="", end="")
        print (Style.RESET_ALL)
        for a in range(0, len(result_list) + 2):
            print ("*", end="")
        break
    except mac_vendor_lookup.InvalidMacError:
        print (Fore.RED + "INVALID MAC ADDRESS")
        print (Style.RESET_ALL)
        break
    except KeyError:
        print ("NO RESULTS FOUND")
        print (Style.RESET_ALL)
        break
