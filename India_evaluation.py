import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('covid_19_india.csv')
df['Date'] = pd.to_datetime(df.Date)
df['Year'] = pd.DatetimeIndex(df.Date).year
df['Month'] = pd.DatetimeIndex(df.Date).month
df['Day'] = pd.DatetimeIndex(df.Date).day
# df['Weekday'] = pd.DatetimeIndex(df.Date).week
#print(df)

new_df = df[['Date', 'Month', 'Day', 'Year', 'ConfirmedIndianNational', 'Cured', 'Deaths', 'Confirmed',
             'State/UnionTerritory']]
print(new_df)
# print(df.info())
#sns.set_style('darkgrid')
# sns.lineplot(x='Month', y='Deaths', data=new_df, palette='Purples_r')
# sns.barplot(x='Month', y='Confirmed', data=new_df, palette='Purples_r')
sns.kdeplot(data=new_df, x='Confirmed', bw_adjust=.3)

#plt.show()
