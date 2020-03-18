#!/usr/bin/env python3

try:
  from argparse import ArgumentParser
  from colored import fg, attr, bg
  from sys import argv, exit
  from main import programName
except ImportError as err:\
    print(f'Import Error: {err}')



def parseArgs():
  """
	Parse arguments passed in the command line

		:parameters:
			None

		:returns:
			arguments passed to command line
	"""
  parser = ArgumentParser(
    description=('%s%s* SCAN FILES FOR VIRUSES WITH VSCAN *%s'%(fg(255),bg(1),attr(0))),
    usage=('vscan %s(-f|--file) [-m|--mass] [--csv]\
                  \n\t     [--json] [--norm] [-o|--output]%s')%(fg(39),attr(0)))

  parser._optionals.title = ('%s%s Options %s'%(fg(255),bg(2),attr(0)))

  # the single file a user wants to scan
  parser.add_argument(
    '-f', '--file',
    dest='single_file',
    type=str,
    help='file to scan for virus')

  # if the user wants to scan more than one file
  parser.add_argument(
    '-m','--mass',
    type=str,
    dest='mass_file',
    help='file containing list of files to scan (50 files max)\
           \nNote: 50 files will take about 12 to 15 minutes to scan')

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
  	dest='api_key',
  	type=str,
  	default=None,
  	help='VirusTotal API key to use for scan requests')

  # if user wants an interface to interact with
  parser.add_argument(
    '-i', '--interface',
    action='store_true',
    default=False,
    help='interface')

  # if user wants to send report files to an email account
  parser.add_argument(
    '-e', '--email',
    action='store_true',
    default=False,
    help='send an email containing files of your choice'
  )

  # check if no args were passed
  # or if too many args were passed
  if len(argv) == 1 or len(argv) > 5:
  	# show program banner
  	programName()
  	# print help menu
  	parser.print_help()
  	# exit program
  	exit(1)

  # get arguments from parser object
  args = parser.parse_args()

  return args
