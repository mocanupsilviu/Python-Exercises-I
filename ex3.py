"""
 Exercise 3:
 From the below string extract, IP DATE PICS URL , and print it
 Input String
 '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248
 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)'
"""
import re

def find(s):
    #print(string)
    if not isinstance(s, str):
        print("Not a valid string!")
        return
    ip_find = re.search(r'\d+\.\d+\.\d+\.\d+', s)
    date_find = re.search(r'\[(.*?)]', s)
    pics_url_find = re.search(r'GET (/pics/\S+)', s)
    url_find = re.search(r'"(https?://[^"]+)"', s)
    if ip_find:
        print("IP:", ip_find[0])
    if date_find:
        print("DATE:", date_find[0])
    if pics_url_find:
        print("PICS URL:", pics_url_find[0])
    if url_find:
        print("URL:", url_find[0])

string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
find(string)
find(None)