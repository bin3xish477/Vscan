#!/usr/bin/env python3

# *****************************  SCAN FILES  ********************************

import json
import requests
from sys import exit


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
		apikey = input('Please enter a valid VirusTotal API key: ')
	# try to make requests
	try:
		# url to request scan results
		url = (f'https://www.virustotal.com/vtapi/v2/file/report\
			?apikey={apikey}&resource={sha256_hash}')
		# storing the reponse
		resp = requests.get(url)
	# if error occurs while making requests
	except:
		print('[-] Error making GET request to VirusTotal')
		exit(0)
	# return json data
	return resp.json()
