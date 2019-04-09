# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data.rename(index = str , columns = {'Total': 'Total_Medals'}, inplace = True)
data.head(10)
#Code starts here



# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , "Summer", "Winter")
data.loc[data['Total_Summer']==data['Total_Winter'], ['Better_Event']] = 'Both'
better_event = data['Better_Event'].value_counts().index.tolist()[0]


# --------------
#Code starts here
top_countries = data.loc[:,['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop('146', axis = 0, inplace = True)
def top_ten(df,c):
    country_list = []
    a = df.nlargest(10, c) 
    for i in a['Country_Name']:
        country_list.append(i)
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')

common = [x for x in top_10_summer if x in top_10_winter if x in top_10]


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

fig = plt.figure(figsize=(20,8))
ax1 = fig.add_subplot(131)
plt.title('Top 10 medal countries in summer')
ax2 = fig.add_subplot(132)
plt.title('Top 10 medal countries in winter')
ax3 = fig.add_subplot(133)
plt.title('Top 10 medal countries')
summer_df.plot(x = 'Country_Name', y = 'Total_Summer', kind = 'bar', ax = ax1)
winter_df.plot(x = 'Country_Name', y = 'Total_Winter', kind = 'bar', ax = ax2)
top_df.plot(x = 'Country_Name', y = 'Total_Medals', kind = 'bar', ax = ax3)
plt.show()


# --------------
#Code starts here

summer_df['Golden Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df.loc[summer_df['Golden Ratio'] == summer_df['Golden Ratio'].max()]
summer_country_gold = summer_max_ratio['Country_Name']
summer_country_gold = list(summer_country_gold)[0]
summer_max_ratio = list(summer_max_ratio['Golden Ratio'])[0]

winter_df['Golden Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df.loc[winter_df['Golden Ratio'] == winter_df['Golden Ratio'].max()]
winter_country_gold = list(winter_max_ratio['Country_Name'])[0]
winter_max_ratio = list(winter_max_ratio['Golden Ratio'])[0]

top_df['Golden Ratio'] = top_df['Gold_Total']/ top_df['Total_Medals']
top_max_ratio = top_df.loc[top_df['Golden Ratio'] == top_df['Golden Ratio'].max()]
top_country_gold = list(top_max_ratio['Country_Name'])[0]
top_max_ratio = list(top_max_ratio['Golden Ratio'])[0]


# --------------
#Code starts here
data.drop('146', inplace = True)
data_1 = data
data_1['Total_Points'] = data['Gold_Total']*3 + data['Silver_Total']*2 + data['Bronze_Total']
most_points = list(data_1.loc[data_1['Total_Points'] == data_1['Total_Points'].max()]['Total_Points'])[0]
best_country = list(data_1.loc[data_1['Total_Points'] == data_1['Total_Points'].max()]['Country_Name'])[0]


# --------------
#Code starts here
best = data.loc[data['Country_Name'] == best_country]
best = best.loc[:,['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked = True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)
plt.show()


