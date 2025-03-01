import requests

url = "https://www.virustotal.com/api/v3/urls"

payload = { "url": f'{check_url}' }
headers = {
    "accept": "application/json",
    "x-apikey": f'{API}' ,
    "content-type": "application/x-www-form-urlencoded"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)