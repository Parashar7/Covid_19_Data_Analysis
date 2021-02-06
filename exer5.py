import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = sns.load_dataset('tips')
print(df)
fig, ax = plt.subplots()
rects1 = ax.bar(df.total_bill, df.tip)
#ax.set_ylabel('Tip')
#ax.set_xlabel('Total Bill')
ax.set_title('Total Bill Vs Tip')
ax.set_xticks(df.total_bill)
ax.set_xticklabels(df.total_bill)
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
