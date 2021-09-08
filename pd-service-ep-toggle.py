#!/usr/local/bin/python

import requests
import json

apiKey      = 'YOURAPIKEYGOESHERE' # api key MUST have write access
serviceId   = 'PR8MOOH'
weekdayEpId = 'P5IB0SR'
weekendEpId = 'PDJMLYV'

url = "https://api.pagerduty.com/services/" + serviceId

headers = {
'Authorization': 'Token token=' + apiKey,
'Accept': 'application/vnd.pagerduty+json;version=2',
'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers)

serviceDetails = response.json()['service']
currentEp = serviceDetails['escalation_policy']['id']
if currentEp == weekdayEpId:
    newEp = weekendEpId
else:
    newEp = weekdayEpId

print("\n")
print("Service Name: " + serviceDetails['name'] + " (" + serviceId + ")")
print("----------------------------------------------")
print("🔴 Previous EP: " + currentEp)

payload = json.dumps({
        "service": {
        "type": "service",
        "escalation_policy": {
            "id": newEp,
            "type": "escalation_policy_reference"
        }
    }
})

requests.request("PUT", url, headers=headers, data=payload)

print("🟢 Updated EP: " + newEp)
print("\n")