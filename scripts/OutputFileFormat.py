#!/usr/bin/env python3

import json
import csv


# 8888888888888888888888888888888
# purpose: output data as CSV
# param: name of file to create,
#        data to write to file
# 8888888888888888888888888888888
def toCSV(filename, data):
  with open(filename + '.csv', newline='') as csvfile:
    # create csv writer object that will write
    # our data in csv format to our file
    writeto = csv.writer(csvfile, delimiter=',')
    # the data passed to this function should be
    # a list containing lists, where each embedded list
    # will create its own row within the csv file
    writeto.writerows(data)


# 8888888888888888888888888888888
# purpose:  output data as JSON
# param: name of file to create,
#        data to write to file
# 8888888888888888888888888888888
def toJSON(filename, data):
  with open(filename + '.json') as jsonfile:
    # the response from VirusTotal is already in json
    # so no need for conversions
    jsonfile.write(data)


# 8888888888888888888888888888888
# purpose: output data as NORMAL
# param: name of file to create,
#        data to write to file
# 8888888888888888888888888888888
def toNORM(filename, data):
  with open(filename + '.txt') as txtfile:
    # the data passed to this function will be
    # a dictionary and we'll simply traverse it
    # and print key,value pairs seperated by colons
    for key, val in data:
      txtfile.write(key + ': ' + val)
    
