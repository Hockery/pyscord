import os
import json 
import bs4 
import time, random, urllib
from log_init import logger
from get_page.get_methods import get_methods 
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
        for method in main_item["method_describe"]:
            data = get_methods(method)
            if data == '':
                print("get %s failed!"%(main_item['item_url']))
                continue
            print(data)


if __name__ == "__main__":
    scord_main()