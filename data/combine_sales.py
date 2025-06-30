import pandas as pd
import os

files = ["daily_sales_data_0.csv",
         "daily_sales_data_1.csv",
         "daily_sales_data_2.csv"
         ]

all_data = []

for file in files:
    print(f"Reading file: {file}")
    df = pd.read_csv(file)
    df = df[ df['product'] == 'pink morsel']
    df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
    df['quantity'] = df['quantity'].astype(int)
    df['sales'] = df['quantity'] * df['price']
    df = df[['sales', 'date', 'region']]
    all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)
combined_df.to_csv("combined_sales_data.csv", index=False)

print("Combined sales data saved to 'combined_sales_data.csv'")
