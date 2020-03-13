#!/usr/bin/env python3


try:
	import subprocess as subp
	from os import getcwd, path, devnull
	from sys import exit
	from colored import fg, attr, bg
except ImportError as err:
  print(f'Import Error: {err}')


API_KEY = ''



def sendFile(sha256_hash, apikey, filename):
	"""
	"""

	global API_KEY
	file_path = path.join(getcwd(), filename)

	# if no API key was passed prompt user for API key
	if not apikey:
		# get API key
		API_KEY = input('%sEnter a valid VirusTotal API key $: %s' 
										% (fg(196), attr(0)))
	else:
		API_KEY = apikey

	# try to make requests
	try:
		# redirect errors to devnull
		DEVNULL = open(devnull, 'w')
		# use curl to send the file to be scanned
		resp = subp.run(f'curl --request POST \
  					--url https://www.virustotal.com/api/v3/files \
  					--header "x-apikey: {API_KEY}" \
  					--form file=@{file_path}', shell=True, stdout=subp.PIPE,
  					stderr=subp.DEVNULL)

	# if connection error occurs while making requests
	except requests.exceptions.ConnectionError:
		print('[-] %s%sThere was a connection error!%s' % (fg(233), bg(9), attr(0)))

	# if any other issues present themselves
	except:
		print('[-] %s%sAn error occured sending file to get scanned%s' % (fg(233), bg(9), attr(0)))



def getReport(sha256_hash):
	"""
	"""

	global API_KEY

	try:
		# redirect errors to devnull
		DEVNULL = open(devnull, 'w')
		# make GET request with curl to get file report
		resp = subp.run(f'curl --request GET \
	  				--url https://www.virustotal.com/api/v3/files/{sha256_hash} \
	  				--header "x-apikey: {API_KEY}"', shell=True, stdout=subp.PIPE,
	  				stderr=subp.DEVNULL)

	except:
		print('[-] %s%sAn error occured retrieving scan report%s' % (fg(233), bg(9), attr(0)))

	return resp.stdout.decode('utf-8')
