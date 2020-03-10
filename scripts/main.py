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
  import haslib
except ImportError:
  raise ImportError('Error importing module')

def gen_hash(file_content):
  
  
def main():
    



if __name__ == '__main__':
  try:
    main()
   # handle keyboard interrupt (ctrl+?)
   except KeyboardInterrupt:
    try:
      print('The program has been interrupted.')
      sys.exit(0)
    # handle sys.exit error
    except SystemExit:
      os._exit(0)
      
