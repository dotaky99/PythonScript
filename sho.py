from shodan import Shodan
########################
#country_name ports domains vulns data os server location, ip_str, ports
########################

api = Shodan('KqOGSQKy2uVql8H2O3Ld76qsNs9vRJgd')
hosts = ['47.242.233.1', '116.89.240.43', '116.89.243.4', '147.135.51.41', '147.135.51.46', '15.204.22.184', '169.129.221.20', '169.129.221.67', '213.139.235.244', '47.74.53.52', '69.163.200.241']

for ipInfo in hosts:
    string = ''
    # IP가 쇼단 DB에 있는지 확인
    try:
        ipInfo = api.host(ipInfo)
        string = f'{ipInfo["ip_str"]}\t'
        try:
            string += f'{str(ipInfo["ports"])[1:-1]}\t'
        except:
            string += f'-\t'
            pass
        # # 국가 확인
        # try:
        #     string += f'{ipInfo["country_name"]}\t'
        # except:
        #     string += f'-\t'
        #     pass
        # IP 취약점 확인
        try:
            string += f'{str(ipInfo["vulns"])[1:-1]}'
        except:
            string += f'-\t'
            pass
    except:
        string = f'{ipInfo} is not result'
        continue
    # IP Port 확인
    print(string)