# -*- coding: utf-8 -*-
__author__ = "ogi"

import pandas as pd
import matplotlib as mlab
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import seaborn as sns

plt.close('all')

sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})

#importing the cleaner data field
df = pd.read_pickle('cleanerdf.pkl')


team = 'Rogue'
teamdf = df[df.Team == team]
teamdf = teamdf.set_index('Date')

fig1 = plt.figure()
ax1 = plt.subplot(2,1,1, title=team + ' Points For Histogram')
teamdf.Pts4.plot(kind='hist', alpha=0.5, normed=True)

ax2 = plt.subplot(2,1,2, title=team + ' Points Against Histogram', sharex=ax1)
teamdf.PtsAg.plot(kind='hist', alpha=0.5, normed=True)
plt.show()











#terminators = df[df.Team == 'Terminators']
#terminators['Date'] = pd.to_datetime(terminators['Date'])
#terminators = terminators.set_index('Date')
#
#daBears = df[df.Team == 'Da Bears']
#daBears['Date'] = pd.to_datetime(daBears['Date'])
#daBears = daBears.set_index('Date')
#
#
#
#fig1 = plt.figure()
#ax1 = plt.subplot(2,1,1, title="Terminators Points For Histogram")
#terminators.Pts4.plot(kind='hist', alpha=0.5, normed=True)
#daBears.Pts4.plot(kind='hist', alpha=0.5, normed=True)
#plt.legend(['Termiators', 'Da Bears'])
#
#
#ax2 = plt.subplot(2,1,2, sharex=ax1, title="Terminators Points Against Histogram")
#terminators.PtsAg.plot(kind='hist', alpha=0.5, normed=True)
#daBears.PtsAg.plot(kind='hist', alpha=0.5, normed=True)
#plt.legend(['Termiators', 'Da Bears'])
#plt.show()
#
#
#
#maGames = 3
#maTerminatorsPts4 = pd.rolling_mean(terminators.Pts4, maGames)
#maDaBearsPts4 = pd.rolling_mean(daBears.Pts4, maGames)
#
#maTerminatorsPtsAg = pd.rolling_mean(terminators.PtsAg, maGames)
#maDaBearsPtsAg = pd.rolling_mean(daBears.PtsAg, maGames)
#
#
#
#fig2 = plt.figure()
#
#ax1 = plt.subplot(2, 1, 1, title="Points For 3-Game Moving Average")
#plt.plot(maTerminatorsPts4.index, maTerminatorsPts4)
#plt.plot(maDaBearsPts4.index, maDaBearsPts4)
#plt.legend(['Terminators', 'Da Bears'])
#plt.ylim(ymin=0)
#
#ax2 = plt.subplot(2, 1, 2, title="Points Against 3-Game Moving Average")
#plt.plot(maTerminatorsPtsAg.index, maTerminatorsPtsAg)
#plt.plot(maDaBearsPtsAg.index, maDaBearsPtsAg)
#plt.legend(['Terminators', 'Da Bears'])
#plt.ylim(ymin=0)
#plt.show()