#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime
import logging
import csv
import urllib.request as urllib2 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help="Enter a URL linking")
args = parser.parse_args()


logging.basicConfig(filename='errors.log', level=logging.ERROR)
logger = logging.getLogger('assignment2')

                        
def downloadData(url):
    urlfile = urllib2.urlopen('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv').read()
                              
return urlfile
                                                             
def processData(urlfile):
    processfile = csv.DitcReader(urlfile)
    newdict = {}

    for num, line in enumerate(read):
        try:
            born = datetime.datetime.strptime(line['birthday'], '%d/%m/%Y')
            newdict[line['id']] = (line['name'], born)
        except:
            logging.error('Error processing line #{} for ID# {}'.format(
                num, line['id']))
        return newdict


def displayPerson(id, personData):
    idnum = str(id)
    if num in personData.keys():
        print ('Person #{} is {} with a birthday of {}').format(
            id, personData[num][0], datetime.datetime.strftime(personData[num][1], '%Y-%m-%d'))
    
    else:
        print ('No user found with that ID.')
         


def main():
    if not args.url:
        raise SystemExit
    try:
        csvData = downloadData(args.url)
    except urllib2.URLError:
        print ('Please enter a valid URL.')
        raise
    else:
        personData = processData(csvData)
        personid = int(input('Please enter an ID'))
        print(personid)
        personid = int(personid)
        if personid <= 0:
            print ('Person ID <= to 0')
            raise SystemExit
        else:
            displayPerson(personid, personData)
            main()
            

if __name__ == '__main__':
    main()


# In[ ]:




