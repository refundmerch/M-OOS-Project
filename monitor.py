# Importing libraries
import time
import hashlib
import os
from twilio.rest import Client
from urllib.request import urlopen, Request

account_sid = os.environ['ACcaa1f85bb4f20b690743cd8274512e0a']
auth_token = os.environ['38a5c6334d16a2f19aa1a4f77e0ab01f']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+19803855938',
         to='+15199810480'
     )

print(message.sid)

print ("What site would you like to monitor (please insert full product link)")
url_user = input()
url = Request(url_user,
			headers={'User-Agent': 'Mozilla/5.0'})

# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("Site is now being monitored")
time.sleep(1)
while True:
	try:
		# perform the get request and store it in a var
		response = urlopen(url).read()
		
		# create a hash
		currentHash = hashlib.sha224(response).hexdigest()
		
		# wait for 1 second
		time.sleep(1)
		
		# perform the get request
		response = urlopen(url).read()
		
		# create a new hash
		newHash = hashlib.sha224(response).hexdigest()

		# check if new hash is same as the previous hash
		if newHash == currentHash:
			continue

		# if something changed in the hashes
		else:
			# notify
			print("Product is now in stock!")

			# again read the website
			response = urlopen(url).read()

			# create a hash
			currentHash = hashlib.sha224(response).hexdigest()

			# wait for 1 second
			time.sleep(1)
			continue
			
	# To handle exceptions
	except Exception as e:
		print("error")
