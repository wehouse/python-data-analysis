# -*- coding: utf-8 -*-
import pandas as pd

university_towns = pd.DataFrame(columns=["State", "RegionName"])

with open("university_towns.txt", "r") as f:
        state = ""
        for line in f:
            if "[edit]" in line:
                state =line.split("[")[0]
            else:
                university_towns = university_towns.append({"State": state, "RegionName":line.split("(")[0].rstrip()}, ignore_index=True)
print(university_towns)

states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

all_town_data = pd.read_csv('City_Zhvi_AllHomes.csv')
all_town_data["State"].replace(states, inplace=True)

for i in range(2000, 2016):
    firstQ = str(i)+"q1"
    secondQ = str(i)+"q2"
    thirdQ = str(i)+"q3"
    fourthQ = str(i)+"q4"
    jan = str(i)+"-01"
    feb = str(i)+"-02"
    mar = str(i)+"-03"
    apr = str(i)+"-04"
    may = str(i)+"-05"
    jun = str(i)+"-06"
    jul = str(i)+"-07"
    aug = str(i)+"-08"
    sep = str(i)+"-09"
    octo = str(i)+"-10"
    nov = str(i)+"-11"
    dec = str(i)+"-12"
    all_town_data[firstQ] = (all_town_data[jan] + all_town_data[feb] + all_town_data[mar])/3
    all_town_data[secondQ] = (all_town_data[apr] + all_town_data[may] + all_town_data[jun])/3
    all_town_data[thirdQ] = (all_town_data[jul] + all_town_data[aug] + all_town_data[sep])/3
    all_town_data[fourthQ] = (all_town_data[octo] + all_town_data[nov] + all_town_data[dec])/3

all_town_data
