# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:15:57 2019

@author: Ja
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:24:32 2019

@author: Ja
"""

from textblob import TextBlob
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

banks=['atombank.co.uk', 'wyelandsbank.co.uk', 'countingup.com', 'www.monese.com',
       'starlingbank.com', 'www.monzo.com', 'thinkmoney.co.uk', 'securetrustbank.com',
       'anna.money', 'selinafinance.co.uk', 'www.sainsburysbank.co.uk',
       'tide.co', 'smartsavebank.co.uk', 'www.metrobankonline.co.uk', 'www.loot.io',
       'triodos.co.uk', 'co-operativebank.co.uk', 'www.compte-interdit-bancaire.net',
       'www.monese.com', 'www.firstdirect.com', 'starlingbank.com', 'uaccount.uk']


comms=[]
bank_comms=[]

for bank in banks:
    for i in range(250):
        print("bank: {0}, i: {1}".format(bank, i+1))
        
        #url='https://uk.trustpilot.com/review/atombank.co.uk?page={0}'.format(i+1)
        
        url='https://uk.trustpilot.com/review/{1}?page={0}'.format(i+1, bank)
        

        
        response=requests.get(url)
        
        soup=BeautifulSoup(response.text,'html.parser')
        
        headline_results=soup.find_all('p')
        
        for text in headline_results:
            blob=TextBlob(text.get_text())
            comms.append(text.get_text().strip())
            bank_comms.append(bank.strip())
comms=pd.DataFrame(comms)
bank_comms=pd.DataFrame(bank_comms)
#bank_comms.join(comms)
result=pd.concat([bank_comms, comms], axis=1)
print(result)
result.to_csv(r'C:\Users\Admin\Documents\Results\comments_full.csv')