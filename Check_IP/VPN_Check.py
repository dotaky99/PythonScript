# THIS SHOULD NEVER BE USED IN PRODUCTION AS IS!

# You may need to install Requests pip
# python -m pip install requests

import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests

hostName = "localhost"
serverPort = 8080

class IPQS:
    key = ""
    with open("API_KEY", "r") as f:
        key = f.readline().strip()

    def check_vpn(self):
        ip_list = []
        with open("ip_list", "r") as f:
            for line in f:
                ip_list.append(line.strip())

        url = "https://www.ipqualityscore.com/api/json/ip/%s/%s" %(self.key, ip_list)
        x = requests.get(url, params = vars)
        return (json.loads(x.text))


if __name__ == "__main__":
    imple = IPQS()
    imple.check_vpn()