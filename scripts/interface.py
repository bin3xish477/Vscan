#!/usr/bin/env python3

try:
	import main
	from sys import exit
except ImportError:
	print('[-] Could not find the main file...')
	exit(1)


def interface():
	"""
	Creates Vscan's interface

		:param:

			none

		:returns:

			none
	"""
	file_option = input("Would you like to scan more than one file? \033[31mY/n\033[0m ")
	
	if file_option.lower() == 'n':
		file_name = input("\033[33mEnter the name of the file to be scanned\033[0m: ")
	else:
		file_name = input("\033[32mEnter the file containing a list to files to scan\033[0m: ")
	
	to_file = input("Would you like to save your results to a file? \033[31mY/n\033[0m ")
	
	if to_file.lower() == 'y':
		output_file_name = input("\033[33mEnter output file name (without extension)\033[0m: ")
		file_type = input("File output type \033[34m(txt, csv, or json)\033[0m? ")
		
	api_key = input("\033[31mTo proceed, enter a valid VirusTotal API key\033[0m: ")
	to_email = input("Would you like to send your report as an email? \033[31mY/n\033[0m ")
		
	if file_option.lower() == 'n':
		if to_file.lower() == 'y':
			main.singleScan(file_name, api_key, file_type, out_file=output_file_name)
		else:
			main.singleScan(file_name, api_key)
	else:
		if to_file.lower() == 'y':
			main.masScan(file_name, api_key, file_type, out_file=output_file_name)
		else:
			main.masScan(file_name, api_key)
		
	if to_email.lower() == 'y':
		main.sendReport()
	




