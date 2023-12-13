# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 23:10:22 2023

@author: Guest User
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\Guest User\Desktop\Dataset.csv'
data = pd.read_csv(file_path)

# Select data for the specific indicators and country
indicators_to_plot = [
    'Urban population growth (annual %)',
    'Population growth (annual %)',
    'CO2 emissions from gaseous fuel consumption (% of total)',
    'Electricity production from natural gas sources (% of total)',
    'Electricity production from coal sources (% of total)',
    'Forest area (% of land area)'
]
selected_country = 'China'

# Filter data
selected_data = data[(data['Country Name'] == selected_country) & (data['Indicator Name'].isin(indicators_to_plot))]

# Extract years and values for the bar chart
years = selected_data.columns[2:]
values = [selected_data[selected_data['Indicator Name'] == indicator].iloc[0, 2:].values[:len(years)] for indicator in indicators_to_plot]

# Plot the clustered column chart
plt.figure(figsize=(12, 8))
bar_width = 0.15
bar_positions = [pos - bar_width for pos in range(len(years))]

for i, indicator in enumerate(indicators_to_plot):
    plt.bar([pos + i * bar_width for pos in bar_positions], values[i], width=bar_width, label=indicator)

plt.title(f'{selected_country} - Climate Indicators (2000-2015)')
plt.xlabel('Year')
plt.ylabel('Values')
plt.xticks(range(len(years)), years)  # Set the x-axis ticks to represent years
plt.legend()
plt.grid(axis='y')
plt.show()
 
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path =r'C:\Users\Guest User\Desktop\Dataset.csv'
data = pd.read_csv(file_path)

# Select specific indicator for analysis
selected_indicator = 'CO2 emissions from gaseous fuel consumption (% of total)'

# Select the specific countries for analysis
selected_countries = ['Australia', 'Spain', 'Germany', 'China', 'Belgium', 'United States']

# Filter data for selected indicator and countries
selected_data = data[(data['Indicator Name'] == selected_indicator) & (data['Country Name'].isin(selected_countries))]

# Scatter plot for the selected indicator and countries
plt.figure(figsize=(12, 8))

for country in selected_countries:
    country_data = selected_data[selected_data['Country Name'] == country]
    
    # Check if there is data for the country before plotting
    if not country_data.empty:
        plt.scatter(country_data.columns[2:], country_data.iloc[0, 2:], label=country)

plt.xlabel('Year')
plt.ylabel(f'{selected_indicator} Value')
plt.title(f'Scatter Plot for {selected_indicator} Across Countries')
plt.legend()
plt.grid(True)
plt.show()
 

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\Guest User\Desktop\Dataset.csv'
data = pd.read_csv(file_path)

# Select specific indicators for analysis
indicators_to_analyze = ['Urban population growth (annual %)', 'Population growth (annual %)', 'CO2 emissions from gaseous fuel consumption (% of total)', 'Electricity production from natural gas sources (% of total)', 'Electricity production from coal sources (% of total)', 'Forest area (% of land area)']
# Select the specific country for analysis
selected_country = 'Australia'

# Filter data for selected indicators and country
selected_data = data[(data['Indicator Name'].isin(indicators_to_analyze)) & (data['Country Name'] == selected_country)]

# Plot time trends for the selected country and indicators
plt.figure(figsize=(16, 10))
for indicator in indicators_to_analyze:
    indicator_data = selected_data[selected_data['Indicator Name'] == indicator]
    plt.plot(indicator_data.columns[2:], indicator_data.iloc[0, 2:], label=indicator)

plt.xlabel('Year')
plt.ylabel('Value')
plt.title(f'Time Trends for {selected_country} - Selected Indicators')
plt.legend()

# The y-axis limits are determined automatically

plt.show()
 

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\Guest User\Desktop\Dataset.csv'
data = pd.read_csv(file_path)

# Select specific indicators for analysis
indicators_to_analyze = ['Urban population growth (annual %)', 'Population growth (annual %)', 'CO2 emissions from gaseous fuel consumption (% of total)', 'Electricity production from natural gas sources (% of total)', 'Electricity production from coal sources (% of total)', 'Forest area (% of land area)']
# Select the specific country for analysis
selected_country = 'Spain'

# Filter data for selected indicators and country
selected_data = data[(data['Indicator Name'].isin(indicators_to_analyze)) & (data['Country Name'] == selected_country)]

# Plot time trends for the selected country and indicators
plt.figure(figsize=(16, 10))
for indicator in indicators_to_analyze:
    indicator_data = selected_data[selected_data['Indicator Name'] == indicator]
    plt.plot(indicator_data.columns[2:], indicator_data.iloc[0, 2:], label=indicator)

plt.xlabel('Year')
plt.ylabel('Value')
plt.title(f'Time Trends for {selected_country} - Selected Indicators')
plt.legend()

# The y-axis limits are determined automatically

plt.show()
 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\Guest User\Desktop\Dataset.csv'
data = pd.read_csv(file_path)

# Select specific indicators for correlation matrix
selected_indicators = ['Urban population growth (annual %)', 'Population growth (annual %)', 'CO2 emissions from gaseous fuel consumption (% of total)', 'Electricity production from natural gas sources (% of total)', 'Electricity production from coal sources (% of total)', 'Forest area (% of land area)']

# Choose a specific country
selected_country = 'Germany'

# Filter data for selected indicators and country
selected_data = data[(data['Country Name'] == selected_country) & (data['Indicator Name'].isin(selected_indicators))]

# Extract years dynamically from the columns
years = selected_data.columns[2:]  # Assuming the years start from the 3th column

# Pivot the data
pivot_data = selected_data.melt(id_vars=['Country Name', 'Indicator Name'], value_vars=years, var_name='Year', value_name='Value')
pivot_data['Year'] = pivot_data['Year'].astype(int)  # Convert 'Year' to integer type

# Create a correlation matrix for selected indicators
correlation_matrix = pivot_data.pivot_table(index='Year', columns='Indicator Name', values='Value').corr()

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Draw the heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Set the title
plt.title(f'Correlation Matrix for {selected_country} - Selected Indicators')

# Show the plot
plt.show()
 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\Guest User\Desktop\Dataset.csv'

data = pd.read_csv(file_path)

# Select specific indicators for correlation matrix
selected_indicators = ['Urban population growth (annual %)', 'Population growth (annual %)', 'CO2 emissions from gaseous fuel consumption (% of total)', 'Electricity production from natural gas sources (% of total)', 'Electricity production from coal sources (% of total)', 'Forest area (% of land area)']

# Choose a specific country
selected_country = 'Iran, Islamic Rep.'

# Filter data for selected indicators and country
selected_data = data[(data['Country Name'] == selected_country) & (data['Indicator Name'].isin(selected_indicators))]

# Extract years dynamically from the columns
years = selected_data.columns[2:]  # Assuming the years start from the 3th column

# Pivot the data
pivot_data = selected_data.melt(id_vars=['Country Name', 'Indicator Name'], value_vars=years, var_name='Year', value_name='Value')
pivot_data['Year'] = pivot_data['Year'].astype(int)  # Convert 'Year' to integer type

# Create a correlation matrix for selected indicators
correlation_matrix = pivot_data.pivot_table(index='Year', columns='Indicator Name', values='Value').corr()

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Draw the heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Set the title
plt.title(f'Correlation Matrix for {selected_country} - Selected Indicators')

# Show the plot
plt.show()
