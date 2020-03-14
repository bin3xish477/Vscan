#!/usr/bin/env python3


try:
	import json
	import csv
	from colored import fg, bg, attr
except ImportError as err:
  print(f'Import Error: {err}')


def toCsv(data, outfile='results'):
	"""
	Writes data to a CSV file

		:parameters:

			data (list) : a list of lists containing chosen elements from scan result
										to write to CSV file
			outfile (str) : name of output file, default = 'results'

		:returns:

			none
	"""

	try:
	  with open(outfile + '.csv', 'a+', newline='') as csvfile:
	    # create csv writer object that will write
	    # our data in csv format to our file
	    writeto = csv.writer(csvfile, delimiter=',')

	    # the data passed to this function should be
	    # a list containing lists, where each embedded list
	    # will create its own row within the csv file
	    writeto.writerows(data)
	except:
		FileError()




def toJson(data, outfile='results'):
	"""
	Writes data to a json file

	:parameters:

		data (list) : scan results in JSON form
		outfile (str) : name of output file, default = 'results'

	:returns:

		none
	"""

	try:
	  with open(outfile + '.json', 'a+') as jsonfile:
	    # dump JSON data to JSON FILE
	    json.dump(data, jsonfile)
	except:
		FileError()




def toNorm(data, outfile='results'):
	"""
	Writes data to a text file

	:parameters:

		outfile (str) : name of output file, default = 'results'
		data (dictionary) : dictionary containing selected data

	:returns:

		none
	"""

	try:
	  with open(outfile + '.txt', 'a+') as txtfile:
	  	# retrieve keys and values from dictionary
	  	# and write them to the text file
	    for key, val in data:
	      txtfile.write(key + ': ' + val, end='\n')
	except:
		FileError()



def FileError():
	"""
	Handles possible file errors

		:parameters:
			None

		:returns:
			None
	"""

	# print error message
	print('[-] %s%sAn error occured with a file operation.%s' % (fg(233), bg(9), attr(0)))
	# exit program
	exit(0)
