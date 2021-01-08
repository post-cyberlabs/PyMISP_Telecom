#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymisp import ExpandedPyMISP
from keys import misp_url, misp_key, misp_verifycert

# This script is a really simple example on how to extract GTs from SS7 Objects in Telecom MISP events
# I then create a csv file with the following template:
# Source GT, Event URL

f = open('misp.csv','w')
f.write('id,url\n')

if __name__ == '__main__':

    misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)
    result = misp.search(tags=['SS7 Attack', 'SS7-Attack'], return_format='json')

    if not result:
        print('No results for this query')
        exit(0)

    for r in result:
        for o in r['Event']['Object']:
            for a in o['Attribute']:
                if a['object_relation'] == 'SccpCgGT':
                    # Handle when several GT with ',' or ';' have been inserted in the SccpCgGT attribute
                    if ',' in a['value']:
                        l_value = a['value'].split(",")
                        for v in l_value:
                            f.write(v.strip()+",https://misp.gsma.com/events/view/"+r['Event']['id']+"\n")
                    elif ';' in a['value']:
                        l_value = a['value'].split(";")
                        for v in l_value:
                            f.write(v.strip()+",https://misp.gsma.com/events/view/"+r['Event']['id']+"\n")
                    else:
                        f.write(a['value'].strip()+",https://misp.gsma.com/events/view/"+r['Event']['id']+"\n")

