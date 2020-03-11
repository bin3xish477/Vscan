#!/usr/bin/env python3

# *****************************  SCAN FILES  ********************************


import requests
from sys import exit
from colored import fg, attr


# --------------------------------------
''' 
purpose: send a GET request
to VirusTotal to retrieve the 
scan results.
params: - the SHA256 hash of the
file that will be scanned,
- VirusTotal api key to append
to url
'''
# --------------------------------------
def get_scan(sha256_hash, apikey):
	
	# if no API key was passed prompt user for API key
	if not apikey:
		print('[-] You must provide a VirusTotal API key to proceed')
		# get API key
		apikey = input('%sPlease enter a valid VirusTotal API key:%s ' 
										% (fg(196), attr(0)))

	# try to make requests
	try:
		# url to request scan results
		url = f'https://www.virustotal.com/vtapi/v2/file/report'

		# params for requests
		params = {'apikey': apikey, 'resource': sha256_hash}

		# storing the reponse
		resp = requests.get(url, params=params)

		# get returned json data
		resp_json = resp.json()

	# if connection error occurs while making requests
	except requests.exceptions.ConnectionError:
		print('[-] There was a connection error!')

	# if any other issues present themselves
	except:
		print('[-] There was an issue sending the request to VirusTotal')

	# return json data
	return resp_json

