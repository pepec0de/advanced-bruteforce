#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import mechanize
import urllib
from core import *

branch = ["0", "Web", "SSH", "FTP", "Proxy"] # main branches
branchs = [[], ["0", "Facebook", "Instagram", "Twitter", "Costum"],[],[],[]] #subBranches of each branch
credits = """\033[1;31m
	}-----{+} Coded By Pepe {+}-----{
     }--------{+}   github.com  {+}--------{
	}-----{+}  /pepesource  {+}-----{\033[1;m
"""
banner = """\033[1;33m
██████╗ ██████╗ ██╗███╗   ██╗██████╗ ██╗   ██╗███████╗██╗ ██╗ █████╗
██╔══██╗██╔══██╗██║████╗  ██║██╔══██╗██║   ██║██╔════╝██║ ██╔╝██╔══██╗
██████╔╝██████╔╝██║██╔██╗ ██║██║  ██║██║   ██║███████╗█████╔╝ ███████║
██╔══██╗██╔══██╗██║██║╚██╗██║██║  ██║██║   ██║╚════██║██╔═██╗ ██╔══██║
██████╔╝██║  ██║██║██║ ╚████║██████╔╝╚██████╔╝███████║██║  ██╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
\033[1;m"""
def clear():
	os.system("clear")
def bruteforceWeb(url, user, wordlist, userF, passwordF, methodF):
	for password in wordlist:
        	response = br.open(url) # The url is openned
	        br.set_response(response) # Set up the response
        	br.open(url)
	        br.select_form( nr = 0 ) # The first form that is found is set
	        br.form[userF] = user # web form to bruteforce
	        br.form[passwordF] = password.strip() # web form to bruteforce
	        br.method = methodForm # form method is set
	        response = br.submit() # data is send
def pChance(x): # method to print a chance based on array[]
	for z in range(1, len(x)):
                print "   {" + str(z) + "}--" + x[z]
        print "   {99}-Exit\n"
def sWeb(x):
	while switch(x):
		if case(1, 2, 3):
			user = inputCostum("Insert username/number/email to crack:")
			print user
			break
		if case(99):
			clear()
			main()
		sWeb(inputChance())
		break
def sSSH():
	print "SSH"
def sFTP():
	print "FTP"
def sProxy():
	print "Proxy"
def sMain(x):
	while switch(x):
	    	if case(1):
        	        pChance(branchs[1])
			sWeb(inputChance())
		        break
    		if case(2):
	        	sSSH()
	        	break
        	if case(3):
	    	    	sFTP()
			break
    		if case(4):
	        	sProxy()
	        	break
		if case(99):
			exit()
			break
    		sMain(inputChance())
		break
def top():
	print banner
	print credits
def branchChance():
	pChance(branch)
	sMain(inputChance())
def inputChance():
	input = raw_input("brinduska~# ")
        try:
		xx = int(input)
	except:
		input = inputChance()
	return int(input)
def inputCostum(msg):
	return raw_input(msg + " ")
def main():
	top()
	branchChance()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "\n{*} Exiting..."
		exit()

