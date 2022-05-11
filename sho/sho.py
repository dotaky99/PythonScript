from shodan import Shodan
########################
#country_name ports domains vulns data os server location, ip_str, ports
########################

api = Shodan('')
hosts = []

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