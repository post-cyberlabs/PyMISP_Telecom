# PyMISP Telecom

The goal of this repository is to document how to use the PyMISP lib with simple examples to interact with Telecom Data / Objects via PyMISP.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Install PyMISP: 
```
pip3 install pymisp
```
For any issue on installation please refer to the PyMISP readme for lib install tutorial.

* Fill up the file ```keys.py``` with your the MISP url and your own MISP API Key

## Usage example

### Flubot Data Collection
To extract all domains from Flubot data, you can use the following command line:
```
python3 extract_flubot_domains.py
```
As an output, a new file will be generated with the following format:
```
YearMonthDay-HourMinute-flubot-domains.txt
```

## Repository content listing

This repository contains:
* extract_SS7_GT.py : Extract all the offensive GTs from SS7 objects published, write the result into a CSV file
* publish_SS7_event.py : Publish a SS7 event with an SS7-attack object
* publish_iot_event.py : Publish a IoT Malware event with simple attributes
* extract_call_spam.py : Extract fraudulent numbers reported into MISP

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Or contact us via an issue or the T-ISAC initiative.

## Acknowledgements
* MISP Community - This project uses [PyMISP](https://github.com/MISP/PyMISP) and [MISP](https://github.com/MISP/MISP). 
* GSMA T-ISAC community - These efforts are made to support the GSMA T-ISAC initiative [GSMA T-ISAC Official Page](https://www.gsma.com/security/t-isac/)
* POST Luxembourg
* CO Finance by EU - Part of the [PISAX](https://www.pisax.org/) project
