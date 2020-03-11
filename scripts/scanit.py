#!/usr/bin/env python3

# *****************************  SCAN FILES  ********************************
import json
import requests

API_KEY = 'fd50a384922570f4ab387464e3042bf5c15edd2d0f3659122c58a85bb8edec54' # YOUR API KEY GOES HERE!!


# 88888888888888888888888888888888888888
''' 
purpose: send a GET request
         to VirusTotal to retrieve the 
         scan results.
param: the md5 hash of the
       file/s that will be scanned
'''
# 88888888888888888888888888888888888888
def get_scan(sha256_hash):
	# url to request scan results
	url = 'https://www.virustotal.com/vtapi/v2/file/report'
	
	# parameter that will be passed to GET request
	params = {'apikey': API_KEY, 'resource': sha256_hash}

	# storing the reponse
	resp = requests.get(url, params=params)

	# return json data
	return resp.json()
