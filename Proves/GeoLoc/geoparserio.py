import requests, json
url = 'https://geoparser.io/api/geoparser'
headers = {'Authorization': 'apiKey INSERT-YOUR-API-KEY-HERE'}
data = {'inputText': 'I was born in Springfield and grew up in Boston.'}
response = requests.post(url, headers=headers, data=data)
print (response)
print (json.dumps(response.json(), indent=4))