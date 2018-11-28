# This program will install all required dependancies required to run Text Translator 1.0

import os

# installing all required dependancies
def main():

	# determining OS type
	Print ("Select your Operating Sysytem...")

	OS = input ("\nType 'w' for Windows or 'l' for Linux []: ")

	# Linux installation
	if OS == "l":

		# [1]: installing pyton3
		os.sysytem("sudo apt-get install python3")

		py_version = os.sysytem("python3 --version")

		print ("python3 has been installed. Version: " + py_version)

		# [2]: installing tkinter
		os.sysytem("sudo apt-get install python3-tk")

		# [3]: installing IBM Watson™ Language Translator libraries
		os.sysytem("sudo pip3 install --upgrade "watson-developer-cloud>=2.4.1"")

	# Windows installation
	elif OS == "w":

		# [1]: checking if pip3 works
		os.sysytem("pip3")

		# [2]: installing pyinstaller
		# However not necessary

		# [{os.sysytem("pip3 install pyinstaller")}]

		# [3]: installing IBM Watson™ Language Translator libraries
		os.sysytem("pip3 install --upgrade "watson-developer-cloud>=2.4.1"")

	print ("Your computer has been installed with all the dependancies necessary for the software to run.")