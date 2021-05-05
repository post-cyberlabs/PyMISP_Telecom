#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymisp import ExpandedPyMISP
from keys import misp_url, misp_key, misp_verifycert

# This script is a really simple example on how to extract FluBot URL published on event 820
# It will create a urls.txt file

f = open('urls.txt','w')

if __name__ == '__main__':

    misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)
    result = misp.search(eventid=820, return_format='json')

    for r in result:
        for o in r['Event']['Object']:
            for a in o['Attribute']:
                if a['object_relation'] == 'url':
                    if '//' in a['value']:
                        f.write(a['value'])
                        f.write('\n')
    f.close()
