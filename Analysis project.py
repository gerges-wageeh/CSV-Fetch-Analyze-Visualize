
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Download CSV file from URL
url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv'
filename = 'data.csv'
response = requests.get(url)

# Step 2: Save it locally
with open(filename, 'wb') as f:
    f.write(response.content)

# Step 3: Load data using pandas
df = pd.read_csv(filename)

# Step 4: Clean column names
df.columns = df.columns.str.strip().str.replace('"', '')

# Step 5: Show data preview and info
print("Preview of data:\n", df.head())
print("\nData info:\n")
print(df.info())
print("\nStatistical summary:\n")
print(df.describe())

# Step 6: Plot Histogram for height
if 'Height(Inches)' in df.columns:
    col_name = 'Height(Inches)'
    plt.hist(df[col_name].dropna(), bins=5, color="skyblue")
    plt.title("Distribution of Height")
    plt.xlabel("Height (Inches)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig('chart.png', bbox_inches='tight', dpi=300)
    plt.show()
else:
    print("Column 'Height(Inches)' not found.")

# Step 7: Export cleaned data to Excel
df.to_excel("cleaned_data.xlsx", index=False)
