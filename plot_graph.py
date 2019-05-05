import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("911.csv")

print(df.info())

df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
print(df['Reason'].value_counts())

plt.ion()
plt.figure()
sns.countplot(x='Reason', data=df, palette='viridis')
plt.pause(5)

df['timeStamp'] = pd.to_datetime(df['timeStamp'])

time = df['timeStamp'].iloc[0]
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

plt.figure()
sns.countplot(x='Day of week', data=df, hue='Reason', palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.pause(5)

plt.figure()
sns.countplot(x='Month', data=df, hue='Reason', palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.pause(5)

byMonth = df.groupby('Month').count()
plt.figure()
byMonth['lat'].plot()
plt.pause(5)

sns.lmplot(x='Month', y='twp', data=byMonth.reset_index())
plt.pause(5)

df['Date'] = df['timeStamp'].apply(lambda time: time.date())
plt.figure()
df.groupby('Date').count()['lat'].plot()
plt.tight_layout()
plt.pause(5)

dayHour = df.groupby(by=['Day of week', 'Hour']).count()['Reason'].unstack()

plt.figure(figsize=(12, 6))
sns.heatmap(dayHour, cmap='viridis')
plt.pause(5)

sns.clustermap(dayHour, cmap='viridis')
plt.pause(5)

plt.close()