import md5
import urllib2
import hashlib
import time
import json


url = 'http://gateway.marvel.com:80/v1/public/characters?limit=10&offset=300&apikey=' 

public_key = 'c4de224ed518964c1094d1adc20a6e47'
private_key = 'e4082b603d959644261bc98de096a7373f6f0896'
#ts = '1234'
#Server-side applications must pass two parameters in addition to the apikey parameter:

#ts - a timestamp (or other long string which can change on a request-by-request basis)
#hash - a md5 digest of the ts parameter, your private key and your public key (e.g. md5(ts+privateKey+publicKey)
#For example, a user with a public key of "1234" and a private key of "abcd" could construct a valid call as follows: 
# http://gateway.marvel.com/v1/comics?ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150 
#(the hash value is the md5 digest of 1abcd1234)

def getMarvels():

	ts = long(time.time()*100)

	hash_string = hashlib.md5(str(ts)+private_key+public_key).hexdigest()

	url_string = url+public_key+'&hash='+hash_string+'&ts='+str(ts)

	print url_string
	data =  json.loads(urllib2.urlopen(url_string).read())['data']

	#for marvel in data['results']:
	#	print marvel['name']
	#	print marvel['description']
	#	print marvel['comics']['available']
	return data['results']


