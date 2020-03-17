#!/usr/bin/env python3


__author__ = 'Alexis Rodriguez'
__collaborator__ = 'Kenny Masuda'
__start__ = 2020_03_07
__end__ = 2020_03
__version__ = '1.0'
__email__ = 'rodriguez10011999@gmail.com'

try:
	import scanit
	import fileformat
	import hashlib
	import os
	import json
	import parser
	import interface
	import smtplib
	from email.message import EmailMessage
	from getpass import getpass
	from sys import exit
	from time import sleep
	from colored import fg, bg, attr
except ImportError as err:
	print(f'Import Error: {err}')


def singleScan(file_name, apikey, file_format, out_file=None):
	"""
	Sends and scans file using VirusTotal's API

		:parameters:

			file_name (str) : name of file to scan
			apikey (str) : valid VirusTotal API key
			fileformat (str) : type of format to store the report generated by VirusTotal
			outfile (str) : name of file to create if options to create file was provided,
											default = None

		:returns:

			none
	"""

	# the contents of the file in bytes
	content = open(file_name, 'rb').read()

	# the file generated based on the contents of the file
	file_hash = genSha256(content)

	# send file to get scanned
	scanit.sendFile(apikey, file_name)

	# notify of wait time
	print('%s\nPlease wait patiently for your results ...\n%s' % (fg(154), attr(0)))
	sleep(2)

	# retrieve the files report
	result = scanit.getReport(file_hash)

	# check if the user wanted the results
	# to be saved as a CSV file
	if file_format == 'csv':
		forCsv(result, out_file)

	# check if the user wanted the results
	# to be saved as a jSON file
	elif file_format == 'json':
		forJson(result, out_file)

	# check if the user wanted the results
	# to be saved as a normal text file
	elif file_format == 'norm':
		forNorm(result, out_file)

	# if the user did not specify a fileformat option
	# print the raw data as json to the console
	else:
		toConsole(result)


def masScan(file_name, api_key, file_format, out_file=None):
	"""
	Sends and scans multiple files (max is 50) using VirusTotal's API

		:parameters:

			file_name (str) : name of file containing a list of files to scan
			api_key (str) : valid VirusTotal API key
			fileformat (str) : type of format to store the report generated by VirusTotal
			outfile (str) : name of file to create if options to create file was provided,
											default = None

		:returns:

			none
	"""

	# contains list of results for each
	# file that was scanned
	all_results = []
	# open file containing files to scan
	with open(file_name, 'r') as all_files:

		# notify of wait time
		print('%s\nPlease wait patiently for your results ...\n%s' % (fg(154), attr(0)))
		sleep(0.1)

		# this list will contain the data
		# from each scan and will be appended
		# to the all_results list
		result = []
		# loop through each file and perform
		# a scan on each one
		for file in all_files:
			# read the files contents in bytes
			content = open(file, 'rb').read()

			# get the sha256 hash for the file
			file_hash = genSha256(content)

			# send the file to get scanned
			scanit.sendFile(api_key, file_name)

			# retrieve scan report
			result = scanit.getReport(file_hash)

			# append results from the scans to the all_results list
			# to format the data with respect to the format
			# the user specified
			all_results.append(result)

		# check if the user wanted the results
		# to be saved as a CSV file
		if file_format == 'csv':
			forCsv(all_results, out_file)

		# check if the user wanted the results
		# to be saved as a jSON file
		elif file_format == 'json':
			forJson(all_results, out_file)

		# check if the user wanted the results
		# to be saved as a normal text file
		elif file_format == 'norm':
			forNorm(all_results, out_file)

		# if the user did not specify a fileformat option
		# print the raw data as json to the console
		else:
			toConsole(all_results)


def forCsv(data, out_file):
	"""
	Converts the data received from VirusTotal into list containing desired elements
	to send to fileformat.toCsv for writing to CSV file.

		:parameters:

			data (dictionary) : report received for a particualr file
			out_file (str) : name of file to create if options to create file was provided

		:returns:

			none
	"""
	
	
	results = []
	to_append = []
  
	json_str = json.loads(data)
	
	"""  file stats containing overall scan results  """
	antivirus_results = json_str['data']['attributes']

	to_append.append(antivirus_results['last_analysis_stats']['confirmed-timeout'])
	to_append.append(antivirus_results['last_analysis_stats']['failure'])
	to_append.append(antivirus_results['last_analysis_stats']['harmless'])
	to_append.append(antivirus_results['last_analysis_stats']['malicious'])
	to_append.append(antivirus_results['last_analysis_stats']['suspicious'])
	to_append.append(antivirus_results['last_analysis_stats']['timeout'])
	to_append.append(antivirus_results['last_analysis_stats']['type-unsupported'])
	to_append.append(antivirus_results['last_analysis_stats']['undetected'])

	"""   append file metadata  """
	to_append.append(antivirus_results['last_modification_date'])
	to_append.append(antivirus_results['last_submission_date'])
	to_append.append(antivirus_results['magic'])  # filters the type of file to be returned (i.e. magic signature)
	to_append.append(antivirus_results['meaningfule_name'])
	to_append.append(antivirus_results['md5'])
	to_append.append(antivirus_results['sha1'])
	to_append.append(antivirus_results['sha256'])
	to_append.append(antivirus_results['size'])
	to_append.append(antivirus_results['links']['self'])  # the url to find the raw json data

	# append our list containing the result to the final results list
	results.append(to_append)

	# invoke function to write to csv file
	fileformat.toCsv(results)


def forJson(data, out_file):
	"""
	Converts the data received from VirusTotral into a json object to send
	to fileformat.toJson for writing comprehensible json data to a json file

		:parameters:

			data (dictionary) : report received for a particualr file
			out_file (str) : name of file to create if options to create file was provided

		:returns:

			none
	"""

	# load data as JSON text
	json_str = json.loads(data)

	# invoke function to store data into
	# JSON file
	fileformat.toJson(json_str, out_file)

	
def forNorm(data, out_file):
	"""
	Converts the data received from VirusTotral file report into data
	that can be analyzed to send to fileformat.toNorm for writing to a
	normal text file.

		:parameters:

			data (dictionary) : report received for a particualr file
			out_file (str) : name of file to create if options to create file was provided

		:returns:

			none
	"""

	json_dict = json.loads(data)
	engine_results = dict()
	file_stats = dict()

	antivirus_results = json_dict['data']['attributes']['last_analysis_results']

	for engine in antivirus_results.keys():
		engine_results[engine] = antivirus_results[engine]
		engine_results[engine]['engine_update'] = antivirus_results[engine]['engine_update']
		engine_results[engine]['engine_version'] = antivirus_results[engine]['engine_version']
		engine_results[engine]['category'] = antivirus_results[engine]['category']
		engine_results[engine]['method'] = antivirus_results[engine]['method']
		engine_results[engine]['result'] = antivirus_results[engine]['result']

	file_report_stats = json_dict['data']['attributes']['last_analysis_stats']

	file_stats['file_statistics'] = {
		'confirmed-timeout' : file_report_stats['confirmed-timeout'],
		'failure': file_report_stats['failure'],
		'harmless': file_report_stats['harmless'],
		'malicious': file_report_stats['malicious'],
		'suspicious': file_report_stats['suspicious'],
		'timeout': file_report_stats['timeout'],
		'type-unsupported': file_report_stats['type-unsupported'],
		'undetected': file_report_stats['undetected']
	}

	more_stats = json_dict['data']['attributes']

	file_stats['last_modified'] = more_stats['last_modification_date']
	file_stats['last_submitted'] = more_stats['last_submission_date']
	file_stats['magic'] = more_stats['magic']
	file_stats['md5_hash'] = more_stats['md5']
	file_stats['sha1_hash'] = more_stats['sha1']
	file_stats['sha256_hash'] = more_stats['sha256']
	file_stats['type_description'] = more_stats['type_description']

	fileformat.toNorm(engine_results, file_stats)


def toConsole(data):
	"""
	Displays raw data retrieve from VirusTotal's file report

		:parameters:

			data (dictionary) : report received for a particualr file

		:returns:

			none
	"""

	# load data as JSON text
	json_str = json.loads(data)

	# get the data that we are most concerned with
	antivirus_results = json_str['data']['attributes']['last_analysis_results']

	print('[--------------%sScan Report%s-------------]' % (fg(9), attr(0)))  # add some color to this
	for engine in antivirus_results.keys():
		print('+--------------------------------------+')
		print(('\n%sAntivirus Engine:%s ' % (fg(201), attr(0))), str(antivirus_results[engine]['engine_name']))
		print(('%s  Engine Version:%s ' % (fg(112), attr(0))), str(antivirus_results[engine]['engine_version']))
		print(('%s   Engine Update:%s ' % (fg(117), attr(0))), str(antivirus_results[engine]['engine_update']))
		print(('%s        Category:%s ' % (fg(88), attr(0))), str(antivirus_results[engine]['category']))
		print(('%s          Method:%s ' % (fg(130), attr(0))), str(antivirus_results[engine]['method']))
		print(('%s          Result:%s ' % (fg(11), attr(0))), str(antivirus_results[engine]['result']), end='\n\n')

	# get final statistics from the files report
	file_report_stats = json_str['data']['attributes']['last_analysis_stats']

	print('[------------%sFile Stats%s-----------]' % (fg(9), attr(0)))
	print(('%s\nFailure:%s ' % (fg(124), attr(0))), file_report_stats['failure'])
	print(('%sHarmless:%s ' % (fg(124), attr(0))), file_report_stats['harmless'])
	print(('%sMalicious:%s ' % (fg(124), attr(0))), file_report_stats['malicious'])
	print(('%sSuspicious:%s ' % (fg(124), attr(0))), file_report_stats['suspicious'])
	print(('%sTimeout: %s ' % (fg(124), attr(0))), file_report_stats['timeout'])
	print(('%sType-unsupported:%s ' % (fg(124), attr(0))), file_report_stats['type-unsupported'])
	print(('%sUndetected:%s ' % (fg(124), attr(0))), file_report_stats['undetected'], end='\n\n')

	# for specific file metadata
	file_meta = json_str['data']['attributes']

	print('[----------------------%sFile Metadata%s----------------------]' % (fg(9), attr(0)))
	print(('%s\nFirst submitted:%s ' % (fg(201), attr(0))), file_meta['first_submission_date'])
	print(('%sLast Submission Date:%s ' % (fg(201), attr(0))), file_meta['last_submission_date'])
	print(('%sMagic:%s ' % (fg(201), attr(0))), file_meta['magic'])
	print(('%sMd5 hash:%s ' % (fg(201), attr(0))), file_meta['md5'])
	print(('%sSHA1 hash:%s ' % (fg(201), attr(0))), file_meta['sha1'])
	print(('%sSHA256 hash:%s ' % (fg(201), attr(0))), file_meta['sha256'])
	print(('%sTags:%s ' % (fg(201), attr(0))), file_meta['tags'])
	print(('%sSize:%s ' % (fg(201), attr(0))), file_meta['size'])



def genSha256(file_content):
	"""
	Generates SHA256 hash of a specific files contents

		:parameters:

			file_content (str) : all the contents the file as a string

		:returns:

			SHA256 hash of files content
	"""

	# generating sha256 hash and returning it
	return hashlib.sha256(file_content).hexdigest()


def sendReport():
	"""
	Sends files to an gmail account

		:parameters:
			none
		
		:returns:
			none
	"""

	# get files to be sent as email attachment
	FILES = input('%s\nEnter file/s to send seperated by commas $:%s ' % (fg(252), attr(0))).split(',')

	# an object to easily craft an email
	MESSAGE = EmailMessage()

	SENDER = input('%sEnter your gmail account $:%s ' % (fg(75), attr(0)))
	MESSAGE['From'] = SENDER
	# the getpass method will allow a user to enter a password
	# without having to expose password in the clear
	PASSWORD = getpass('%sEnter your password $:%s ' % (fg(190), attr(0)))
	MESSAGE['To'] = input('%sEnter the recipient\'s email account $:%s ' % ( fg(75), attr(0)))
	MESSAGE['Subject'] = input('%sEnter the subject of your email $:%s ' % (fg(129), attr(0)))
	MESSAGE.set_content('Vscan v1.0 file report/s')

	# loop through list of files to send in email
	for file in FILES:
		with open(file, 'rb') as file_to_send:
			file_bytes = file_to_send.read()
			# get the file object name property
			file_name = file_to_send.name
			# attach file to the email we are crafting
			MESSAGE.add_attachment(
				file_bytes,
				maintype='application',
				subtype='octet-stream',
				filename=file_name)

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		try:
			# login in to gmail account
			smtp.login(SENDER, PASSWORD)
			# send email
			smtp.send_message(MESSAGE)
		# handle authentication error
		except smtplib.SMTPAuthenticationError:
			print('[-] %s%sThere was an error authenticating to your account%s' % (fg(233), bg(9), attr(0)))


def main():

	# get arguments
	arguments = parser.parseArgs()

	# dict containing values of arguments passed
	args_dict = {
		'single_file': arguments.single_file,
		'mass_file':   arguments.mass_file,
		'csv':         arguments.csv,
		'json':        arguments.csv,
		'norm':        arguments.norm,
		'output_file': arguments.output_file,
		'api_key':      arguments.api_key,
		'interface':   arguments.interface,
		'email':			 arguments.email
	}

	# if no file arguments were given
	if not args_dict['single_file'] and not args_dict['mass_file']:
		print('[-] no file arguments were passed... please try again!' % (fg(233), bg(9), attr(0)))
		exit(0)

	else:
		if args_dict['interface']:
			interface.interface()

		else:
			# if no file format is passed, this variable will not change
			file_format = None
			# # if file format is csv
			if args_dict['csv']:
				file_format = 'csv'
			# if file format is json
			elif args_dict['json']:
				file_format = 'json'
			# if file_format is normal
			elif args_dict['norm']:
				file_format = 'norm'

		if not file_format:
			if args_dict['single_file']:
				singleScan(
					args_dict['single_file'],  # function arguments
					args_dict['api_key'],
					file_format)

			# if the m argument was given
			else:
				masScan(
					args_dict['mass_file'],  # function arguments
					args_dict['api_key'],
					file_format)

		else:
			if args_dict['single_file']:
				singleScan(
					args_dict['single_file'],  # function arguments
					args_dict['api_key'],
					file_format,
					args_dict['output_file'])

			# if the m argument was given
			else:
				masScan(
					args_dict['mass_file'],  # function arguments
					args_dict['api_key'],
					file_format,
					args_dict['output_file'])

	# if arguments to email was passed, invoke function
	# to send email
	if args_dict['email']:
		sendReport()


def programName():
	print('''
██╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗    ██╗   ██╗ ██╗    ██████╗
██║   ██║██╔════╝██╔════╝██╔══██╗████╗  ██║    ██║   ██║███║   ██╔═████╗
██║   ██║███████╗██║     ███████║██╔██╗ ██║    ██║   ██║╚██║   ██║██╔██║
╚██╗ ██╔╝╚════██║██║     ██╔══██║██║╚██╗██║    ╚██╗ ██╔╝ ██║   ████╔╝██║
 ╚████╔╝ ███████║╚██████╗██║  ██║██║ ╚████║     ╚████╔╝  ██║██╗╚██████╔╝
  ╚═══╝  ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝      ╚═══╝   ╚═╝╚═╝ ╚═════╝
''')


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

