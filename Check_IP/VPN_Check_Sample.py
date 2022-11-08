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

    def payment_transaction_fraud_prev(self, ip: str, vars: dict = {}) -> dict:
        """Method used to lookup Payment & Transaction Fraud Prevention API 

        Args:
            ip (str): _description_
            vars (dict, optional): Reffer to https://www.ipqualityscore.com/documentation/proxy-detection/transaction-scoring for variables.. Defaults to {}.

        Returns:
            dict: _description_
        """
        if not bool(vars):
            return {}

        url = "https://www.ipqualityscore.com/api/json/ip/%s/%s" %(self.key, ip)
        x = requests.get(url)
        return (json.loads(x.text))




class MyServer(BaseHTTPRequestHandler):
    """This is an example basic web server. we limited it to handle "/" path only."""

    def do_GET(self):
        if self.path == "/":
            ipqs = IPQS()
            
            header_items= dict(self.headers.items())
            parameters = {
                'user_agent'                    : header_items['User-Agent'],
                'user_language'                 : header_items['Accept-Language'].split(',')[0],
                'strictness'                    : 0,
                # You may want to allow public access points like coffee shops, schools, corporations, etc...
                'allow_public_access_points'    : 'true',
                # Reduce scoring penalties for mixed quality IP addresses shared by good and bad users.
                'lighter_penalties'             : 'false'
            }


         
            result = ipqs.payment_transaction_fraud_prev(self.client_address[0],parameters)

            if 'success' in result and result['success'] == True:
                """
                NOTICE: If you want to use one of the examples below, remove
                any lines containing /*, */ and *-, then remove * from any of the
                the remaining lines.
                """


                """
                Example 1: We'd like to block all proxies and send them to Google.
                """

                if result['proxy'] == True:
                    
                    self.send_response(303)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location','https://www.ipqualityscore.com/disable-your-proxy-vpn-connection')
                    self.end_headers()
                    return
                
                """
                Example 2: We'd like to block all proxies, but allow legitimate
                crawlers like Google on our site:
                
                if result['proxy'] == True and result['is_crawler'] == False:
                	self.send_response(303)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location','https://www.ipqualityscore.com/disable-your-proxy-vpn-connection')
                    self.end_headers()
                    return
                """
                
                """
                Example 3: We'd like to block only visitors with a fraud score,
                of 80 or over, but allow crawlers such as Google:
                
                if result['fraud_score'] >= 80 and result['is_crawler'] == False:
                	self.send_response(303)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location','https://www.ipqualityscore.com/disable-your-proxy-vpn-connection')
                    self.end_headers()
                    return
                """
                
                """
                Example 4: We'd like to block only visitors which are a proxy with a
                fraud score of 80 and over, but allow crawlers such as Google:

                if result['proxy'] == True and result['tor'] == True or result['fraud_score'] >= 80 or result['is_crawler'] == False:
                	self.send_response(303)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location','https://www.ipqualityscore.com/disable-your-proxy-vpn-connection')
                    self.end_headers()
                    return
                """

                """
                Example 5: We'd like to block only visitors which are using tor.
                
                if result['tor'] == True:
                	self.send_response(303)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location','https://www.ipqualityscore.com/disable-your-proxy-vpn-connection')
                    self.end_headers()
                    return
                """

                """
                If you are confused with these examples or simply have a use case
                not covered here, please feel free to contact IPQualityScore's support
                team. We'll craft a custom piece of code to meet your requirements.
                """

            self.send_response(500)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>The Example has failed to get a proper result.</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

