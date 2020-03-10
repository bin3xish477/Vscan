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
  import scan-it
except ImportError:
  raise ImportError('Error importing module')

def main():
    



if __name__ == '__main__':
  try:
    main()
   except KeyboardInterrupt:
    try:
      print('The program has been interrupted.')
      sys.exit(0)
    except SystemError:
      os._exit(0)
      
