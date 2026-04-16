import pandas as pd

# Read and combine all 3 files
df0 = pd.read_csv('data/daily_sales_data_0.csv')
df1 = pd.read_csv('data/daily_sales_data_1.csv')
df2 = pd.read_csv('data/daily_sales_data_2.csv')
df = pd.concat([df0, df1, df2], ignore_index=True)

# Filter to pink morsel only
df = df[df['product'] == 'pink morsel']

# Clean price column and calculate sales
df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
df['sales'] = df['quantity'] * df['price']

# Keep only the required columns
df = df[['sales', 'date', 'region']]

# Save
df.to_csv('data/pink_morsel_sales.csv', index=False)