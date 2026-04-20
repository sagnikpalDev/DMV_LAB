
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

df = pd.read_csv("D:\companydataset.csv")  
print(df.head())
df.columns = df.columns.str.strip()

df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce')

df['review_count'] = df['review_count'].str.replace('[^0-9.]', '', regex=True)
df['review_count'] = pd.to_numeric(df['review_count'], errors='coerce') * 1000

df['years'] = df['years'].str.extract('(\d+)')
df['years'] = pd.to_numeric(df['years'], errors='coerce')

import re
import numpy as np

def convert_employees(val):
    if pd.isna(val):
        return np.nan
    
    val = str(val).lower()
    
    try:
        if '-' in val:
            parts = val.split('-')
            
            def parse_part(p):
                if 'lakh' in p:
                    num = float(re.findall(r'\d+\.?\d*', p)[0])
                    return num * 100000
                elif 'k' in p:
                    num = float(re.findall(r'\d+\.?\d*', p)[0])
                    return num * 1000
                return np.nan
            
            low = parse_part(parts[0])
            high = parse_part(parts[1])
            
            return (low + high) / 2  # take average
        
        # Case 2: "1 Lakh+"
        elif 'lakh' in val:
            num = float(re.findall(r'\d+\.?\d*', val)[0])
            return num * 100000
        
        # Case 3: "50k"
        elif 'k' in val:
            num = float(re.findall(r'\d+\.?\d*', val)[0])
            return num * 1000
        
        else:
            return np.nan
    
    except:
        return np.nan

df['employees'] = df['employees'].apply(convert_employees)

print(df[['name','employees']].head(10))
df = df.dropna(subset=['employees'])

df = df.dropna(subset=['ratings','review_count','years','employees'])


plt.figure(figsize=(8,8))
plt.pie(df['employees'], labels=df['name'], autopct='%1.1f%%')
plt.title("Employee Distribution by Company")
plt.show()

plt.figure(figsize=(10,8))
plt.barh(df['name'], df['review_count'])
plt.title("Company Reviews (Funnel Alternative)")
plt.xlabel("Reviews")
plt.ylabel("Company")
plt.show()

print("\nTop 10 Company Headquarters:\n")
print(df[['name','hq']].head(10))

plt.figure(figsize=(12,6))
sns.barplot(x='name', y='ratings', data=df)
plt.xticks(rotation=60)
plt.title("Company Ratings")
plt.show()

plt.figure(figsize=(12,6))
plt.plot(df['name'], df['years'], marker='o')
plt.xticks(rotation=60)
plt.title("Company Age (Years)")
plt.xlabel("Company")
plt.ylabel("Years")
plt.show()