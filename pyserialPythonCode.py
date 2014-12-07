from time import sleep
import serial
import urllib
import urllib2

"""if not os.path.exists("data.json"):
	with open("data.json", mode='r', encoding='utf-8') as f:
		json.dump([],f)"""

ser = serial.Serial("/dev/cu.usbmodem1413", 9600) # Establish the connection on a specific port
counter = 32 # Below 32 everything in ASCII is gibberish

data = []

def sendData(data):
	url = 'http://104.236.33.166:8081/api/plantTemp.php'
	values = {'temp':temp}
	data = urllib.urlencode(values)
	req = urllib2.Request(url,data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	print the_page

while True:
	counter +=1
	ser.write(str(chr(counter))) # Convert the decimal number to ASCII then send it to the Arduino

	temp = ser.readline()
	
	data.append(temp)

	print temp # Read the newest output from the Arduino

	sleep(.1) # Delay for one tenth of a second

	if counter % 10 == 0:

		sendData(data)

		data = []

     #Reset if end
	if counter == 255:
		counter = 32
