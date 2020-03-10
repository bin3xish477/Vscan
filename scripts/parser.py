#!/usr/bin/env python3

import argparse
import colored

def ParseArgs(self):
  """
  parsing arguments passed in the command line
  """
  
  parser = ArgumentParser(
    description='Scan files for viruses',
    usage='usage: -f|--file [-m|--mass] [--csv]
                  [--json] [--norm]'
  )
  
  required = parser.add_argument_group('required args')
  
  required.add_argument(
    '-f', '--file',
    required=True,
    type=str,
    help='file to scan for virus')
    
  parser.add_argument(
  '-m','--mass',
  type=str,
  help='file containing multiple files to scan (100 files max)')
  
  parser.add_argument(
  '--csv',
  type=str,
  help='output scan results to file in csv format')
  
  parser.add_argument(
  '--json',
  type=str,
  help='output scan results to file in json format')
  
  parser.add_argument(
  '--norm',
  type=str,
  help='output scan results to file with a normal format')
