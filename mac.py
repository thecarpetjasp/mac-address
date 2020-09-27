#!/usr/bin/env python3
import mac_vendor_lookup
from mac_vendor_lookup import MacLookup
print ("")
mac_add = input('MAC ADDRESS: ')
print ("")
print ("**********")
print (MacLookup().lookup(mac_add))
print ("**********")
