import urllib2
import json
from pprint import pprint

# via Simon Willison: http://simonwillison.net/2008/Jun/21/jsontime/

# urlopen returns a file-like object containing the data
data = urllib2.urlopen('http://json-time.appspot.com/time.json')

json_data = json.load(data)
pprint(json_data)

print
print json_data['datetime']
