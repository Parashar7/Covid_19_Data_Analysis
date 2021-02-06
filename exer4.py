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
fig, ax = plt.subplots()
rects1 = ax.bar(reduced_graph.month, reduced_graph.new_cases)
ax.set_ylabel('New Cases')
ax.set_xlabel('Month')
ax.set_title('New Cases Vs Month')
ax.set_xticks(reduced_graph.month)
ax.set_xticklabels(reduced_graph.month)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x(), height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)

plt.show()
