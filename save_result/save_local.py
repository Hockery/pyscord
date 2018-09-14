import os, time, urllib, random



def download_file(url, file_path, random_time):
    if os.access(file_path, os.F_OK):
        return
    dir_name = os.path.dirname(file_path)
    if not os.access(dir_name, os.F_OK):
        os.mkdir( dir_name, 777 )
    sleep_random = random.randint(random_time[0],random_time[1])/1000
    time.sleep(sleep_random)
    try:
        f = urllib.request.urlopen(url) 
    except:
        print("download file error!")
        return
    data = f.read() 
    with open(file_path, "wb") as code:     
        code.write(data)


def write_context(txt_name, item_name):
    # save_path = os.path.join(download_dir, txt_title+".txt")
    try:
        text_file = open(txt_name,'w+')
    except:
        print("Can't open file[%s]!"%(txt_name))
        
    for item in item_name:
        text_file.write(item.text+'\n')


