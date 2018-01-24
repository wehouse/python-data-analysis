import pandas as pd
from string import digits


def answer_one():
    energy = (pd.read_excel('Energy Indicators.xls', 
                skip_footer=38, 
                usecols=range(2,6), 
                skiprows=17, 
                na_values=['...'],
                names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']))
    #Fix country names
    energy.Country = (energy.Country.replace(to_replace={"Republic of Korea": "South Korea", "United States of America20": "United States",
    "United Kingdom of Great Britain and Northern Ireland19": "United Kingdom",
    "China, Hong Kong Special Administrative Region3": "Hong Kong"}))
    
    #Fix names with numbers in them
    #df.Country = (df.Country.replace(to_replace={"Australia1":"Australia", "China2":"China"}))
    energy.Country = energy.Country.str.translate({ord(k): None for k in digits})
    
    #Paranthesis countries
    energy.Country = (energy.Country.replace(to_replace={"Bolivia (Plurinational State of)":"Bolivia", 
                                                 "Falkland Islands (Malvinas)":"Falkland Islands", 
                                                 "Iran (Islamic Republic of)":"Iran",
                                                 "Micronesia (Federated States of)":"Micronesia",
                                                 "Sint Maarten (Dutch part)":"Sint Maarten",
                                                 "Venezuela (Bolivarian Republic of)":"Venezuela"}))
    
    gdp = pd.read_csv("world_bank.csv", skiprows=4)
    gdp["Country Name"] = gdp["Country Name"].replace(to_replace={"Korea, Rep.": "South Korea", 
    "Iran, Islamic Rep.": "Iran",
    "Hong Kong SAR, China": "Hong Kong"})
    gdp[gdp["Country Name"].str.contains("Iran")]
    
    merged = pd.merge(energy, gdp, how='inner', left_on='Country', right_on='Country Name')
    merged_col_filtered = merged[['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable','2006', '2007', '2008',
           '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    
    
    ScimEn = pd.read_excel("scimagojr-3.xlsx")
    final_merged = pd.merge(merged_col_filtered, ScimEn, how='inner', on='Country')
    final_merged.sort_values('Rank', ascending=1,inplace=True)
    ret_rdy = final_merged.head(15).set_index("Country")
    ret_rdy['Energy Supply'] = ret_rdy['Energy Supply'] * 1000000

    return ret_rdy

answer_one()

def answer_two():
    return 156

answer_two()

def answer_three():
    top15 = answer_one()
    top15['2015'] = top15['2015'].fillna(value=0)
    top15['Average GDP'] = (top15['2006'] + top15['2007'] +top15['2008'] + top15['2009'] + top15['2010'] + top15['2011'] + top15['2012'] + top15['2013'] + top15['2014'] + top15['2015'])/10
    top15['Average GDP']
    top15.sort_values('Average GDP', ascending=0, inplace=True)
    return pd.Series(top15['Average GDP'], index=top15.index.values)

answer_three()

def answer_four():
    top15 = answer_one()
    top15['2015'] = top15['2015'].fillna(value=0)
    top15['Average GDP'] = (top15['2006'] + top15['2007'] +top15['2008'] + top15['2009'] + top15['2010'] + top15['2011'] + top15['2012'] + top15['2013'] + top15['2014'] + top15['2015'])/10
    top15['Average GDP']
    top15.sort_values('Average GDP', ascending=0, inplace=True)
    return top15.iloc[5]['2015'] - top15.iloc[5]['2006']

answer_four()

def answer_five():
    Top15 = answer_one()
    return Top15['Energy Supply per Capita'].mean()

answer_five()

def answer_six():
    Top15 = answer_one()
    Top15.sort_values('% Renewable', ascending=0, inplace=True)
    Top15 = Top15.reset_index()
    return (Top15.iloc[0]['Country'], Top15.iloc[0]['% Renewable'])

answer_six()

def answer_seven():
    Top15 = answer_one()
    Top15["SelfCitRatio"] = Top15['Self-citations'] / Top15['Citations']
    Top15RI = Top15.reset_index()
    return (Top15RI.nlargest(1,'SelfCitRatio')['Country'].iloc[0], Top15RI.nlargest(1,'SelfCitRatio')['SelfCitRatio'].iloc[0])

answer_seven()

Top15Pop=answer_one()

def answer_eight():
    Top15Pop['Population'] = Top15Pop['Energy Supply'] / Top15Pop['Energy Supply per Capita']
    Top15RI = Top15Pop.sort_values('Population', ascending=0)
    Top15RI = Top15RI.reset_index()
    return Top15RI.iloc[2]['Country']

answer_eight()

def answer_nine():
    Top15Pop['CitDocCapita'] = Top15Pop['Citable documents'] / Top15Pop['Population']
    return Top15Pop['CitDocCapita'].corr(Top15Pop['Energy Supply per Capita'])

answer_nine()

def answer_ten():
    median = Top15Pop['% Renewable'].median()
    Top15Pop['RenewableMed'] =(Top15Pop['% Renewable'] >= median)
    Top15RI = Top15Pop.sort_values(by=['Rank'])
    index = list(Top15RI.index.values)
    return pd.Series(Top15RI['RenewableMed'].values, index = index)

answer_ten()

ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}

def answer_eleven():
    return Top15Pop.groupby(ContinentDict)['Population'].agg(['size', 'sum', 'min', 'std'])

answer_eleven()

def answer_twelve():
    return Top15Pop.groupby([ContinentDict,pd.cut(Top15Pop['% Renewable'], 5)])['Population'].agg(['size'])['size']

answer_twelve()

def answer_thirteen():
    return Top15Pop.apply(lambda x: "{:,}".format(x['Population']), axis=1)

answer_thirteen()