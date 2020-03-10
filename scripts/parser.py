#!/usr/bin/env python3

import argparse
import colored

###### add some color to this!
def ParseArgs():
  """
  parsing arguments passed in the command line
  """
  
  parser = ArgumentParser(
    description='Scan files for viruses',
    usage='usage: -f|--file [-m|--mass] [--csv]
                  [--json] [--norm] [-o|--output]'
  )
  
  required = parser.add_argument_group('required args')
  
  # the single file a user wants to scan
  required.add_argument(
    '-f', '--file',
    required=True,
    type=str,
    help='file to scan for virus')
  
  # if the user wants to scan more than one file
  parser.add_argument(
    '-m','--mass',
    type=str,
    help='file containing multiple files to scan (50 files max)\n
           Note: the timing for multiple scans will depend on the quality of your api key')
  
  # if the user wants wants the output format to be pure csv
  parser.add_argument(
    '--csv',
    action='store_true',
    help='output scan results to file in csv format')

  # if the user wants the output format to be pure json
  parser.add_argument(
    '--json',
    action='store_true',
    help='output scan results to file in json format')
  
  # if the user wants the output format to be normal text
  parser.add_argument(
    '--norm',
    action='store_true',
    help='output scan results to file with a normal format')
  
  # the output file name to create when user chooses
  # to output scan results to file (json, csv, or normal)
  parser.add_argument(
    '-o', '--output',
    dest='filename',
    type=str,
    help='name of file to create (json, csv, or nornaml)')
  
