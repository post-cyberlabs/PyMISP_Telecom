#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymisp import ExpandedPyMISP, MISPEvent
from pymisp import MISPObject
from keys import misp_url, misp_key, misp_verifycert
from datetime import date

misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)

event = MISPEvent()
event.info = 'IoT malware'  # Event Title
event.distribution = 1 # 0 = Your Organisation Only, 1 = Community
event.threat_level_id = 2 # 1 = High, 2 = Medium, 3 = Low
event.analysis = 2  # 0 (initial analysis), 1 (On-Going), 2 (Complete)

event.add_tag('malware_classification:malware-category="Botnet"')
event.add_tag('tlp:amber')

d = date.today()
event.set_date(d)

attribute_second = event.add_attribute('url', 'http://1.2.3.4/example', disable_correlation=False, comment="Botnet example text", to_ids=False)

event = misp.add_event(event, pythonify=True)

# Publish event
event.publish()
