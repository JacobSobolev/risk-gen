## Risk Gen API

Risk Gen API is an API that generates FAKE cybersecurity risk reports.


## Usage

```sh
https://risk-gen.onrender.com/report
```
```sh
https://risk-gen.onrender.com/report?records=50
```
records param needs to be between 1 and 100

## Example Report

```
[
  {
    "date": "Thu, 05 Sep 2024 13:21:57 GMT",
    "device_type": "Email Security Gateway",
    "ip": "199.182.31.219",
    "manufacturer": "Proofpoint",
    "risk_level": 3,
    "vulnerability": "Lack of Encryption at Rest",
    "vulnerability_desc": "Sensitive data stored on devices without encryption."
  },
]
```
