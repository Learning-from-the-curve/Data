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

def data_JH(url, container):
    ind = 0
    for i in url:
        if ind <= len(url):
            container.append([url[ind][0],pd.read_csv(url[ind][1], index_col = 0, parse_dates = [0])])
        ind += 1

url_WPP = [['WPP_tot_pop', 'https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2019_TotalPopulationBySex.csv'],
          ['WPP_pop_age_sec', 'https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2019_PopulationByAgeSex_Medium.csv'],
          ['WPP_fertility', 'https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2019_Fertility_by_Age.csv']]

url_JH = [['JH_confirmed', 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'],
            ['JH_death', 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'],
            ['JH_recovered', 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv']]

# Define function to get data from Eurostat
def data_Eurostat(url, container):
    ind = 0
    for i in url:
        if ind <= len(url):
            container.append([url[ind][0], eurostat.get_data_df(url[ind][1])])
        ind += 1

Eurostat_code = [['EU_pop', 'demo_r_gind3'], ['EU_gdp', 'nama_10_gdp'], ['EU_cons', 'nama_10_fcs'], ['EU_trade', 'nama_10_exi'], ['EU_short_rate', 'irt_st_a'],
                ['EU_long_rate', 'irt_lt_gby10_a'], ['EU_unemp', 'une_rt_a'], ['EU_inv', 'nama_10_an6']]            

# Define function to get data from Oxford
def data_Ox(url, container):
    ind = 0
    for i in url:
        if ind <= len(url):
            container.append([url[ind][0],pd.read_excel(url[ind][1], index_col = 0, parse_dates = [0])])
        ind += 1

url_Ox = [['OX_govt_responses', 'https://www.bsg.ox.ac.uk/sites/default/files/OxCGRT_Download_latest_data.xlsx']]

# Define function to get data from Sciensano-Belgium
def data_Belgium(url, container):
    ind = 0
    for i in url:
        if ind <= len(url):
            container.append([url[ind][0],pd.read_csv(url[ind][1], index_col = 0, parse_dates = [0], encoding = "ISO-8859-1")])
        ind += 1
        
url_Belgium = [['Confirmed_cases_by_date_age_sex_and_province', 'https://epistat.sciensano.be/Data/COVID19BE_CASES_AGESEX.csv'],
               ['Confirmed_cases_by_date_and_municipality', 'https://epistat.sciensano.be/Data/COVID19BE_CASES_MUNI.csv'],
               ['Cumulative_number_of_confirmed_cases_by_municipality', 'https://epistat.sciensano.be/Data/COVID19BE_CASES_MUNI_CUM.csv'],
               ['Hospitalisations_by_date_and_provinces', 'https://epistat.sciensano.be/Data/COVID19BE_HOSP.csv'],
               ['Mortality_by_date_age_sex_and_province', 'https://epistat.sciensano.be/Data/COVID19BE_MORT.csv'],
               ['Total_number_of_tests_performed_by_date', 'https://epistat.sciensano.be/Data/COVID19BE_tests.csv']]

# Download all data
JH  = []
WPP = []
EU  = []
OX  = []
BE  = []

with ThreadPoolExecutor(max_workers = 5) as e:
    e.submit(data_JH(url_JH, JH))
    e.submit(data_JH(url_WPP, WPP))
    e.submit(data_Eurostat(Eurostat_code, EU))
    e.submit(data_Ox(url_Ox, OX))
    e.submit(data_Belgium(url_Belgium, BE))

# Define function to reshape JH data
def reshape_JH(JH,JH_reshaped):
    
    for j in range(len(JH)):
    
        # Get and clean an entry of the JH list
        tmp = pd.DataFrame(JH[j][1])
        tmp = tmp.drop(['Lat', 'Long'], axis=1)

        # Rename columns
        tmp.columns = tmp.columns.str.replace('/','')
        new_names = [(i,'Date' + i) for i in tmp.iloc[:, 1:].columns.values]
        tmp.rename(columns = dict(new_names), inplace=True)

        # Rename rows
        tmp.index = pd.Series(tmp.index).replace(np.nan, 'Unique')

        # Create a new ID = row name + first column
        tmp['idx'] = tmp.index
        tmp = tmp.set_index(['CountryRegion', 'idx'])
        tmp['idx'] = tmp.index
        tmp = tmp.reset_index(drop=True)

        # Reshape wide to long
        tmp = pd.wide_to_long(tmp, ["Date"], i="idx", j="date")
        tmp = tmp.rename(columns = {'Date':'occurrences'})

        # Clean index
        idx = []
        cou = []
        reg = []
        date = []
        for k in range(len(tmp.index)):
            idx.append(list(tmp.index[k])[0])
            date.append(list(tmp.index[k])[1])
        
        # Get country and region identifier
        for i in range(len(idx)):
            cou.append(idx[i][0])
            reg.append(idx[i][1])
            
        # Finalize dataset
        tmp['country'] = cou  
        tmp['region'] = reg  
        tmp['date'] = [str(i)+'20' for i in date]
        tmp['date'] = pd.to_datetime(tmp['date'], format='%m%d%Y', errors='coerce')
        tmp = tmp.reset_index(drop=True)
        tmp = tmp[["country", "region", "date", "occurrences"]]

        # Store output in a new list
        JH_reshaped.append([JH[j][0], tmp])
        
    #Return
    return(JH_reshaped)

JH_reshaped = []
JH_reshaped = reshape_JH(JH,JH_reshaped)

# Save all data
def store_data(path = os.getcwd(), JH_data = True, WPP_data = True, EU_data = True, Ox_data = True, BE_data = True):
    os.makedirs(path, exist_ok = True)
    if JH_data:
        ind = 0
        for i in JH_reshaped:
            JH_reshaped[ind][1].to_csv(path + JH_reshaped[ind][0] + '.csv', index = False)
            ind += 1
    if WPP_data:
        ind = 0
        for i in WPP:
            WPP[ind][1].to_csv(path + WPP[ind][0] + '.csv', index = False)
            ind += 1
    if EU_data:
        ind = 0
        for i in EU:
            EU[ind][1].to_csv(path + EU[ind][0] + '.csv', index = False)
            ind += 1
    if Ox_data:
        ind = 0
        for i in OX:
            OX[ind][1].to_csv(path + OX[ind][0] + '.csv', index = False)
            ind += 1
    if BE_data:
        ind = 0
        for i in BE:
            BE[ind][1].to_csv(path + BE[ind][0] + '.csv', index = False)
            ind += 1

store_data(os.getcwd() + "/files/")
end_time = time.time()
print(f"Total time: {end_time - start_time}")