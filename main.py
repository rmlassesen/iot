'''
    File name: main.py
    Author: Rune Møller-Lassesen
    Date created: 12/12/2018
    Date last modified: 12/12/2018
    Python Version: 3.7
'''

# LOCATION-HUB
# Server and communication module for IoT project: IKEA Pricetagging
# Runs storage server, processes RF input, and sends Pricetag-update information to PRICETAG-HUB

# Usage, using prefered CLI
# Storage server: main.py storage
# RF-processing: main.py RF

import sys
from lib.server import spin_up
from lib.rf_handler import listen

if __name__ == '__main__':
    if sys.argv[1] == 'storage':
        spin_up()

    elif sys.argv[1] == 'RF':
        listen()

    else:
        print("Usage:")
        print("Storage server: main.py storage")
        print("RF-processing: main.py RF")

else:
    print("WARNING: This program should be used as CLI, and is not eligible for import as a module")