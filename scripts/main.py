#!/usr/bin/env python3


__author__  = 'Alexis Rodriguez aka BinexisHATT'
__collab__ = 'Kenny Masuda'
__start__ = 2020_03_07
__end__ = 2020_03
__version__ = '1.0'
__email__ = 'rodriguez10011999@gmail.com'



try:
  import parser
  import scanit
  import fileformat
  import hashlib
  import os
  import json
  from sys import exit
  from time import sleep
  from colored import fg, bg, attr
  import interface
except ImportError as err:
  print(f'Import Error: {err}')



def singleScan(filename, apikey, fileformat):
	"""
	"""
	
	# the contents of the file in bytes
	content = open(filename, 'rb').read()

	# the file generated based on the contents of the file
	file_hash = genSha256(content)

	# send file to get scanned
	scanit.sendFile(file_hash, apikey, filename)

	# notify of wait time
	print('%s\nPlease wait patiently for your results ...\n%s' % (fg(154), attr(0)))
	sleep(2)

	# retrieve the files report
	result = scanit.getReport(file_hash)

	# check if the user wanted the results
	# to be saved as a CSV file
	if fileformat == 'csv':
		result = forCsv(result)

	# check if the user wanted the results
	# to be saved as a jSON file
	elif fileformat == 'json':
		result = forJson(result)

	# check if the user wanted the results
	# to be saved as a normal text file
	elif fileformat == 'norm':
		result = forNorm(result)

	# if the user did not specify a fileformat option
	# print the raw data as json to the console
	else:
		toConsole(result)


	return result



def masScan(filename, apikey, fileformat):
	"""
	"""

	# contains list of results for each
	# file that was scanned
	all_results = []
	# open file containing files to scan
	with open(filename, 'r') as allfiles:

		# notify of wait time
		print('%s\nPlease wait patiently for your results ...\n%s' % (fg(154), attr(0)))
		sleep(2)

		# this list will contain the data
		# from each scan and will be appended
		# to the all_results list
		result = []
		# loop through each file and perform
		# a scan on each one
		for file in allfiles:
			# read the files contents in bytes
			content = open(file, 'rb').read()

			# get the sha256 hash for the file
			file_hash = genSha256(content)

			# send the file to get scanned
			scanit.sendFile(file_hash, apikey, filename)

			# retrieve scan report
			result = scanit.getReport(file_hash)

			# append results from the scans to the all_results list
			# to format the data with respect to the format 
			# the user specified
			all_results.append(result)

		# check if the user wanted the results
		# to be saved as a CSV file
		if fileformat == 'csv':
			all_results = forCsv(result)

		# check if the user wanted the results
		# to be saved as a jSON file
		elif fileformat == 'json':
			all_results = forJson(result)

		# check if the user wanted the results
		# to be saved as a normal text file
		elif fileformat == 'norm':
			all_results = forNorm(result)

		# if the user did not specify a fileformat option
		# print the raw data as json to the console
		else:
			toConsole(all_results)



def forCsv(data):
	"""
	"""
	pass



def forJson(data):
	"""
	"""

	# load data as JSON text
	json_str = json.loads(data)

	# invoke function to store data into
	# JSON file
	fileformat.toJson(json_str)



# --------------------------------------)
''' 
purpose: parse data for normal text file
param: data returned from report
'''
# --------------------------------------)
def forNorm(data):
	"""
	"""

	pass




def toConsole(data):
	"""
	"""

	# load data as JSON text
	json_str = json.loads(data)

	print(json_str['data']['attributes']['last_analysis_stats'])



def genSha256(file_content):
	"""
	"""
	# generating sha256 hash
	file_hash = hashlib.sha256(file_content).hexdigest()
	
	# return the hash
	return file_hash
	


def programName():
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
  'mass_file':   arguments.mass_file,
  'csv':         arguments.csv,
  'json':        arguments.csv,
  'norm':        arguments.norm,
  'output_file': arguments.output_file,
  'apikey':      arguments.apikey,
  'interface':   arguments.interface

  }

  if args_dict['interface']:
  	interface()

  else:
	  # if no file format is passed, this variable will not change
	  fileformat = None
	  # if file format is csv
	  if args_dict['csv']:
	  	fileformat = 'csv'

	  # if file format is json
	  elif args_dict['json']:
	  	fileformat = 'json'

	  # if fileformat is normal
	  elif args_dict['norm']:
	  	fileformat = 'norm'


	  """ initiating scans based on the file that was passed as an argument """

	  # if the f argument was given
	  if args_dict['single_file']:
	  	singleScan(args_dict['single_file'], args_dict['apikey'], fileformat)

	  # if the m argument was given
	  elif args_dict['mass_file']:
	  	masScan(args_dict['mass_scan'], args_dict['apikey'], fileformat)


# begin the program
if __name__ == '__main__':
	try:
		main()
	# handle keyboard interrupt (ctrl+?)
	except KeyboardInterrupt:
		try:
			print('\n[-] %s%sProgram interrupted!%s' % (fg(233), bg(9), attr(0)))
			exit(0)
		except SystemExit:
			os._exit(0)
      
