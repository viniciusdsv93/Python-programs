# Program that manipulates json files

import json

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, \
"felineIQ": null}'

# convert json data to python values
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)

# convert python values to json data
stringOfJsonData = json.dumps(jsonDataAsPythonValue)
print(stringOfJsonData)
