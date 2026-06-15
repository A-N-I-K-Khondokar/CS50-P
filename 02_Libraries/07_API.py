import requests #To make https requests
import sys # for commandline argument
import json # comes with python

if len(sys.argv)!=2:
    sys.exit()

response=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1]) #'weezer' as argument
#print(json.dumps(response.json(),indent=2))

o =response.json() # o is a object
for results in o["results"]: # results is a list in that object
    print(results["trackName"]) # trackName is one of the keys

'''
1. What is API? How can we use it?
2. requests library allows to web requests.
3. Documentation : https://pypi.org/project/requests/
4. JSON
5. https://itunes.apple.com/search?entity=song&limit=1&term=weezer 
if i type this on browser it will download a file in JSON formet which is some 
information form the apple itunes API
6. Now, if i want to access this data with python i need to write program
which can access the server's data in this case my python program will patents to be 
a browser.
7.we need to know API formet to manipulate or get something form the apple API
8.You NEED Internet connection!!!!!!



'''

"""
New one
"""