import requests

#endpoint= "https://bitbucket.org"
endpoint="http://127.0.0.1:8000/api/"

get_response=requests.post(endpoint,json={"title":"tt"}) #API end point
print(get_response.json())
#print(get_response.headers)
#print(get_response.text)#printing raw text response
#print(get_response.json())

#time complexiting
