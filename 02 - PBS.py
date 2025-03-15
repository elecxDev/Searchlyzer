#Create point based system
import pandas as pd

df = pd.read_excel('/content/dataset.xlsx')
output = '/content/Output.xlsx'

def calculate_points(row):
    points = 0

    points += row['Traffic (Monthly)'] // 1000

    if row['Bounce Rate (%)'] < 50:
        points += (50 - row['Bounce Rate (%)'])

    points += row['Avg Session Duration (min)']

    if row['Page Load Time (sec)'] < 3:
        points += (3 - row['Page Load Time (sec)'])

    if row['Mobile Friendliness Score'] > 70:
        points += (row['Mobile Friendliness Score'] - 70)

    points += row['Backlinks']

    if row['Domain Authority'] > 20:
        points += (row['Domain Authority'] - 20)

    return points

df['SEO Score'] = df.apply(calculate_points, axis=1)

df.to_excel('Output.xlsx', index=False)

df_sorted = df.sort_values(by='SEO Score', ascending=False)

df_sorted.to_excel(output, index=False)

print("Scoring and sorting completed! Check",output,"")
