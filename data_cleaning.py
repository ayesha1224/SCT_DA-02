import pandas as pd

print("----- Data Cleaning Process Started -----")

#  Load the dataset
df = pd.read_csv("Global_Superstore2.csv",encoding='latin1')
print("\nDataset loaded successfully!")

#  Display first 5 rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Step 4: Check dataset shape
print("\nOriginal Dataset Shape (rows, columns):")
print(df.shape)

# Step 5: Check missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Step 6: Handle missing values
df = df.fillna(0)
print("\nMissing values handled!")

# Step 7: Remove duplicate rows
duplicates = df.duplicated().sum()
print("\nNumber of duplicate rows:", duplicates)

df = df.drop_duplicates()
print("Duplicates removed!")

# Step 8: Convert date columns if available
if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')

if "Ship Date" in df.columns:
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors='coerce')

print("\nDate columns converted successfully!")

# Step 9: Final dataset shape
print("\nCleaned Dataset Shape:")
print(df.shape)

# Step 10: Save cleaned dataset
df.to_csv("cleaned_superstore.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_superstore.csv'")

print("\n----- Data Cleaning Completed Successfully -----")