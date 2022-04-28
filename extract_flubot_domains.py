#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymisp import ExpandedPyMISP
from keys import misp_url, misp_key, misp_verifycert
from urllib.parse import urlparse
import time

# This script is a really simple example on how to extract FluBot domains published on all events with tag "Flubot"
# It will create a flubot-domains.txt

timestr = time.strftime("%Y%m%d-%H%M")

if __name__ == '__main__':

    print("-- Search MISP Events, may take few minutes please be patient --")
    misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)
    # Search for all events with "Flubot" tag
    result = misp.search(tags=['Flubot'], return_format='json')

    # Set to keep uniqueness of domains 
    domains = []

    print("-- Parsing MISP Events --")
    for r in result:
        # if the data is stored into a MISP object
        if r['Event']['Object']:
            for o in r['Event']['Object']:
                for a in o['Attribute']:
                    if a['object_relation'] == 'domain':
                        # Parsing domains to make sure we avoid text etc
                        domain = urlparse(a['value']).netloc
                        domains.append(domain)

        elif r['Event']['Attribute']:
            for e in r['Event']['Attribute']:
                # Parsing domains to make sure we avoid text etc
                domain = urlparse(e['value']).netloc
                domains.append(domain)
    
    filename = timestr+"-flubot-domains.txt"
    print("-- Writing Results to file "+filename+" --")

    # Write all domains into a file
    with open(filename, "w") as outfile:
        outfile.write("\n".join(str(d) for d in list(domains)))
    outfile.close()
