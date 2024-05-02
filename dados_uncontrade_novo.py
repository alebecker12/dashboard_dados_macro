#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:24:54 2023

@author: becker
"""
import sys
import pandas
import requests
import comtradeapicall
from datetime import date
from datetime import timedelta

subscription_key = '7242c56512284d4c97083bff365ac6a7' # comtrade api subscription key (from comtradedeveloper.un.org)
directory = '<OUTPUT DIR>'  # output directory for downloaded files 


from datetime import date
from datetime import timedelta
today = date.today()
yesterday = today - timedelta(days=1)
lastweek = today - timedelta(days=7)

mydf = comtradeapicall.previewFinalData(typeCode='C', freqCode='A', clCode='HS', period='2021',
                                        reporterCode='842', cmdCode='20230', flowCode='M', partnerCode=None,
                                        partner2Code=None,
                                        customsCode=None, motCode=None, maxRecords=500, format_output='JSON',
                                        aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)




mydf = comtradeapicall.getFinalData(subscription_key,typeCode='C', freqCode='A', clCode='HS', period='2021',
                                        reporterCode='36', cmdCode='20230', flowCode='M', partnerCode=None,
                                        partner2Code=None,
                                        customsCode=None, motCode=None, maxRecords=None, format_output='JSON',
                                        aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)


mydfChina = comtradeapicall.getFinalData(subscription_key,typeCode='C', freqCode='A', clCode='HS', period='2021',
                                        reporterCode='156', cmdCode=None, flowCode='M', partnerCode=None,
                                        partner2Code=None,
                                        customsCode=None, motCode=None, maxRecords=None, format_output='JSON',
                                        aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)

dfUSA = comtradeapicall.getFinalData(subscription_key,typeCode='C', freqCode='A', clCode='HS', period='2018',
                                        reporterCode='842', cmdCode=None, flowCode='M', partnerCode=None,
                                        partner2Code=None,
                                        customsCode=None, motCode=None, maxRecords=None, format_output='JSON',
                                        aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)



mydf20230 = comtradeapicall.getFinalData(subscription_key,typeCode='C', freqCode='A', clCode='HS', period='2021',
                                        reporterCode='36', cmdCode='31', flowCode='M', partnerCode=None,
                                        partner2Code=None,
                                        customsCode=None, motCode=None, maxRecords=None, format_output='JSON',
                                        aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)

mydf20230.h



mydf2 = comtradeapicall.getFinalData(subscription_key,typeCode='C', freqCode='M', clCode='HS', 
                                     period='202002',
                                        reporterCode='156', cmdCode='91', flowCode='M', partnerCode=None,
                                        partner2Code=None,
                                        customsCode=None, motCode=None, maxRecords=None, format_output='JSON',
                                        aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)
mydf2.period.unique()


mydf.columns

countryCodes = mydf[['partnerCode','partnerDesc']]

codes = mydf[['cmdCode','cmdDesc']].drop_duplicates()
codesChina = mydfChina[['cmdCode','cmdDesc']].drop_duplicates()

#adiciona os códigos da china
codes = codes.append(codesChina)

#limpa duplicadas
codes = codes.drop_duplicates()

#cicle all countries and check for the codes



#test api for retrieving the codes
countries = comtradeapicall.getReference('partner')

cmdCodes = comtradeapicall.listReference()

productsH6 = comtradeapicall.getReference('cmd:H6')







