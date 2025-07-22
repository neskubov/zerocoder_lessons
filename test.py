import requests
api_url = 'https://api.api-ninjas.com/v1/quotes'
response = requests.get(api_url, headers={'X-Api-Key': 'D1pgeVNb9qXXiDoL/Ozr0Q==2eS39Q4IvdqIQxWv'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
