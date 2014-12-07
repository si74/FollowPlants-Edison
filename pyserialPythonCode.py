from time import sleep
import serial
import urllib
import urllib2

"""if not os.path.exists("data.json"):
	with open("data.json", mode='r', encoding='utf-8') as f:
		json.dump([],f)"""

ser = serial.Serial("/dev/cu.usbmodem1413", 9600) # Establish the connection on a specific port
counter = 32 # Below 32 everything in ASCII is gibberish

#data = {}; 

while True:
     counter +=1
     ser.write(str(chr(counter))) # Convert the decimal number to ASCII then send it to the Arduino

     temp = ser.readline()

     print temp # Read the newest output from the Arduino

     sleep(.1) # Delay for one tenth of a second

     #send every one temperature reading
     if counter % 100 == 0:

     	url = 'http://'
     	values = {'temp':temp}
     	data = urllib.urlencode(values)
     	req = urllib2.Request(url,data)
     	response = urllib2.urlopen(req)
     	the_page = response.read()

     	print 'yay'
     	#Send http request
     	 

     #Reset if end
     if counter == 255:
        counter = 32

