# Data
Repo with data sources and/or code for scraping data.

</br>
</br>

## Datasets in collection
Run the [script](https://github.com/Learning-from-the-curve/Data/blob/master/Get_data.ipynb) to download several datasets on COVID and economics on your local machine. 
The data calls the latest available data (e.g. daily for COVID cases).

### 1. Daily COVID cases and deaths by country from [Johns Hopkins](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series) 
Daily updated information on confirmed cases, deaths and recovered by country/region.

### 2. Population by country from [United Nations](https://population.un.org/wpp/Download/Standard/CSV/) 
Population, country area and population density by country as of Jan 1, 2019.
Also information on demographics: population by age, and fertility by age.

### 3. National accounts EU28 from [Eurostat](https://ec.europa.eu/eurostat/web/population-demography-migration-projections/data/database) 
National accounting identity by EU28 member state: GDP, consumption, investment, trade.
Unemployment by EU28 member state.
Interest rates: short and long term interest rates.

### 4. Daily COVID cases for Belgium by municipality from [Epistat](https://epistat.wiv-isp.be/covid/)
Daily data on confirmed cases by age, sex and province; by date and municipality.
Daily data on hospitalizations by date and province.
Daily data on mortality by date, age, sex and province.
Daily data on total number of tests performed.

</br>
</br>

## Other data sources

This document references several data sources on COVID and economics, which might be of use for conributors.
Sources are grouped by topic and additional sources will be added as the project proceeds. 
Feel free to suggest additional sources by opening an [issue](https://github.com/Learning-from-the-curve/Data/issues).
Datasets that are used intensely from this list can get bumped to the scripted data, again via reporting an [issue](https://github.com/Learning-from-the-curve/Data/issues).

### 1. Policy responses
- **Oxford COVID-19 Government Response Tracker**
  - [Source](https://www.bsg.ox.ac.uk/research/research-projects/oxford-covid-19-government-response-tracker), [Download link](https://www.bsg.ox.ac.uk/sites/default/files/OxCGRT_Download_latest_data.xlsx), [Description](https://www.bsg.ox.ac.uk/sites/default/files/2020-03/BSG-WP-2020-031-v2.0.pdf).
  - Citation: Hale, Thomas and Samuel Webster (2020). Oxford COVID-19 Government Response Tracker.
  
- **Data protection law and the COVID19 outbreak**
  - [Source](https://lsts.research.vub.be/en/data-protection-law-and-the-covid-19-outbreak)
  - Content: a list of what different countries in Europe are doing to guarantee appropriate protection of personal data, during a time in which being able to monitor each and every individual is essential to ensure the success of containment measure 


### 2. Within country heterogeneity
### France
-	**Daily COVID cases for France, detailed by region/department** 
    - [Source](https://github.com/opencovid19-fr/data/blob/master/README.en.md)
    - Content: cas_confirmes, deces, reanimation, hospitalises, gueris, depistes.
  
-	**Daily French public data, detailed by nation/regional/department**
    - [Source](https://geodes.santepubliquefrance.fr/#c=indicator&f=0&i=covid_hospit.hosp&s=2020-03-26&t=a01&view=map2) 
    - Content: number of cases confirmed, number of hospitalizations, number of deaths and number of admissions “en reanimation”, number of individuals recovering at home, number of hospitals having declared at least one positive case since 1st March.

-	**Medical causes and deaths**
    - [Source](https://icd.who.int/browse10/2008/fr)  
    - Content: data on deaths by ICD-10 codes, by department and year, but only up to 2016.
-

### Belgium
- **Population statistics at city level** 
    - [Source](https://statbel.fgov.be/en/themes/population/structure-population)
    - Content: several datasets on number of inhabitants by NIS (city-level), births and fertility, mortality, life excpectancy and causes of death, ...


### Netherlands
- **Weekly deaths by gender and age**
    - [Source](https://opendata.cbs.nl/#/CBS/nl/dataset/70895ned/table?dl=35477)
    - More data [here](https://opendata.cbs.nl/portal.html?_la=nl&_catalog=CBS&tableId=70895ned&_theme=75)
 
 
### Italy
- **Daily COVID cases for Italy, detailed by region**
    - [Source](https://github.com/pcm-dpc/COVID-19/tree/master/dati-regioni)
    - Content: daily updates by region: recovered with symptoms, intensive care, total hospitalized, domestic isolation, tested positive, deaths, ...


### 3. Life expectancy
-	**Global mortality tables by country**
    - [Source](https://population.un.org/wpp/Download/Standard/CSV/)
    - File: WPP2019_Life_Table_Medium
    - Content: Abridged life tables up to age 100 by sex and both sexes combined providing a set of values showing the 
    mortality experience of a hypothetical group of infants born at the same time and subject throughout their lifetime 
    to the specific mortality rates of a given period, from 1950-1955 to 2095-2100.
    
-	**Global period by country**
    - [Source](https://population.un.org/wpp/Download/Standard/CSV/)
    - File: WPP2019_Period_Indicators_Medium
    - Content: Several indicators in 5-year periods, from 1950-1955 to 2095-2100. 
    Including fertility, birth rates, life expectancy, ...
    
-	**Belgian general mortality rates**
    - [Source](https://epistat.wiv-isp.be/momo/)
    - Content: ????
    - [Source](https://statbel.fgov.be/en/open-data/number-deaths-day)
    - Content: number of deaths per day up to 2018
  
-	**Belgian cause of deaths**
    - [Source](https://statbel.fgov.be/en/themes/population/mortality-life-expectancy-and-causes-death/causes-death#figures)
    - Content: yearly deaths by age group and age, by cause of death (up to 2016).
  
-	**Europe general mortality rates**
    - [Source](http://www.euromomo.eu)
  
-	**Epidemiological data, China**
    - [Source](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30119-5/fulltext)
    - Content: Centralised repository of individual-level information on patients with laboratory-confirmed COVID-19


### 4. Humanitarian
-	**Humanitarian Data Exchange:** More than 1700 Gov Interventions across the world
    - [Source](https://data.humdata.org/dataset/acaps-covid19-government-measures-dataset)
    - Content: Category, Measure, Entry Date, Source.
 
 
### 5. Financial data
-	**Daily Prices of National Stock indices**
    - [Source](https://finance.yahoo.com/world-indices/)
    -	APIs: Quandl, Yahoo Finance, OpenFIGI


### 6. Behavioral surveys
- Global (Covid19stop), ongoing
    - [Source](https://www.covid19stop.org/survey)
- Belgium (University of Antwerp), ongoing
    - [Source](https://www.tijd.be/dossiers/coronavirus/34-doden-aantal-ziekenhuisopnames-daalt-voor-tweede-dag-op-rij/10216380.html)
