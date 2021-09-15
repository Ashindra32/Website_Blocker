import time
from datetime import datetime as dt
hosts_temp="hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours...")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+ "\n")
    else:
        with open(host_temp, 'r+')as file:
            content=file.readlines()
            for line in content:
                file.seek(0)
                if not any(website in line for website in website_list):
                    file.writeline()
            file.truncate()
        print("fun hours...")
    time.sleep(5)