#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 23:03:42 2023

@author: becker
"""
import json
import numpy as np
import pandas as pd
import requests




url = f'http://comtrade.un.org/api/get?max=10000&type=C&freq=A&px=S2&ps=2021&r=all&p=156&rg=2&cc=AG2'
result    = requests.get(url).json()
if 'dataset' in result: 
	df = pd.DataFrame(result['dataset'])
	df = df.replace({None: np.nan})
	df.columns = [i[:32] for i in df.columns]
df.columns
df.cmdCode.unique()  




url2 = f'http://comtrade.un.org/api/get?max=10000&type=C&freq=A&px=S2&ps=2021&r=all&p=156&rg=1&cc=652'
result2 = requests.get(url2).json()
if 'dataset' in result2: 
	df2 = pd.DataFrame(result2['dataset'])
	df2 = df2.replace({None: np.nan})
	df2.columns = [i[:32] for i in df2.columns]
df2.columns  
df2.cmdCode.unique()

url3 = f'http://comtrade.un.org/api/get?max=10000&type=C&freq=A&ps=2021&r=156&p=all&rg=1&cc=AG2'
result3 = requests.get(url3).json()
if 'dataset' in result3: 
	df3 = pd.DataFrame(result3['dataset'])
	df3 = df3.replace({None: np.nan})
	df3.columns = [i[:32] for i in df3.columns]
df3.columns  
df3.cmdDescE.unique()




    
class comtrade_data:    
    
    def __init__(self):
        
        self.url=f'http://comtrade.un.org/api/get?max=10000'

    def create_string(self,
                      typeTransaction,
                      frequency,
                      year,
                      reporting_country,
                      partner_country,
                      import_export,
                      level):
        
        command = '&type='+typeTransaction
        command = command +'&freq='+ frequency
        command = command + '&ps=' + year
        command = command + '&r=' + reporting_country
        command = command + '&p=' + partner_country
        command = command + '&rg=' + import_export
        command = command + '&cc=' + level

        return self.url+command

    def update_country_codes(self):

        countries_list = pd.DataFrame({'Code':[],
                                       'Country':[],
                                       'ISO':[]})
        
        
        url = f'http://comtrade.un.org/api/get?max=1&type=C&freq=A&px=S2&ps=2019&r=all&p='+str(item)+'&rg=2&cc=AG2'
        
        url = f'http://comtrade.un.org/api/get?max=10000&type=C&freq=A&px=S2&ps=2021&r=all&p=156&rg=2&cc=AG2'
        result = requests.get(url).json()

        try:
            df = pd.DataFrame(result['dataset'])
            df = df.replace({None:np.nan})
            df.columns = [i[:32] for i in df.columns]
            cod = df.rtCode[0]
            country = df.rtTitle[0]
            iso = df.rt3ISO[0]
            this = pd.DataFrame({'Code':[cod],
                                 'Country':[country],
                                 'ISO':[iso]})
            countries_list = countries_list.append(this)
                            
        except:
            next
                
        return countries_list
                
            
getData = comtrade_data()          
lst_paises = getData.get_country_codes()



if 'dataset' in result2: 
	df2 = pd.DataFrame(result2['dataset'])
	df2 = df2.replace({None: np.nan})
	df2.columns = [i[:32] for i in df2.columns]
df2.columns  
df2.cmdCode.unique()

result3 = requests.get(url3).json()            

url       = f'http://comtrade.un.org/api/get?max=10000&type=C&freq=A&px=S2&ps=2021&r=all&p=156&rg=2&cc=AG2'



teste = getData.create_string('C','A','2021','Brazil','all','1','AG2')



level = '3'
str(level)



















    
#what a need is a loop capable of downloading all data from each country
#and from each designation and from each year 