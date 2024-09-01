from turtle import color
from grpc import intercept_channel
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    fig = plt.figure()
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],s=8)

    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(),2051,1)
    y1 = res1.intercept + res1.slope*x1
    plt.plot(x1,y1,color='firebrick')

    df2 = df[df['Year']>=2000]
    res2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    x2 = np.arange(df2['Year'].min(),2051,1)
    y2 = res2.intercept + res2.slope*x2
    plt.plot(x2,y2,color='mediumseagreen')

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    plt.savefig('sea_level_plot.png')
    return plt.gca()