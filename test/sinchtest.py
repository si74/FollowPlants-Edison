"""import time
from sinchsms import SinchSMS

number = '+12482523866'
message = 'Hello from Sinch!'

client = SinchSMS("f7de985f-d24c-4911-be17-4dd116198f1a", "ltx3SEX+uky/SMwmjj89Lw==")

print("Sending '%s' to %s" % (message, number))
response = client.send_message(number, message)
message_id = response['MessageId']

response = client.check_status(message_id)
while response['Status'] != 'Successful':
    print(response['Status'])
    time.sleep(1)
    response = client.check_status(message_id)
print(response['Status'])"""

import time
import urllib2, base64

app_key = "f7de985f-d24c-4911-be17-4dd116198f1a"
app_secret = "ltx3SEX+uky/SMwmjj89Lw=="

request =urllib2.Request("http://messagingapi.sinch.com/v1/sms/+12482523866")
base64string = base64.b64encode(('application:%s:%s' % (app_key,app_secret)).encode())

auth = 'basic %s'

