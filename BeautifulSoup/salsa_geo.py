# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 20:43:06 2018

@author: mbodtke
"""
from time import sleep
import pandas as pd

def salsa_geo(url_prefix, bike):
    '''
    Takes url from salsa cycles website and returns dictionary containing
    geometry data
    '''
    
    import requests
    from bs4 import BeautifulSoup
    url = url_prefix + bike
    html = requests.get(url)

    #turn into BS object 
    soup = BeautifulSoup(html.text,'html.parser')
    
    #grab geometry table - this will likely be site specific
    geometry = soup.find(id='geometry')
    
    #we only want table information
    geo_table = geometry.table
    
    geo_rows = geo_table.find_all('tr')
    
    #parse geometry table into dictionary
    geo_dict = {} #initialize empty dictionary to store data
    for idx, tr in enumerate(geo_rows):
        if idx == 0:
            header = [i.text for i in tr.find_all('th')]
            geo_dict[header[0]]=header[1:] # creates sizes
            geo_dict['Model']=[bike]*(len(header) - 1)
        else:
            row_header = tr.find('th').text
            row_data = [i.text for i in tr.find_all('td')] #.append(header[idx-1])  #add index col
            geo_dict[row_header]=row_data  #store row in dict.  
    
    return geo_dict

#Is it scary that I produced this list from my memory?
bike_list = [
'beargrease'
,'mukluk'
,'blackborow'
,'journeyman'
,'timberjack_kids'
,'deadwood'
,'redpoint'
,'pony_rustler'
,'marrakesh'
,'fargo'
,'vaya'
,'cutthroat'
,'warbird'
,'woodsmoke'
,'timberjack'
,'bucksaw'
,'spearfish'
,'horsethief'
,'powderkeg']

#all bike pages are structured such that url = url_prefix+bike[i]
url_prefix='https://salsacycles.com/bikes/'

df_list = []
#loop through bike list, grab geometry data, and save it to the dict
for bike in bike_list:
    sleep(2)  #ultra-cautious delay to avoid accidentally overloading salsa servers or getting blocked
    df_list.append(pd.DataFrame(salsa_geo(url_prefix,bike)))
    
geo_df = pd.concat(df_list,sort=False)
geo_df.set_index(['Model','Size'],inplace=True)
geo_df.to_csv('salsa_geometry.csv')
print('program complete')

