import urllib.request
import urllib.parse
import simplejson
import re

p = re.compile('.*youtube\.com.*', re.IGNORECASE)
e = re.compile('<b>|</b>')

# http://google.../q=qqch
q = urllib.parse.urlencode({'q' : 'video2brain ubuntu'})

url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % (q)
#print(url)
search = urllib.request.urlopen(url)

json = simplejson.loads(search.read())

for r in json['responseData']['results']:
    if p.match(r['url']):
        print(e.sub('', r['title']), r['url'])

