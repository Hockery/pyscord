import os
import json 
import bs4 
import time, random, urllib
from log_init import logger
from get_page.get_methods import get_methods 
from save_result import save_local
from page_analyze import analyze_methods

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
                print("get %s failed!"%(main_item['item_name']))
                continue
            analyze_methods
            # print("data", data)
        for analyze_method in main_item["page_analyze"]:
            for get_item in analyze_method:
                print("get_item",get_item)
                # print(get_item["work_items"])
        break


if __name__ == "__main__":
    scord_main()