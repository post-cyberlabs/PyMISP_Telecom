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

### Flubot Data Extract
To extract all domains from Flubot data, you can use the following command line:
```
python3 extract_flubot_domains.py
```
As an output, a new file will be generated with the following format:
```
YearMonthDay-HourMinute-flubot-domains.txt
```

### Flubot Data Import
To extract all domains from Flubot data, you can use the following command line:
```
python3 publish_fluBot_event.py urls-22062021.csv
```
urls-22062021.csv being a CSV formated file which contains information as such:
```
url,domain
http://mail.cngtermconsult.ga/click/,mail.cngtermconsult.ga
http://tochkacompany.ru/path/,tochkacompany.ru
http://ca1.ir/url/,ca1.ir
http://entreprisesmgm.com/click/,entreprisesmgm.com
....
```

As an output, a new event with a url object will be created on your MISP platform:
![image](https://user-images.githubusercontent.com/1607556/129906692-fb00a56e-7d50-4860-8fb3-60ff2d85309f.png)

## Repository content listing

This repository contains:
* extract_flubot_domains.py : Extract all the FLubot domains from URLs and exports them into a txt file
* extract_SS7_GT.py : Extract all the offensive GTs from SS7 objects published, write the result into a CSV file
* publish_fluBot_event.py : Publish a Flubot event importing a list of domains from a CSV file
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
