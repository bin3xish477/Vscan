#!/usr/bin/env python3

from argparse import ArgumentParser
import colored
from sys import argv, exit
from main import program_name

###### add some color to this!
def ParseArgs():
  """
  parsing arguments passed in the command line
  """
  
  parser = ArgumentParser(
    description='Scan files for viruses',
    usage='vscan (-f|--file) [-m|--mass] [--csv]\
                  \n\t     [--json] [--norm] [-o|--output]'
  )
  
  required = parser.add_argument_group('REQUIRED')
  parser._optionals.title = ('OPTIONAL')
  
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
  # check if no args were passed
  # or if too many args were passed
  if len(argv) == 1 or len(argv) >= 5:
  	program_name()
  	parser.print_help()
  	exit(1)
  
  args = parser.parse_args()
  
  return args
