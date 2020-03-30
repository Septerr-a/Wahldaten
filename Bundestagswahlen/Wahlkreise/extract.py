# This file extracts the data from the csv files published by the bundeswahlleiter and puts it into JSON files

import pandas as pd
import os
import math
import json

# you might want to switch to the directory this file is located in manually
os.chdir("YOURPATH/Wahldaten/Bundestagswahlen/Wahlkreise")

# thirst rows to ignore (start with 1, include header)
rows_empty = 8

# read csv file 
data = pd.read_csv("src/Wahlkreise_BTW17.csv",encoding='ISO-8859-1',sep=";",skiprows=lambda x: x < rows_empty, engine='python')

# make dicts
data_json = {'copyright': "(c) Der Bundeswahlleiter, Statistische Ämter des Bundes und der Länder, Wiesbaden 2017. Vervielfältigung und Verbreitung, auch auszugsweise, mit Quellenangabe gestattet.", "status": "28.02.2017", "data": {}}

# iterate over it to get plz mapping
for index,row in data.iterrows():
    if not math.isnan(row[15]):
        data_json['data'][str(int(row[15]))] = {"wahlkreis_nummer": str(row[0]), "wahlkreis_bezeichnung": str(row[1]), "bundesland": str(row[7]), "kreis": str(row[9]), "gemeinde": str(row[10])}
    
with open('wahlkreise_btw_plz.json', 'w',encoding="utf-8") as fp:
    json.dump(data_json, fp,ensure_ascii=False)

# make dicts
data_json = {'copyright': "(c) Der Bundeswahlleiter, Statistische Ämter des Bundes und der Länder, Wiesbaden 2017. Vervielfältigung und Verbreitung, auch auszugsweise, mit Quellenangabe gestattet.", "status": "28.02.2017", "data": {}}

# iterate over it to get gemeinde mapping
for index,row in data.iterrows():
    if not math.isnan(row[15]):
        data_json['data'][str(row[10])] = {"wahlkreis_nummer": str(row[0]), "wahlkreis_bezeichnung": str(row[1]), "bundesland": str(row[7]), "kreis": str(row[9]), "plz": str(int(row[15]))}
    
with open('wahlkreise_btw_gemeinde.json', 'w',encoding="utf-8") as fp:
    json.dump(data_json, fp,ensure_ascii=False)

# make dicts
data_json = {'copyright': "(c) Der Bundeswahlleiter, Statistische Ämter des Bundes und der Länder, Wiesbaden 2017. Vervielfältigung und Verbreitung, auch auszugsweise, mit Quellenangabe gestattet.", "status": "28.02.2017", "data": {}}

# iterate over it to get wahlkreis mapping
for index,row in data.iterrows():
    if not math.isnan(row[15]):
        if str(row[1]) in data_json['data']:
            data_json['data'][str(row[1])]['plz'].append(str(int(row[15])))
        else:
            data_json['data'][str(row[1])] = {"wahlkreis_nummer": str(row[0]), "bundesland": str(row[7]), "plz": [str(int(row[15]))]}
    
with open('wahlkreise_btw_wahlkreis.json', 'w',encoding="utf-8") as fp:
    json.dump(data_json, fp,ensure_ascii=False)

# make dicts
data_json = {'copyright': "(c) Der Bundeswahlleiter, Statistische Ämter des Bundes und der Länder, Wiesbaden 2017. Vervielfältigung und Verbreitung, auch auszugsweise, mit Quellenangabe gestattet.", "status": "28.02.2017", "data": {}}

# iterate over it to get wahlkreisnummer mapping
for index,row in data.iterrows():
    if not math.isnan(row[15]):
        if str(row[1]) in data_json['data']:
            data_json['data'][str(row[0])]['plz'].append(str(int(row[15])))
        else:
            data_json['data'][str(row[0])] = {"wahlkreis_bezeichnung": str(row[1]), "bundesland": str(row[7]), "plz": [str(int(row[15]))]}
    
with open('wahlkreise_btw_wahlkreisnummer.json', 'w',encoding="utf-8") as fp:
    json.dump(data_json, fp,ensure_ascii=False)

