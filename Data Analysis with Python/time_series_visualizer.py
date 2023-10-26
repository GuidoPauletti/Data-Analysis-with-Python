import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
mask = (df['value'] < df['value'].quantile(0.975)) & (df['value'] > df['value'].quantile(0.025))
df = df[mask]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16,6))
    ax.plot(df, color='r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.strftime('%b') for d in df_bar.date]

    # Draw bar plot
    plt.clf()
    fig = plt.gcf()
    fig.set_size_inches(20,16)
    sns.barplot(x = 'year' , y = 'value' , data = df_bar , hue = 'month' , errorbar=None, palette = "deep")
    plt.legend(title = "Months" , labels = ['January' ,'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December'])
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Create box subplots
    plt.clf()
    fig, ax = plt.subplots(1,2)
    fig.set_size_inches(28,12)

    sns.boxplot(x='year', y='value',data=df_box, ax=ax[0]).set(title = "Year-wise Box Plot (Trend)", xlabel="Year",ylabel="Page Views")
    
    sns.boxplot(x='month', y='value',data=df_box, ax=ax[1], order=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug","Sep", "Oct", "Nov", "Dec"))
    
    plt.title("Month-wise Box Plot (Seasonality)")
    plt.xlabel("Month")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
