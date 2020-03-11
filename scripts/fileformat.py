#!/usr/bin/env python3

# **************************** OUTPUT RESULT TO FILE ****************************

import json
import csv


# 8888888888888888888888888888888
"""
purpose: output data as CSV
params: name of file to create,
        data to write to file
"""
# 8888888888888888888888888888888
def toCSV(filename, data):
	try:
	  with open(filename + '.csv', newline='') as csvfile:
	    # create csv writer object that will write
	    # our data in csv format to our file
	    writeto = csv.writer(csvfile, delimiter=',')
	    
	    # the data passed to this function should be
	    # a list containing lists, where each embedded list
	    # will create its own row within the csv file
	    writeto.writerows(data)
	except:
		handleFileError()



# 8888888888888888888888888888888
"""
purpose: output data as JSON
params: name of file to create,
        data to write to file
"""
# 8888888888888888888888888888888
def toJSON(filename, data):
	try:
	  with open(filename + '.json') as jsonfile:
	    # the response from VirusTotal is already in json
	    # so no need for conversions
	    jsonfile.write(data)
	except:
		handleFileError()



# 8888888888888888888888888888888
"""
purpose: output data as NORMAL
params: name of file to create,
        data to write to file
"""
# 8888888888888888888888888888888
def toNORM(filename, data):
	try:
	  with open(filename + '.txt') as txtfile:
	    # the data passed to this function will be
	    # a dictionary and we'll simply traverse it
	    # and print key,value pairs seperated by colons
	    for key, val in data:
	      txtfile.write(key + ': ' + val, end='\n')
  except:
  	handleFileError()



""" Handling possible file errors """
def handleFileError():
	print('[-] An error occured with a file operation.')
	exit(0)