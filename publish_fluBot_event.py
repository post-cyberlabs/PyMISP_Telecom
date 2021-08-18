#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
from datetime import date

from pymisp import ExpandedPyMISP, MISPEvent
from pymisp import MISPObject
from keys import misp_url, misp_key, misp_verifycert

if len(sys.argv) < 2:
    print("No filename provided, please use python3 publish_FluBot_event.py url.csv")
    sys.exit()

misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)

event = MISPEvent()
event.info = 'FluBot - POST Luxembourg Detected URLs - All domains'  # Event Title
event.distribution = 1 # 0 = Your Organisation Only, 1 = Community
event.threat_level_id = 1 # 1 = High, 2 = Medium, 3 = Low
event.analysis = 2  # 0 (initial analysis), 1 (On-Going), 2 (Complete)

event.add_tag('tlp:green')
event.add_tag('Flubot')
event.add_tag('android')
event.add_tag('Smishing')
event.add_tag('android-malware')

d = date.today()
event.set_date(d)

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        misp_object = MISPObject('url', standalone=False)
        misp_object.comment = 'Flubot Domain detect via TIDS'
        misp_object.add_attribute('url', value=row[0])
        misp_object.add_attribute('domain', value=row[1])
        event.add_object(misp_object)

event = misp.add_event(event, pythonify=True)

# Publish event
event.publish()
