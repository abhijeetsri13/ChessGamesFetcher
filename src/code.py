

import json 
import os 
import requests 
# Opening JSON file 
f = open('config.json',) 

# returns JSON object as 
# a dictionary 
data = json.load(f) 

# Iterating through the json 
# list 
for i in data['AllUsers']: 
	user=i['user']
	stYr=i['StartYear']
	endYr=i['EndYear']
	
	path = os.path.join(os.getcwd(), user)

	isDir = os.path.exists(path)	
	
	if isDir == False:
		os.mkdir(user)
	for i in range(stYr, endYr):
		for j in range(1, 12):
			url =  'https://api.chess.com/pub/player/'+user+'/'+'games'+'/'+str(i)+'/'+str(j).zfill(2)+'/pgn'
			r = requests.get(url)
			data = str(r.text)
			
			if not data:
				continue
			filename = path + '\\' + str(i) +str(j).zfill(2)+'.pgn'
			fileobj = open(filename, 'w') 
			fileobj.write(r.text)
			fileobj.close()
			
	
f.close() 
