import os
import sys
import time
import socks
import requests
import pyfiglet
os.system("clear")
print ("                            DEEPNET | DARKNET")
banner=pyfiglet.figlet_format("OnionCOPY",font="standard")
print(banner)
print ("                                                    V1.0")
print ("   Coded By Rahat Khan Tusar(rkt)")
print ("   Follow in Github : https://github.com/r3k4t")
session=requests.session()
session.proxies={}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'
print
onionsite=raw_input("Enter a onion  site :")
response=session.get(onionsite)
date = time.strftime("%d/%m/%y")
if response.headers["CONNECTION"]:
   print(chr(27)+"[32m"+"[==[ACTIVE]==>"+chr(27)+"[37m"+response.url+chr(27)+"[32m"+"[==[DATE]==>"+chr(27)+"[37m"+date)
start = time.time()
end = time.time()
t_time = end - start
rkt_folder = os.path.dirname(os.path.abspath(__file__))
rkt_file = os.path.join(rkt_folder, 'index.html')
file = open("index.html", "w") 
file.write(response.content)
print("Total Runing Time : " ,t_time,"seconds") 
file.close() 
print(chr(27)+"[32m"+"Please, check index.html file.[Open a terminal and Type a command:firefox index.html]")
