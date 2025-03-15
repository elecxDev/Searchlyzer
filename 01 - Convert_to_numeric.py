#Convert to numeric
import pandas as pd

file_path = '/content/dataset.xlsx'
df = pd.read_excel(file_path)

def convert_to_numeric(value):
    value = str(value)
    if 'billion' in value:
        return float(value.replace(' billion', '')) * 1e9
    elif 'M' in value:
        return float(value.replace('M', '')) * 1e6
    elif 'K' in value:
        return float(value.replace('K', '')) * 1e3
    else:
        try:
            return float(value)
        except ValueError:
            return value

df['Traffic (Monthly)'] = df['Traffic (Monthly)'].apply(convert_to_numeric)
df['Backlinks'] = df['Backlinks'].apply(convert_to_numeric)
df['Social Media Shares'] = df['Social Media Shares'].apply(convert_to_numeric)

print(df)

output_file = '/content/dataset.xlsx'
df.to_excel(output_file, index=False)

print(f"Data saved to {output_file}")
