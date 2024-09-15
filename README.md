## Risk Gen API

Risk Gen API is an API that generates FAKE cybersecurity risk reports. <br />
The api live on https://risk-gen.onrender.com <br />
It uses the free tier, so if the server is not responding, try again in a minute or so because it spinned down due to inactivity. 


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

## Frontend, Report Preview

![image](https://github.com/user-attachments/assets/36760fe8-448f-4297-8198-37ec8a3961ca)
![image](https://github.com/user-attachments/assets/0379f7a8-58b9-4e6a-8bab-8ea7efc80749)





