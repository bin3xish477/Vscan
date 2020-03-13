#!/usr/bin/env python3


try:
	from argparse import ArgumentParser
	from colored import fg, attr, bg
	from sys import argv, exit
	from main import programName
except ImportError as err:
  print(f'Import Error: {err}')



def ParseArgs():
	"""
	Parse arguments passed in the command line

	Parameters:
		None

	Returns:
		arguments passed to command line
	"""

  parser = ArgumentParser(
    description=('%s%s* SCAN FILES FOR VIRUSES WITH VSCAN *%s'%(fg(255),bg(1),attr(0))),
    usage=('vscan %s(-f|--file) [-m|--mass] [--csv]\
                  \n\t     [--json] [--norm] [-o|--output]%s')%(fg(39),attr(0))
  )
  
  required = parser.add_argument_group('%s%s REQUIRED %s'%(fg(255),bg(2),attr(0)))
  parser._optionals.title = ('%s%s OPTIONAL %s'%(fg(255),bg(2),attr(0)))
  
  # the single file a user wants to scan
  required.add_argument(
    '-f', '--file',
    required=True,
    dest='single_file',
    type=str,
    help='file to scan for virus')
  
  # if the user wants to scan more than one file
  parser.add_argument(
    '-m','--mass',
    type=str,
    dest='mass_file',
    help='file containing multiple files to scan (50 files max)\
           \nNote: the timing for multiple scans will depend on the quality of your API key')
  
  # if the user wants wants the output format to be pure csv
  parser.add_argument(
    '--csv',
    action='store_true',
    default=False,
    help='output scan results to file in csv format')

  # if the user wants the output format to be pure json
  parser.add_argument(
    '--json',
    action='store_true',
    default=False,
    help='output scan results to file in json format')
  
  # if the user wants the output format to be normal text
  parser.add_argument(
    '--norm',
    action='store_true',
    default=False,
    help='output scan results to file with a normal format')
  
  # the output file name to create when user chooses
  # to output scan results to file (json, csv, or normal)
  parser.add_argument(
    '-o', '--output',
    dest='output_file',
    type=str,
    help='name of file to create (json, csv, or nornaml)')
  # if the user wants to provide an API key as an argument
  parser.add_argument(
  	'-A', '--apikey',
  	dest='apikey',
  	type=str,
  	default=None,
  	help='VirusTotal API key to use for scan requests')
  
  # if user wants an interface to interact with
  parser.add_argument(
    '-i', '--interface',
    action='store_true',
    default=False,
    help='interface')

  # check if no args were passed
  # or if too many args were passed
  if len(argv) == 1 or len(argv) >= 5:
  	# show program banner
  	programName()
  	# print help menu
  	parser.print_help()
  	# exit program
  	exit(1)
  
  # get arguments from parser object
  args = parser.parse_args()
  
  return args
