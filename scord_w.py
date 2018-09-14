import os
import json 
import bs4 
import time, random, urllib
from log_init import logger
from get_page import get_methods 
from save_result import save_local

main_config = './scord_c.json'
indent = '  '
html_ext = ['shtml', 'htm', 'html']
dir_name= '.'

def scord_main():
    if not os.path.exists(main_config):
        logger.error("the main config file isn't exist or invalid!")
        return 0

    with open(main_config, 'r') as config_fb:
        main_json = json.loads(config_fb.read())
    # print(main_json)
    for main_item in main_json:
        if "get_time" in main_item.keys():
            get_time = main_item["get_time"]
            if isinstance(get_time[0], int) and isinstance(get_time[1], int):
                data = get_methods.get_html_normal(main_item['item_url'], get_time)
                if data == '':
                    print("get %s failed!"%(main_item['item_url']))
                    continue
                print(data)
        # get_methods.get_html_normal(main_item['item_url'],)


if __name__ == "__main__":
    scord_main()