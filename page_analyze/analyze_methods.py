import bs4 

def analyze_methods(page, works_items):
    pass

def get_items(src_items, method, paths):
    if method == 'grad':
        tmps = src_items
        for path in paths:
            tmps2 = []
            for tmp in tmps:
                tmps2 += tmp.select(path)
            tmps = tmps2 
        return tmps
    if method == 'and':
        tmps = []
        for path in paths:
            tmps += src_items.select(path)
        return tmps
    
def get_content(items, get_type):
    contents = []
    for item in items:
        if get_type == 'text':
                contents.append(item.text)
        elif get_type == 'href':
                contents.append(item.get('href'))   
    return contents 