import json
from pprint import pprint

object = {
    'true' : True,
    'false' : False,
    'null' : None,
    'number' : 123,
    'number_' : 123.321,
    'string' : 'abc',
    'array' : [],
    'object' : {},
}

pprint(object)
print json.dumps(object, indent=1)
        
