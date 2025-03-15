#Data visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Site': ['Google Search', 'YouTube', 'Facebook', 'Twitter', 'Instagram',
             'Baidu', 'Wikipedia', 'Yandex', 'Yahoo', 'WhatsApp',
             'Amazon', 'Yahoo JP', 'Live', 'Netflix', 'Reddit',
             'TikTok', 'Docomo', 'LinkedIn', 'Office', 'Samsung'],
    'Traffic (Monthly)': [92000000000, 34000000000, 25000000000, 6000000000,
                          6000000000, 7000000000, 4000000000, 2000000000,
                          3000000000, 5000000000, 15000000000, 2500000000,
                          1000000000, 10000000000, 4000000000, 8000000000,
                          800000000, 1500000000, 900000000, 3000000000],
    'Bounce Rate (%)': [28, 50, 42, 40, 45, 30, 55, 38, 40, 25,
                        35, 45, 60, 55, 50, 48, 50, 40, 35, 45],
    'Avg Session Duration (min)': [11, 20, 15, 10, 8, 12, 5, 9,
                                   10, 7, 18, 7, 4, 4.1, 12, 11,
                                   4, 10, 6, 8],
    'Page Load Time (sec)': [2.1, 3.5, 4, 4.2, 4, 3.1, 2.8, 4.5,
                              3.8, 2.9, 3.2, 3, 3.5, 2.5, 4,
                              4.3, 3.5, 3.8, 3.9, 4.1],
    'Backlinks': [5000000, 4500000, 3200000, 2000000, 2300000, 1800000,
                  5500000, 1200000, 1500000, 2000000, 2700000, 1300000,
                  1000000, 3500000, 2000000, 2500000, 700000, 2000000,
                  1500000, 2000000],
}

df = pd.DataFrame(data)

df['Domain Authority'] = [100, 90, 80, 70, 75, 65, 85, 90, 95, 80,
                           70, 65, 60, 50, 55, 45, 40, 35, 30, 25]

df['Conversion Rate (%)'] = [1, 2, 1.5, 2.5, 3, 1, 1.8, 2,
                             2.2, 3, 3.5, 2.1, 1.3, 2.8,
                             2, 2.4, 1.1, 1.5, 2.6, 2.9]

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Traffic (Monthly)', y='Bounce Rate (%)')
plt.title('Traffic vs. Bounce Rate')
plt.xlabel('Monthly Traffic')
plt.ylabel('Bounce Rate (%)')
plt.xscale('log')
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Page Load Time (sec)', y='Avg Session Duration (min)')
plt.title('Avg Session Duration vs. Page Load Time')
plt.xlabel('Page Load Time (seconds)')
plt.ylabel('Avg Session Duration (minutes)')
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, y='Bounce Rate (%)')
plt.title('Bounce Rate Distribution')
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Backlinks', y='Domain Authority')
plt.title('Backlinks vs. Domain Authority')
plt.xlabel('Backlinks')
plt.ylabel('Domain Authority')
plt.xscale('log')
plt.grid()
plt.show()

plt.figure(figsize=(12, 8))
conversion_rate_data = df.groupby('Site').mean()['Conversion Rate (%)'].reset_index()
sns.barplot(data=conversion_rate_data, x='Site', y='Conversion Rate (%)')
plt.title('Average Conversion Rate by Site')
plt.xticks(rotation=45)
plt.grid()
plt.show()
