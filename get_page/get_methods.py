import urllib,bs4
import random, time
from log_init import logger

def get_methods(method, url=''):
    if url == '' and "item_url" in method.keys():
        url = method['item_url']
    else:
        return
        
    if method["get_method"] == "normal":
        if "get_time" in method.keys():
            get_time = method["get_time"]
            if isinstance(get_time[0], int) and isinstance(get_time[1], int):
                return get_html_normal(url, get_time)

def get_html_normal(url, random_time):
    html = ''
    i = 2
    while(i):
        try:
            sleep_random = random.randint(random_time[0],random_time[1])/1000
            # print("sleep "+str(sleep_random)+" s")
            time.sleep(sleep_random)
            response = urllib.request.urlopen(url,timeout=3) 
            html = response.read().decode('utf-8')
            return html
        except Exception as e:
            i = i -1
            logger.debug('['+str(e)+']'+url)
    print ('URLError: <urlopen error timed out> All times is failed ' )   
    return '' 