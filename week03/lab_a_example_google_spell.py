import sys
import urllib2
import re
from BeautifulSoup import BeautifulSoup


search_url = 'http://www.google.com/search?q='
word = 'mispelled'
if len(sys.argv) > 1:
    word = sys.argv[1]

# so we can pretend to be IE 6
headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)'}

req = urllib2.Request(search_url + word, headers=headers)
response = urllib2.urlopen(req)
html = response.read()

#print html
soup = BeautifulSoup(html)

def spelling_text(text):
    text = text.lower()
    if ('did you mean' in text or
            'showing results for' in text):
        return True

did_you_mean = soup.find(text=spelling_text)
if did_you_mean:
    div = did_you_mean.parent.parent
    #print div
    print div.i.text
else:
    print 'not found'

