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
			# field identifiers
			csvfile.write('confirmed-timeout,failure,harmless,malicious,suspicious,timeout,type-unsupported\
				undetected,last_modification_date,last_submission_date,magic_signature,meaningful_name,md5\
				sha1,sha256,size,link_for_results\n')
			# create csv writer object that will write
			# our data in csv format to our file
			writeto = csv.writer(csvfile, delimiter=',')

			# the data passed to this function should be
			# a list containing lists, where each embedded list
			# will create its own row within the csv file
			writeto.writerows(data)
	except:
		fileError()


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
			jsonfile.write('[------------------------------Scan Report-----------------------------]\n')
			# dump JSON data to JSON FILE
			json.dump(data, jsonfile)
	except:
		fileError()


def toNorm(engine_results, file_stats, outfile='results'):
	"""
	Writes data to a text file

	:parameters:

		outfile (str) : name of output file, default = 'results'
		engine_results (dictionary) : dictionary containing each antivirus engine results
		file_stats (dictionary) : dictionary containing the statistics and properties of the file

	:returns:

		none
	"""

	try:
		with open(outfile + '.txt', 'a+') as txtfile:
			txtfile.write('[------------Scan Report-------------]')
			# retrieve keys and values from dictionary
			# and write them to the text file
			for engine in engine_results.keys():
				txtfile.write('\n')
				for key, val in engine_results[engine].items():
					txtfile.write('\n')
					txtfile.write(key + ': ' + str(val))

			txtfile.write('\n\n[-------------File Stats-------------]\n')
			for key, val in file_stats.items():
				txtfile.write('\n')
				txtfile.write(key + ': ' + str(val))
			txtfile.write('\n')
	except:
		fileError()


def fileError():
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
