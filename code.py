import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

# Perform linear regression on all data
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Create line of best fit through 2050
years_extended = range(1880, 2051)
line_fit_all_data = [slope * year + intercept for year in years_extended]
plt.plot(years_extended, line_fit_all_data, label='Line of Best Fit (All Data)')

# Perform linear regression on data from 2000 onward
recent_data = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

# Create line of best fit from 2000 onward through 2050
line_fit_recent_data = [slope_recent * year + intercept_recent for year in years_extended]
plt.plot(years_extended, line_fit_recent_data, label='Line of Best Fit (2000 Onward)')

# Set labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Add legend
plt.legend()

# Show the plot
plt.show()
