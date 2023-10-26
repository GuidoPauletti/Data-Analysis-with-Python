import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", index_col='Year')  

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df.index, df['CSIRO Adjusted Sea Level'], color='blue', label='Sea Level Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df.index, df['CSIRO Adjusted Sea Level'])
    line_x = np.array([min(df.index), max(df.index), 2050])  # Including year 2050
    line_y = slope * line_x + intercept
    plt.plot(line_x, line_y, color='yellow', label='Line of Best Fit')

    # Create second line of best fit
    df_recent = df[df.index >= 2000]
    recent_slope, recent_intercept, recent_r_value, recent_p_value, recent_std_err = linregress(df_recent.index, df_recent['CSIRO Adjusted Sea Level'])
    recent_line_x = np.array([2000, max(df.index), 2050])  # Including year 2050
    recent_line_y = recent_slope * recent_line_x + recent_intercept
    plt.plot(recent_line_x, recent_line_y, color='red', label='Line of Best Fit, Recent Years')
  
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level')
    plt.title('Sea Level Rise and Prediction')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()