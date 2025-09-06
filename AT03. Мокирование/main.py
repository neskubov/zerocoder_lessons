import requests

def fetch_random_cat_image(api_url='https://api.thecatapi.com/v1/images/search'):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
