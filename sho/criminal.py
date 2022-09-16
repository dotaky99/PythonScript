import requests

# get API KEY
YOUR_API_KEY = ""
with open("API_KEY", "r") as f:
    YOUR_API_KEY = f.readline()

url = "https://api.criminalip.io/v1/user/me"

payload={}
headers = {
  "x-api-key": YOUR_API_KEY
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)