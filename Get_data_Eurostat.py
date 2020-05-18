# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:33:01 2020

@author: Fabrizio Leone & Learning From the Curve Team
"""

# Import libraries
# If some package is missing type pip install --namepackage
import pandas as pd
import numpy as np
import os
import eurostat
from concurrent.futures import ThreadPoolExecutor
import time

# Define function to get data from John Hopkins
start_time = time.time()


# Define function to get data from Eurostat
def data_Eurostat(url, container):
    ind = 0
    for i in url:
        if ind <= len(url):
            container.append([url[ind][0], eurostat.get_data_df(url[ind][1])])
        ind += 1

Eurostat_code = [['EU_pop', 'demo_r_gind3'], ['EU_gdp', 'nama_10_gdp'], ['EU_cons', 'nama_10_fcs'], ['EU_trade', 'nama_10_exi'], ['EU_short_rate', 'irt_st_a'],
                ['EU_long_rate', 'irt_lt_gby10_a'], ['EU_unemp', 'une_rt_a'], ['EU_inv', 'nama_10_an6']]            

# Download all data
JH  = []
WPP = []
EU  = []
OX  = []
BE  = []

with ThreadPoolExecutor(max_workers = 5) as e:
    e.submit(data_Eurostat(Eurostat_code, EU))




# Save all data
def store_data(path = os.getcwd(), EU_data = True):
    os.makedirs(path, exist_ok = True)
    if EU_data:
        ind = 0
        for i in EU:
            EU[ind][1].to_csv(path + EU[ind][0] + '.csv', index = False)
            ind += 1

store_data(os.getcwd() + "/files/")
end_time = time.time()
print(f"Total time: {end_time - start_time}")