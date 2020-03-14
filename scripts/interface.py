#!/usr/bin/env python3

try:
    import main
except ImportError:
    print('[-] Could not find the main module')



def interface():
    """
	Creates Vscan's interface

		:parameters:

			none

		:returns:

			none
	"""
    pass

    # # get api key
    # API_KEY = input('%sEnter a valid VirusTotal API key $: %s'
    #                 % (fg(196), attr(0)))
    # # name of file to write
    # out_file = input('Enter the name of the output file: ')
    #
    #
    #
    # """
    # prompt user for:
    #     - file format (csv, json, or norm)
    #     - api key
    #     - name of the output file is the user specified an output file format
    #     - ask user if they would like to email reports
    # """
    # scanit.sendFile(API_KEY, NAME_OF_FILE)
    #
    # filecontent = open(filename, 'rb').read()
    #
    # file_hash = main.genSha256(filecontent)
    #
    # result = scanit.getReport(file_hash)





