"""
{
  "Status": "Healthy",
  "Checks": [
    {
      "Name": "Connections",
      "Status": "Healthy"
    },
    {
      "Name": "ConnectionRead",
      "Status": "unHealthy"
    },
    {
      "Name": "redis",
      "Status": "Healthy"
    },
    {
      "Name": "ProcessCheck",
      "Status": "Healthy"
    },
    {
      "Name": "UserProfile",
      "Status": "unHealthy"
    },
    {
      "Name": "features",
      "Status": "unHealthy",
      "Description": "sample sample sample"
    },
    {
      "Name": "shutdown",
      "Status": "Healthy"
    },
    {
      "Name": "lifespan",
      "Status": "unHealthy"
    }
  ]
}
"""

# make a json parser class
# above example is the input for when the object is created
# make function that will output the number of healthy and unhealthy
# make a function that will create and output the list of unhealthy and healthy check names

# Key, Value  = checks["Name"], Healthy

import json

class WebChecker:

    healthyDict = dict()
    unhealthyDict = dict()

    def __init__(self,jsonString):
        self.jsonDict = json.loads(jsonString)

        for checks in self.jsonDict["Checks"]:
            if checks["Status"] == "Healthy":
                WebChecker.healthyDict[checks["Name"]]= "Healthy"
            else:
                WebChecker.unhealthyDict[checks["Name"]]="unHealthy"

    # this Method will return the Healthy Number
    def get_healthy_number(self):
        return len(WebChecker.healthyDict)

    # this Method will return the unHealthy Number
    def get_unhealthy_number(self):
        return len(WebChecker.unhealthyDict)
    
    # this Method will return the healthy Names
    def get_healthy_names(self):
        healthyList= []
        for names in WebChecker.healthyDict:     
           healthyList.append(names)
        return healthyList

    # this Method will return the unHealthy Names
    def get_unhealthy_names(self):
        unhealthyList= []
        for names in WebChecker.unhealthyDict:
            unhealthyList.append(names)
        return unhealthyList
        
        
checkJson = """{
  "Status": "Healthy",
  "Checks": [
    {
      "Name": "Connections",
      "Status": "Healthy"
    },
    {
      "Name": "ConnectionRead",
      "Status": "unHealthy"
    },
    {
      "Name": "redis",
      "Status": "Healthy"
    },
    {
      "Name": "ProcessCheck",
      "Status": "Healthy"
    },
    {
      "Name": "UserProfile",
      "Status": "unHealthy"
    },
    {
      "Name": "features",
      "Status": "unHealthy",
      "Description": "sample sample sample"
    },
    {
      "Name": "shutdown",
      "Status": "Healthy"
    },
    {
      "Name": "lifespan",
      "Status": "unHealthy"
    }
  ]
}"""

checker1 = WebChecker(checkJson)
print(checker1.healthyDict)


print("Healthy Names HERE :")
for eachHealthy in checker1.get_healthy_names():
    print(eachHealthy)

healthyNumber = checker1.get_healthy_number()
print(f"No of Healthy Checks is: {healthyNumber}")

print("\n")

print("unHealthy Names HERE :")
for eachUnhealhy in checker1.get_unhealthy_names():
    print(eachUnhealhy)

unHealthyNumber = checker1.get_unhealthy_number()
print(f"No of unHealthy Checks is: {unHealthyNumber}")
