#!/usr/bin/env python3

# ************************* COMMAND & CONTROL *********************************
# Author : Alexis Rodriguez
# Started : 2020-03-10
# Ended : 2020-03-

try:
  import sys
  import os
  import parser
  import scanit
  import fileformat
  import hashlib
except ImportError:
  raise ImportError('Error importing module... try "pip3 install -r requirements.txt"')



# 88888888888888888888888888888888888888
''' 
purpose: perform a single scan on a file
passed as an argument
param: name of the file to scan
'''
# 88888888888888888888888888888888888888
def singleScan(filename, apikey):

	content = open(filename, 'rb').read()

	file_hash = genSha256(content)

	result = scanit.get_scan(file_hash, apikey)

	return result



# 88888888888888888888888888888888888888
''' 
purpose: perform a mass scan on all
files contained within a single file
param: - file containing list of files
				to scan for viruses
				- VirusTotal API key
'''
# 88888888888888888888888888888888888888
def masScan(filename, apikey):

	result_lst = []
	# open file containing files to scan
	with open(filename, 'r') as allfiles:
		# loop through each file and perform
		# a scan on each one
		for file in allfiles:
				content = open(file, 'rb').read()

				file_hash = genSha256(content)

				result = scanit.get_scan(file_hash)

				result_lst.append(result)


# 88888888888888888888888888888888888888
''' 
purpose: parse data for JSON file
param: data returned from GET requests
'''
# 88888888888888888888888888888888888888
def forJSON(data):

	pass



# 88888888888888888888888888888888888888
''' 
purpose: parse data for CSV file
param: data returned from GET requests
'''
# 88888888888888888888888888888888888888
def forCSV(data):

	pass



# 88888888888888888888888888888888888888
''' 
purpose: parse data for normal text file
param: data returned from GET requests
'''
# 88888888888888888888888888888888888888
def forNORM(data):

	pass



# 88888888888888888888888888888888888888
''' 
purpose: generate sha256 hash to send
as to VirusTotal to be scanned
param: file contents read as bytes
'''
# 88888888888888888888888888888888888888
def genSha256(file_content):

	file_hash = hashlib.sha256(file_content).hexdigest()
	
	return file_hash
	


def program_name():
	print('''
██╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗    ██╗   ██╗ ██╗    ██████╗ 
██║   ██║██╔════╝██╔════╝██╔══██╗████╗  ██║    ██║   ██║███║   ██╔═████╗
██║   ██║███████╗██║     ███████║██╔██╗ ██║    ██║   ██║╚██║   ██║██╔██║
╚██╗ ██╔╝╚════██║██║     ██╔══██║██║╚██╗██║    ╚██╗ ██╔╝ ██║   ████╔╝██║
 ╚████╔╝ ███████║╚██████╗██║  ██║██║ ╚████║     ╚████╔╝  ██║██╗╚██████╔╝
  ╚═══╝  ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝      ╚═══╝   ╚═╝╚═╝ ╚═════╝
''')



def main():
	# get arguments
  arguments = parser.ParseArgs()

  # dict containing values of arguments passed
  args_dict = {
  'single_file': arguments.single_file,
  'mass_file': arguments.mass_file,
  'csv': arguments.csv,
  'json': arguments.csv,
  'norm': arguments.norm,
  'output_file': arguments.output_file,
  'apikey': arguments.apikey
  }

  if args_dict['single_file']:
  	file_hash = singleScan(args_dict['single_file'])
  	


  elif args_dict['mass_file']:
  	results = masScan(args_dict['mass_scan'])








if __name__ == '__main__':
	try:
		main()
	# handle keyboard interrupt (ctrl+?)
	except KeyboardInterrupt:
		try:
			print('The program has been interrupted.')
			sys.exit(0)
		except SystemExit:
			os._exit(0)
      
