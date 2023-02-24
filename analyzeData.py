from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('./seattle-weather.csv')

weather_gb = df.groupby(['weather']).mean()
barplot = weather_gb.plot.bar(y=['temp_max','temp_min'])
barplot.set_title('Seattle Weather Data, 2012-01-01 to 2015-12-31')
plt.savefig('barplot.png')
plt.close()

x = list(df['precipitation'])
y = list(df['temp_max'])
p = np.polyfit(x,y,1)
x_line = [min(x), max(x)]
y_line = np.polyval(p,x_line)

corr = np.corrcoef(x,y)
plt.title(f'Temp_Max vs Precipitation, Pearson Corr = {corr[0,1]:.4f}')
plt.xlabel('Precipitation')
plt.ylabel('Maximum Temperature')
plt.scatter(x=df['precipitation'], y=df['temp_max'])
plt.plot(x_line,y_line,color='orange')
plt.savefig('scatterplot.png')
