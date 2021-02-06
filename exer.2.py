import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ori_data = pd.read_csv('covid_data.csv')
ori_data['date'] = pd.to_datetime(ori_data.date)
ori_data['year'] = pd.DatetimeIndex(ori_data.date).year
ori_data['month'] = pd.DatetimeIndex(ori_data.date).month
ori_data['day'] = pd.DatetimeIndex(ori_data.date).day
# print(ori_data.info())

new_df = ori_data.query("iso_code==['IND']")
# print(new_df.info())

final_df = new_df[['iso_code', 'date', 'year', 'month', 'day', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths',
                   'positive_rate', 'female_smokers', 'male_smokers', 'aged_65_older', 'aged_70_older']]
print(final_df.info(), final_df.nunique(), final_df.date)
reduced_graph = final_df[['iso_code', 'new_cases', 'new_deaths', 'total_cases', 'total_deaths', 'month']]

plt.bar(reduced_graph.month, reduced_graph.new_cases)

# zip joins x and y coordinates in pairs
for x, y in zip(reduced_graph.month, reduced_graph.new_cases):
    label = "{:.2f}".format(y)

    plt.annotate(label,  # this is the text
                 (x, y),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(0, 10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center

plt.show()
