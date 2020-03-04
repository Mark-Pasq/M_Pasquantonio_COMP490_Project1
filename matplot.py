from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy
import pandas as pd

df = pd.read_excel(r'C:\Users\mpasq\PycharmProjects\M_Pasquantonio_COMP490_Project1\lat_long.xlsx', 'main_lat_long_locations')

fig = plt.figure(figsize=(12, 9))

m = Basemap(projection='mill',
            llcrnrlat=20,
            urcrnrlat=60,
            llcrnrlon=-130,
            urcrnrlon=-60,
            resolution='c')

m.drawcoastlines()
m.drawcountries(color='blue')
m.drawstates(color='red')
# m.drawrivers(color='blue')

m.drawmapboundary(color='pink', linewidth=10, fill_color='lightblue')

m.fillcontinents(color='lightgreen', lake_color='blue', zorder=0)

sites_lat_x = df['longitude'].tolist()
sites_lon_y = df['latitude'].tolist()

m.scatter(sites_lon_y, sites_lat_x, latlon=True, s=500, marker='*', edgecolor='k')
# m.scatter(-135, 40, latlon=True, s=250, marker='*', edgecolor='k')

plt.show()
