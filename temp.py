# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from textblob import TextBlob
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

class Analysis:
    def __init__(self,term):
        self.term=term
        self.sentiment=0
        self.subjectivity=0
        self.url='https://uk.trustpilot.com/review/atombank.co.uk?page=1'.format(self.term)
    
    def run(self):
        response=requests.get(self.url)
        #print(response.text)
        soup=BeautifulSoup(response.text,'html.parser')
        #print(soup.prettify())
        headline_results=soup.find_all('p')
        #headline_results=soup.findAll('reviewBody')
        links=[]
        comms=[]
        for text in headline_results:
            blob=TextBlob(text.get_text())
            print(blob)
        #    comms.append(blob.string)
        #print(comms)
        #comms=pd.DataFrame(comms)
        #comms.to_csv(r'C:\Users\Admin\Documents\Results\comments.csv')
r'''
            if (text.get('href')).find("/url?q=") >=0:
                print(text.get('href')[7:text.get('href').find("&sa=U")])
                links.append(text.get('href')[7:text.get('href').find("&sa=U")])
                print(text.get('href'))
                self.sentiment+=blob.sentiment.polarity / len(headline_results)
                self.subjectivity+=blob.sentiment.subjectivity / len(headline_results)
                print(blob, self.sentiment, blob.subjectivity)
                links=pd.DataFrame(links)
                print(links)
r'''   
            

a=Analysis('null')
a.run()
                                                                                                      
