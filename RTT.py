import time
import requests

def RTT(url):
    t1=time.time()

    r=requests.get(url)

    t2=time.time()

    ti=str(t2-t1)
    print("the time in seconsd:"+ti)

url="http://www.google.com/"
RTT(url)