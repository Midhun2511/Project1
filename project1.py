import pandas as pd

# Load dataset
df = pd.read_excel("data\\Dataset for Data Analytics.xlsx")

# 1. Check missing values
print(df.isnull().sum())

# 2. Handle missing values
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')

# 3. Remove duplicates
df = df.drop_duplicates()

# 4. Correct data formats
df['Date'] = pd.to_datetime(df['Date'])

df['Quantity'] = df['Quantity'].astype(int)
df['ItemsInCart'] = df['ItemsInCart'].astype(int)

df['UnitPrice'] = df['UnitPrice'].astype(float)
df['TotalPrice'] = df['TotalPrice'].astype(float)

# 5. Standardize text formatting
text_columns = [
    'Product',
    'PaymentMethod',
    'OrderStatus',
    'ReferralSource'
]

for col in text_columns:
    df[col] = df[col].str.strip().str.title()

# Final check
print(df.info())
print(df.isnull().sum())

# Save cleaned dataset
df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("Data cleaning completed!")