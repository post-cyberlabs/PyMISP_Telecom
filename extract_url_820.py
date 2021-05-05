#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymisp import ExpandedPyMISP
from keys import misp_url, misp_key, misp_verifycert
from phone_iso3166.country import *

# This script is a really simple example on how to extract call spam numbers in Telecom MISP events
# I then create a file with the phone numbers

f.write('number,country_iso2\n')

if __name__ == '__main__':

    misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)
    result = misp.search(eventid=820, return_format='json')

    f = open('urls.txt','w')

    for r in result:
        for o in r['Event']['Object']:
            for a in o['Attribute']:
                if a['object_relation'] == 'url':
                    f.write(a['value'])
                    f.write('\n')
    f.close()
