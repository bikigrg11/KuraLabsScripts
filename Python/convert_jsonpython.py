import json

# from JSON to Python dict

# jsonObject = '{ "name":"Biki", "age":200, "city":"New York"}'

# pythonObject = json.loads(jsonObject)

# print(pythonObject["name"])


# # from Python dict to JSON Object

# pythonDict = {
#     "name" : "Biki",
#     "age" : "100",
#     "city" : "New York"
# }

# JSONObject = json.dumps(pythonObject)

# print(JSONObject)

example = {
    "Teams":[
        {"Giants":[{"wins":4}, {"losses":1}]},
        {"Jets":[{"wins":3}, {"losses":2}]}
    ]
}

print(example["Teams"][1])
print(example["Teams"][0]["Giants"][0]["wins"])


'''
    share screen:
    http and get
    page check return json - exmaple of the json you might get from the url 

    required:

    make a Class JsonParser
    take an input when the object is created. 

    # make function that will output the number of healthy checks and unhealthy checks 
    # make a function that will output the list which names are healthy and which names are unhealthy
'''
