import urllib
import urllib2

temp = 5 

url = 'http://104.236.33.166:8081/api/plantTemp.php'
values = {'temp':temp}
data = urllib.urlencode(values)
req = urllib2.Request(url,data)
response = urllib2.urlopen(req)
the_page = response.read()

print the_page