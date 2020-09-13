#!/usr/bin/env python
# coding: utf-8

# In[23]:


import csv
import argparse
import urllib as urllib2
import re

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help="Enter a URL linking to a .csv file.")
args = parser.parse_args()

def downloadData(url):
    
    return datafile

def processData(datafile):
    
    readfile = csv.reader(datafile)
    linecount = 0
    imgcount = 0

    chrome = ['Google Chrome', 0]
    ie = ['Internet Explorer', 0]
    safari = ['Safari', 0]
    Firefox = ['Firefox', 0]
    for line in readfile:
        linecount += 1
        if re.search("firefox", line[2], re.I):
            Firefox[1] += 1
        elif re.search(r"MSIE", line[2]):
            ie[1] += 1
        elif re.search(r"Chrome", line[2]):
            chrome[1] += 1
        elif re.search(r"Safari", line[2]) and not re.search("Chrome", line[2]):
            safari[1] += 1
        if re.search(r"jpe?g|JPE?G|png|PNG|gif|GIF", line[0]):
            imgcount += 1

    img_hit_pct = (float(imgcount) / linecount) * 100

    browser_count = [chrome, ie, safari, fox]

    top_browser = 0
    top_name = ' '
    for b in browser_count:
        if b[1] > top_brwsr:
            top_brwsr = b[1]
            top_name = b[0]
        else:
            continue

    msg = ('There were {} page hits today, image requests account for {}% of '
           'hits. \n{} has the most hits with {}.').format(linecount,
                                                           img_hit_pct,
                                                           top_name,
                                                           top_brwsr)
    print (msg)

def main():
 
    if not args.url:
        raise SystemExit
    try:
        data = downloadData(args.url)
    except urllib2.URLError:
        print ('Please enter a valid URL.')
        raise
    else:
        processData(data)

if __name__ == '__main__':
    main()


# In[ ]:




