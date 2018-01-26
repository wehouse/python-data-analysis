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
all_town_data["2000q1"] = (all_town_data["2000-01"] + all_town_data["2000-02"] + all_town_data["2000-03"])/3
all_town_data["2000q2"] = (all_town_data["2000-04"] + all_town_data["2000-05"] + all_town_data["2000-06"])/3
all_town_data["2000q3"] = (all_town_data["2000-07"] + all_town_data["2000-08"] + all_town_data["2000-09"])/3
all_town_data["2000q4"] = (all_town_data["2000-10"] + all_town_data["2000-11"] + all_town_data["2000-12"])/3

all_town_data["2001q1"] = (all_town_data["2001-01"] + all_town_data["2001-02"] + all_town_data["2001-03"])/3
all_town_data["2001q2"] = (all_town_data["2001-04"] + all_town_data["2001-05"] + all_town_data["2001-06"])/3
all_town_data["2001q3"] = (all_town_data["2001-07"] + all_town_data["2001-08"] + all_town_data["2001-09"])/3
all_town_data["2001q4"] = (all_town_data["2001-10"] + all_town_data["2001-11"] + all_town_data["2001-12"])/3

all_town_data["2002q1"] = (all_town_data["2002-01"] + all_town_data["2002-02"] + all_town_data["2002-03"])/3
all_town_data["2002q2"] = (all_town_data["2002-04"] + all_town_data["2002-05"] + all_town_data["2002-06"])/3
all_town_data["2002q3"] = (all_town_data["2002-07"] + all_town_data["2002-08"] + all_town_data["2002-09"])/3
all_town_data["2002q4"] = (all_town_data["2002-10"] + all_town_data["2002-11"] + all_town_data["2002-12"])/3

all_town_data["2003q1"] = (all_town_data["2003-01"] + all_town_data["2003-02"] + all_town_data["2003-03"])/3
all_town_data["2003q2"] = (all_town_data["2003-04"] + all_town_data["2003-05"] + all_town_data["2003-06"])/3
all_town_data["2003q3"] = (all_town_data["2003-07"] + all_town_data["2003-08"] + all_town_data["2003-09"])/3
all_town_data["2003q4"] = (all_town_data["2003-10"] + all_town_data["2003-11"] + all_town_data["2003-12"])/3

all_town_data["2004q1"] = (all_town_data["2004-01"] + all_town_data["2004-02"] + all_town_data["2004-03"])/3
all_town_data["2004q2"] = (all_town_data["2004-04"] + all_town_data["2004-05"] + all_town_data["2004-06"])/3
all_town_data["2004q3"] = (all_town_data["2004-07"] + all_town_data["2004-08"] + all_town_data["2004-09"])/3
all_town_data["2004q4"] = (all_town_data["2004-10"] + all_town_data["2004-11"] + all_town_data["2004-12"])/3

all_town_data["2005q1"] = (all_town_data["2005-01"] + all_town_data["2005-02"] + all_town_data["2005-03"])/3
all_town_data["2005q2"] = (all_town_data["2005-04"] + all_town_data["2005-05"] + all_town_data["2005-06"])/3
all_town_data["2005q3"] = (all_town_data["2005-07"] + all_town_data["2005-08"] + all_town_data["2005-09"])/3
all_town_data["2005q4"] = (all_town_data["2005-10"] + all_town_data["2005-11"] + all_town_data["2005-12"])/3

all_town_data["2005q1"] = (all_town_data["2005-01"] + all_town_data["2005-02"] + all_town_data["2005-03"])/3
all_town_data["2005q2"] = (all_town_data["2005-04"] + all_town_data["2005-05"] + all_town_data["2005-06"])/3
all_town_data["2005q3"] = (all_town_data["2005-07"] + all_town_data["2005-08"] + all_town_data["2005-09"])/3
all_town_data["2005q4"] = (all_town_data["2005-10"] + all_town_data["2005-11"] + all_town_data["2005-12"])/3

all_town_data["2005q1"] = (all_town_data["2005-01"] + all_town_data["2005-02"] + all_town_data["2005-03"])/3
all_town_data["2005q2"] = (all_town_data["2005-04"] + all_town_data["2005-05"] + all_town_data["2005-06"])/3
all_town_data["2005q3"] = (all_town_data["2005-07"] + all_town_data["2005-08"] + all_town_data["2005-09"])/3
all_town_data["2005q4"] = (all_town_data["2005-10"] + all_town_data["2005-11"] + all_town_data["2005-12"])/3

all_town_data["2005q1"] = (all_town_data["2005-01"] + all_town_data["2005-02"] + all_town_data["2005-03"])/3
all_town_data["2005q2"] = (all_town_data["2005-04"] + all_town_data["2005-05"] + all_town_data["2005-06"])/3
all_town_data["2005q3"] = (all_town_data["2005-07"] + all_town_data["2005-08"] + all_town_data["2005-09"])/3
all_town_data["2005q4"] = (all_town_data["2005-10"] + all_town_data["2005-11"] + all_town_data["2005-12"])/3

all_town_data["2005q1"] = (all_town_data["2005-01"] + all_town_data["2005-02"] + all_town_data["2005-03"])/3
all_town_data["2005q2"] = (all_town_data["2005-04"] + all_town_data["2005-05"] + all_town_data["2005-06"])/3
all_town_data["2005q3"] = (all_town_data["2005-07"] + all_town_data["2005-08"] + all_town_data["2005-09"])/3
all_town_data["2005q4"] = (all_town_data["2005-10"] + all_town_data["2005-11"] + all_town_data["2005-12"])/3

all_town_data["2005q1"] = (all_town_data["2005-01"] + all_town_data["2005-02"] + all_town_data["2005-03"])/3
all_town_data["2005q2"] = (all_town_data["2005-04"] + all_town_data["2005-05"] + all_town_data["2005-06"])/3
all_town_data["2005q3"] = (all_town_data["2005-07"] + all_town_data["2005-08"] + all_town_data["2005-09"])/3
all_town_data["2005q4"] = (all_town_data["2005-10"] + all_town_data["2005-11"] + all_town_data["2005-12"])/3

all_town_data["2005q1"] = (all_town_data["2005-01"] + all_town_data["2005-02"] + all_town_data["2005-03"])/3
all_town_data["2005q2"] = (all_town_data["2005-04"] + all_town_data["2005-05"] + all_town_data["2005-06"])/3
all_town_data["2005q3"] = (all_town_data["2005-07"] + all_town_data["2005-08"] + all_town_data["2005-09"])/3
all_town_data["2005q4"] = (all_town_data["2005-10"] + all_town_data["2005-11"] + all_town_data["2005-12"])/3

all_town_data["2005q1"] = (all_town_data["2005-01"] + all_town_data["2005-02"] + all_town_data["2005-03"])/3
all_town_data["2005q2"] = (all_town_data["2005-04"] + all_town_data["2005-05"] + all_town_data["2005-06"])/3
all_town_data["2005q3"] = (all_town_data["2005-07"] + all_town_data["2005-08"] + all_town_data["2005-09"])/3
all_town_data["2005q4"] = (all_town_data["2005-10"] + all_town_data["2005-11"] + all_town_data["2005-12"])/3

all_town_data["2005q1"] = (all_town_data["2005-01"] + all_town_data["2005-02"] + all_town_data["2005-03"])/3
all_town_data["2005q2"] = (all_town_data["2005-04"] + all_town_data["2005-05"] + all_town_data["2005-06"])/3
all_town_data["2005q3"] = (all_town_data["2005-07"] + all_town_data["2005-08"] + all_town_data["2005-09"])/3
all_town_data["2005q4"] = (all_town_data["2005-10"] + all_town_data["2005-11"] + all_town_data["2005-12"])/3

all_town_data["2005q1"] = (all_town_data["2005-01"] + all_town_data["2005-02"] + all_town_data["2005-03"])/3
all_town_data["2005q2"] = (all_town_data["2005-04"] + all_town_data["2005-05"] + all_town_data["2005-06"])/3
all_town_data["2005q3"] = (all_town_data["2005-07"] + all_town_data["2005-08"] + all_town_data["2005-09"])/3
all_town_data["2005q4"] = (all_town_data["2005-10"] + all_town_data["2005-11"] + all_town_data["2005-12"])/3

all_town_data["2005q1"] = (all_town_data["2005-01"] + all_town_data["2005-02"] + all_town_data["2005-03"])/3
all_town_data["2005q2"] = (all_town_data["2005-04"] + all_town_data["2005-05"] + all_town_data["2005-06"])/3
all_town_data["2005q3"] = (all_town_data["2005-07"] + all_town_data["2005-08"] + all_town_data["2005-09"])/3
all_town_data["2005q4"] = (all_town_data["2005-10"] + all_town_data["2005-11"] + all_town_data["2005-12"])/3

all_town_data["2005q1"] = (all_town_data["2005-01"] + all_town_data["2005-02"] + all_town_data["2005-03"])/3
all_town_data["2005q2"] = (all_town_data["2005-04"] + all_town_data["2005-05"] + all_town_data["2005-06"])/3
all_town_data["2005q3"] = (all_town_data["2005-07"] + all_town_data["2005-08"] + all_town_data["2005-09"])/3
all_town_data["2005q4"] = (all_town_data["2005-10"] + all_town_data["2005-11"] + all_town_data["2005-12"])/3