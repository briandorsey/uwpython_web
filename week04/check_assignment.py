import sys
import urllib
import urllib2
import json
import random

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    print "USAGE:\nverify_assignment.py URL"
    print "You may need double quotes around the URL"
    print "Do NOT include a ? or anything after it."
    sys.exit(1)

a = random.randrange(1, 200)
b = random.randrange(1, 200)
expected_result = a + b
url = url + "?a=%s&b=%s" % (a,b)

print "=" * 70
print "Checking the URL: %s" % url
print "Passing numbers: %s and %s" % (a, b)

try:
    response = urllib2.urlopen(url)
    raw_data = response.read()
except StandardError, e:
    print "Couldn't fetch the URL"
    raise

try:
    data = json.loads(raw_data)
except StandardError, e:
    print "Couldn't parse the result:\n%s" % raw_data
    raise

try:
    print "Check: uwnetid"
    assert 'uwnetid' in data
    #assert type(unicode(data['uwnetid'])) == type(unicode())

    print "Check: time"
    assert 'time' in data
    int(data['time'])

    print "Check: result"
    assert 'result' in data
    print "Check: result (type)"
    result = data['result']
    assert int(result) == result
    print "Check: result (value)"
    assert result == expected_result


except StandardError, e:
    print "The object doesn't match the requirements:" 
    print json.dumps(data, indent=4)
    raise

print "=" * 70
print "Looks good!  Turn it in!"

