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

all_town_data["2006q1"] = (all_town_data["2006-01"] + all_town_data["2006-02"] + all_town_data["2006-03"])/3
all_town_data["2006q2"] = (all_town_data["2006-04"] + all_town_data["2006-05"] + all_town_data["2006-06"])/3
all_town_data["2006q3"] = (all_town_data["2006-07"] + all_town_data["2006-08"] + all_town_data["2006-09"])/3
all_town_data["2006q4"] = (all_town_data["2006-10"] + all_town_data["2006-11"] + all_town_data["2006-12"])/3

all_town_data["2007q1"] = (all_town_data["2007-01"] + all_town_data["2007-02"] + all_town_data["2007-03"])/3
all_town_data["2007q2"] = (all_town_data["2007-04"] + all_town_data["2007-05"] + all_town_data["2007-06"])/3
all_town_data["2007q3"] = (all_town_data["2007-07"] + all_town_data["2007-08"] + all_town_data["2007-09"])/3
all_town_data["2007q4"] = (all_town_data["2007-10"] + all_town_data["2007-11"] + all_town_data["2007-12"])/3

all_town_data["2008q1"] = (all_town_data["2008-01"] + all_town_data["2008-02"] + all_town_data["2008-03"])/3
all_town_data["2008q2"] = (all_town_data["2008-04"] + all_town_data["2008-05"] + all_town_data["2008-06"])/3
all_town_data["2008q3"] = (all_town_data["2008-07"] + all_town_data["2008-08"] + all_town_data["2008-09"])/3
all_town_data["2008q4"] = (all_town_data["2008-10"] + all_town_data["2008-11"] + all_town_data["2008-12"])/3

all_town_data["2009q1"] = (all_town_data["2009-01"] + all_town_data["2009-02"] + all_town_data["2009-03"])/3
all_town_data["2009q2"] = (all_town_data["2009-04"] + all_town_data["2009-05"] + all_town_data["2009-06"])/3
all_town_data["2009q3"] = (all_town_data["2009-07"] + all_town_data["2009-08"] + all_town_data["2009-09"])/3
all_town_data["2009q4"] = (all_town_data["2009-10"] + all_town_data["2009-11"] + all_town_data["2009-12"])/3

all_town_data["2010q1"] = (all_town_data["2010-01"] + all_town_data["2010-02"] + all_town_data["2010-03"])/3
all_town_data["2010q2"] = (all_town_data["2010-04"] + all_town_data["2010-05"] + all_town_data["2010-06"])/3
all_town_data["2010q3"] = (all_town_data["2010-07"] + all_town_data["2010-08"] + all_town_data["2010-09"])/3
all_town_data["2010q4"] = (all_town_data["2010-10"] + all_town_data["2010-11"] + all_town_data["2010-12"])/3

all_town_data["2011q1"] = (all_town_data["2011-01"] + all_town_data["2011-02"] + all_town_data["2011-03"])/3
all_town_data["2011q2"] = (all_town_data["2011-04"] + all_town_data["2011-05"] + all_town_data["2011-06"])/3
all_town_data["2011q3"] = (all_town_data["2011-07"] + all_town_data["2011-08"] + all_town_data["2011-09"])/3
all_town_data["2011q4"] = (all_town_data["2011-10"] + all_town_data["2011-11"] + all_town_data["2011-12"])/3

all_town_data["2012q1"] = (all_town_data["2012-01"] + all_town_data["2012-02"] + all_town_data["2012-03"])/3
all_town_data["2012q2"] = (all_town_data["2012-04"] + all_town_data["2012-05"] + all_town_data["2012-06"])/3
all_town_data["2012q3"] = (all_town_data["2012-07"] + all_town_data["2012-08"] + all_town_data["2012-09"])/3
all_town_data["2012q4"] = (all_town_data["2012-10"] + all_town_data["2012-11"] + all_town_data["2012-12"])/3

all_town_data["2013q1"] = (all_town_data["2013-01"] + all_town_data["2013-02"] + all_town_data["2013-03"])/3
all_town_data["2013q2"] = (all_town_data["2013-04"] + all_town_data["2013-05"] + all_town_data["2013-06"])/3
all_town_data["2013q3"] = (all_town_data["2013-07"] + all_town_data["2013-08"] + all_town_data["2013-09"])/3
all_town_data["2013q4"] = (all_town_data["2013-10"] + all_town_data["2013-11"] + all_town_data["2013-12"])/3

all_town_data["2014q1"] = (all_town_data["2014-01"] + all_town_data["2014-02"] + all_town_data["2014-03"])/3
all_town_data["2014q2"] = (all_town_data["2014-04"] + all_town_data["2014-05"] + all_town_data["2014-06"])/3
all_town_data["2014q3"] = (all_town_data["2014-07"] + all_town_data["2014-08"] + all_town_data["2014-09"])/3
all_town_data["2014q4"] = (all_town_data["2014-10"] + all_town_data["2014-11"] + all_town_data["2014-12"])/3

all_town_data["2015q1"] = (all_town_data["2015-01"] + all_town_data["2015-02"] + all_town_data["2015-03"])/3
all_town_data["2015q2"] = (all_town_data["2015-04"] + all_town_data["2015-05"] + all_town_data["2015-06"])/3
all_town_data["2015q3"] = (all_town_data["2015-07"] + all_town_data["2015-08"] + all_town_data["2015-09"])/3
all_town_data["2015q4"] = (all_town_data["2015-10"] + all_town_data["2015-11"] + all_town_data["2015-12"])/3

all_town_data["2016q1"] = (all_town_data["2016-01"] + all_town_data["2016-02"] + all_town_data["2016-03"])/3
all_town_data["2016q2"] = (all_town_data["2016-04"] + all_town_data["2016-05"] + all_town_data["2016-06"])/3
all_town_data["2016q3"] = (all_town_data["2016-07"] + all_town_data["2016-08"])/2
