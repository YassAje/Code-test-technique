import urllib.request
import urllib.parse
import simplejson

# http://google.../q=qqch
q = urllib.parse.urlencode({'q' : 'video2brain ubuntu'})

url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % (q)
#print(url)
search = urllib.request.urlopen(url)

json = simplejson.loads(search.read())

print(json['responseData']['results'])

