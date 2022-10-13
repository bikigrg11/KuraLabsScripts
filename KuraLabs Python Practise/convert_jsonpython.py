import json

# from JSON to Python dict

jsonObject = '{ "name":"Biki", "age":200, "city":"New York"}'

pythonObject = json.loads(jsonObject)

print(pythonObject["name"])


# from Python dict to JSON Object

pythonDict = {
    "name" : "Biki",
    "age" : "100",
    "city" : "New York"
}

JSONObject = json.dumps(pythonObject)

print(JSONObject)