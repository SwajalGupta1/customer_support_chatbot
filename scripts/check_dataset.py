import pandas as pd
df=pd.read_csv('data/flipkart_faq.csv')
print(df.head())
print(f"Initial dataset size: {len(df)}")
print(f"Columns: {df.columns.tolist()}")
print("="*50)
duplicates=df["question"].duplicated().sum()
print(f"Number of duplicate questions: {duplicates}")

if(duplicates>0):
    df=df.drop_duplicates(subset=["question"])
    print(f"Removed {duplicates} duplicate questions.")

print(df["category"].unique())
