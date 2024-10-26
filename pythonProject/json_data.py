'''
Java script object notation

JSON            PYTHON
object          dict
array           list
string          str
number (int)    int
number (real)   float
true            True
false           False
null            None
'''

import json


people_string = '''
{
    "people" : [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

# json.loads - parse json string into python object
# json.dumps - parse python object string into json
# json.load - load the json file and parse into python object
# json.dump - create new json file from python object (json.dump(data, f, indent=2))

data = json.loads(people_string)

data = json.dumps(data, indent=2, sort_keys=True)
print(data)
