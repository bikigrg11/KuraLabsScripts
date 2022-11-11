import requests
import json

 
url = "https://api.travelpayouts.com/v2/prices/month-matrix"
 
querystring = {"currency": "usd", "show_to_affiliates": "true",
               "origin": "LED", "destination": "HKT"}
 
headers = {'x-access-token': '2160a9f9ca2fa3d348f4a3a32504538e'}
 
response = requests.request("GET", url, headers=headers, params=querystring)
 
# print(response.text)

flightDetail = json.loads(response.text)

# print(type(flightDetail))

# print(flightDetail['data'][0]['value'])


lowerData = []
higherData = [] 

for flightdata in flightDetail['data']:
    if flightdata['value'] < 650 :
       lowerData.append(flightdata)
    else:
        higherData.append(flightdata)

def printFlightData(userData):
    for eachData in userData:
        print(f"Origin - {eachData['origin']}")
        print(f"Destination - {eachData['destination']}")
        print(f"Price - {eachData['value']}")
        print("\n")


userInput = (input("Please enter if you want to see flights below or higher 650 ?")).lower()

if userInput == "below":
    printFlightData(lowerData)
else:
    printFlightData(higherData)


