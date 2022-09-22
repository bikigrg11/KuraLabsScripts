try:
    import simplejson as json
except ImportError:
    import json


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y = json.dumps(x)
z = json.loads(y)

print(z["age"])
print(y)

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")