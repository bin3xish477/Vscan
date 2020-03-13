#!/usr/bin/env python3

# **************************** OUTPUT RESULT TO FILE ****************************


import json
import csv


# -------------------------------
'''
purpose: output data as CSV
params: name of file to create,
data to write to file
'''
# -------------------------------
def toCsv(filename, data):

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
		FileError()



# -------------------------------
'''
purpose: output data as JSON
params: name of file to create,
data to write to file
'''
# -------------------------------
def toJson(filename, data):

	try:
	  with open(filename + '.json') as jsonfile:
	    # the response from VirusTotal is already in json
	    # so no need for conversions
	    json.dump(data, jsonfile)
	except:
		FileError()



# -------------------------------
'''
purpose: output data as NORMAL
params: name of file to create,
data to write to file
'''
# -------------------------------
def toNorm(filename, data):
	
	try:
	  with open(filename + '.txt') as txtfile:
	    # the data passed to this function will be
	    # a dictionary and we'll simply traverse it
	    # and print key,value pairs seperated by colons
	    for key, val in data:
	      txtfile.write(key + ': ' + val, end='\n')
	except:
		FileError()



''' Handling possible file errors '''
def FileError():
	print('[-] An error occured with a file operation.' % (fg(233), bg(9), attr(0)))
	exit(0)