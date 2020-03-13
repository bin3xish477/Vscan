#!/usr/bin/env python3

# *****************************  SCAN FILES  ********************************


import requests
from sys import exit
from time import sleep
from colored import fg, attr, bg


API_KEY = ''


# --------------------------------------
''' 
purpose: send file to get scanned
params: - the SHA256 hash of the
file that will be sent,
VirusTotal api key to use,
the name of the file to send
'''
# --------------------------------------
def sendFile(sha256_hash, apikey, filename):
	
	global API_KEY
	# if no API key was passed prompt user for API key
	if not apikey:
		# get API key
		API_KEY = input('%sEnter a valid VirusTotal API key $: %s' 
										% (fg(196), attr(0)))
	else:
		API_KEY = apikey
	# try to make requests
	try:
		with open(filename, 'rb') as scanfile:
			# url to upload files for scanning
			url = f'https://www.virustotal.com/api/v3/files'
			# sending api key as data
			data = {'x-apikey': API_KEY}
			# storing the reponse
			resp = requests.post(url, data=data, files=scanfile)
			# notify of wait time
			print('%sPlease wait 5 seconds...%s' % (fg(154), attr(0)))
			sleep(5)
			# get returned json data
			resp_json = resp.json()

	# if connection error occurs while making requests
	except requests.exceptions.ConnectionError:
		print('[-] %s%sThere was a connection error!%s' % (fg(233), bg(9), attr(0)))

	# if any other issues present themselves
	except:
		print('[-] %s%sThere was an issue sending the request to VirusTotal%s' % (fg(233), bg(9), attr(0)))


# ---------------------------------------
''' 
purpose: 
params: hash of file that will retrieved
'''
# ---------------------------------------
def getReport(sha256_hash):

	global API_KEY
	# url to retrieve file reports from
	url = f'https://www.virustotal.com/api/v3/files/{sha256_hash}'
	# sending api key as data
	data = {'x-apikey': API_KEY}
	# send GET requests
	resp = requests.get(url, data=data)
