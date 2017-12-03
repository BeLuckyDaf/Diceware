import requests
import json
import os

request_id = 78342  # some number


def generate(api):
	# getting a dictionary from a local directory
	dictionary = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dictionary.asc")
	
	# a request to send
	payload = {"jsonrpc": "2.0", "method": "generateIntegers",
				"params": {"apiKey": api, "n": "30", "min": "1", "max": "6"}, "id": request_id}
    
	# random.org url for json-rpc requests
	url = "https://api.random.org/json-rpc/1/invoke"
	
	# specifying a header
	headers = {'content-type': 'application/json-rpc'}
	
	# receiving the response from random.org (numbers from 1 to 6)
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	
	# parsing the data
	random = json.loads(response.text)['result']['random']['data']

	# temporary variables
	temp = ""
	pairs = []
	password = ""

    
	# splitting numbers into pairs
	for i in range(0, len(random)):
		temp += str(random[i])
		if i % 5 == 4:
			pairs.append(temp)
			temp = ""
			
	# making words using the dictionary and the pairs above
	for combination in pairs:
		with open(dictionary, 'r') as sfile:
			for line in sfile:
				if combination in line:
					password += (line[6:-1]) + " "

					
	# returns a string of format "word word word word word word"
	return password[:-1]
