# -*- coding: utf-8 -*-
__author__ = "ogi"

import pandas as pd
#import matplotlib as mlab
import matplotlib.pyplot as plt
#from matplotlib.dates import date2num
import seaborn as sns

plt.close('all')

sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})

#importing the cleaner data field
df = pd.read_pickle('cleanerdf.pkl')


team = 'Nobody'
teamdf = df[df.Team == team]
teamdf = teamdf.set_index('Date')



#Plain Histogram
plt.figure('plainHistogram')
ax1 = plt.subplot(211, title=team + ' Points For')
plt.hist(teamdf.Pts4)

ax2 = plt.subplot(212, title=team + ' Points Against')
plt.hist(teamdf.PtsAg)


#Pandas KDE Plot
plt.figure(num='Pandas KDE Plot')
ax1 = plt.subplot(2,1,1, title=team + ' Points For Histogram')
teamdf.Pts4.plot(kind='kde', alpha=0.5)

ax2 = plt.subplot(2,1,2, title=team + ' Points Against Histogram', sharex=ax1)
teamdf.PtsAg.plot(kind='kde', alpha=0.5)
plt.show()



#Pandas Moving Average Plot
maGames = 2
maTeamPts4 = pd.rolling_mean(teamdf.Pts4, maGames)
maTeamPtsAg = pd.rolling_mean(teamdf.PtsAg, maGames)

plt.figure('MatPlotLib Moving Average')
ax1 = plt.subplot(2, 1, 1, title=("Points For "+str(maGames)+ " Game Moving Average"))
plt.plot(maTeamPts4.index, maTeamPts4)
plt.ylim(ymin=0)

ax2 = plt.subplot(2, 1, 2, title=("Points Against " +str(maGames)+ " Game Moving Average"), sharex=ax1)
plt.plot(maTeamPtsAg.index, maTeamPtsAg)
plt.ylim(ymin=0)


plt.figure('Seaborn KDE')
#sns.distplot(teamdf.Pts4, hist=False, kde_kws={"shade": True})
sns.kdeplot(teamdf.Pts4, bw=1, cut=40, shade=True, label=team)
sns.kdeplot(df.Pts4, bw=1, shade=True, label='League Overall')
#sns.kdeplot(teamdf.PtsAg, bw=1, cut=40, shade=True)



plt.figure('Rugplot')
sns.rugplot(teamdf.Pts4)





plt.show()