from bs4 import BeautifulSoup
import urllib
import requests
import socket
import time
import random


def use_Agent():
    agents=[
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
        ]
    header={}
    header['User-agent']=random.choice(agents)
    return header

def getProxyIp():
    proxy=[]
    for i in range(1,2):
        try:
            url = 'http://www.xicidaili.com/nn/' + str(i)
            # url = 'http://www.xicidaili.com/nn/66'
            use=use_Agent()
            req = requests.get(url, headers=use)
            soup = BeautifulSoup(req.text, 'html.parser')
            # <tr class="odd">
            #     <td class="country"></td>
            #     <td>IP</td>
            #     <td>PORT</td>
            #     ...
            # </tr>
            ips = soup.findAll('tr')
            for x in range(1, len(ips)):
                ip = ips[x]
                tds = ip.findAll("td")
                # ip+端口
                ip_temp = tds[1].contents[0] + ":" + tds[2].contents[0]
                proxy.append(ip_temp)
        except:
            continue
    return proxy


def validateIp(proxy):
    url = "http://ip.chinaz.com/getip.aspx"
    f = open("ip.txt", "w+")
    # 因为urlopen之后的read()操作其实是调用了socket层的某些函数。所以设置socket缺省超时时间，就可以让网络自己断掉。不必在read()处一直等待。
    # socket.setdefaulttimeout(3)
    requests.Session()
    for i in range(0, len(proxy)):
        try:
            proxy_host = proxy[i]
            proxy_temp = {"http": proxy_host}
            # res = urllib.urlopen(url, proxies = proxy_temp).read()
            wb_data = requests.get(url, headers=use_Agent(), proxies=proxy_temp)
            soup = BeautifulSoup(wb_data.text, 'lxml')
            f.write(proxy_host + '\n')
            print(proxy_host+"**********")
        except:
            continue
    f.close()


if __name__=="__main__":
    proxy=getProxyIp()
    validateIp(proxy)
