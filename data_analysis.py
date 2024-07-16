import csv
import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a pandas dataframe
df = pd.read_csv("Big MIR Vessels.csv", sep=',')

# Extract the 'mirDownlink' column from the dataframe
mir_downlink = df['mirDownlink']

# Create a histogram with 10 bins
plt.hist(mir_downlink, bins=5)

# Add labels and title
plt.xlabel('mirDownlink')
plt.ylabel('Frequency')
plt.title('Histogram of mirDownlink in High Plan Vessels')

# Display the histogram
plt.show()