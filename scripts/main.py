#!/usr/bin/env python3

# **********************************************************************
# Author : Alexis Rodriguez
# Started : 2020-03-10
# Ended : 2020-03-
#                          Command & Control
# **********************************************************************

try:
  import sys

  import os

  import parser

  import scanit

  import outputfileformat

  import hashlib

except ImportError:
  raise ImportError('Error importing module... try "pip3 install -r requirements.txt"')



def gen_hash(file_content):
	pass
  


def main():
	# get arguments
  arguments = parser.ParseArgs()

  # dict containing values of arguments passed
  args_dict = {
  'file_to_scan': arguments.single_file,
  'mass_file': arguments.mass_scan,
  'csv': arguments.csv,
  'json': arguments.csv,
  'norm': arguments.norm,
  'output_file': arguments.output_file
  }

  



if __name__ == '__main__':
	try:
		main()
	# handle keyboard interrupt (ctrl+?)
	except KeyboardInterrupt:
		try:
			print('The program has been interrupted.')
			sys.exit(0)
		except SystemExit:
			os._exit(0)
      
