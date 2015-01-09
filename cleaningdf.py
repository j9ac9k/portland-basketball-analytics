# -*- coding: utf-8 -*-
__author__ = "ogi"

import pandas as pd

df = pd.read_csv('rawPortlandBasketballData.csv',
                      header=1,
                      skip_blank_lines=True,
                      skipinitialspace=True,
                      index_col=False,
                      parse_dates=True,
                      infer_datetime_format=True,
                      keep_date_col=True,
                      low_memory=False)

df = df.dropna()
df = df.drop_duplicates()

# No need for the difference column
df = df.drop('Diff', 1)

# removing entries with meaningless data
df = df[~df['Week'].str.contains('week')]

# removing pick to play games
df = df[~df['Team'].str.contains('to play')]
df = df[~df['Opponent'].str.contains('to play')]

df = df[~df['Team'].str.contains('to Play')]
df = df[~df['Opponent'].str.contains('to Play')]

df = df[~df['Team'].str.contains('P2P')]
df = df[~df['Opponent'].str.contains('P2P')]

# removing games with no recorded score
df = df.rename(columns={'Pts 4': 'Pts4', 'Pts Ag': 'PtsAg'})
df = df[~(df.Pts4 == 0)]
df = df[~(df.PtsAg == 0)]

# removing youth games...
df = df[~df.Team.str.contains('Youth')]
df = df[~df.Opponent.str.contains('Youth')]

df = df[~df.Team.str.contains('youth')]
df = df[~df.Opponent.str.contains('youth')]

# removing no-shows...
df = df[~df.Team.str.contains('no show')]
df = df[~df.Opponent.str.contains('no show')]

# Fixing problematic dates...

wrongDate = df['Date'] == '0000-00-00'
#df[wrongDate & (df['Week'] == '2') & (df['Season'] == 'Spring 1 2014')]['Date'].replace(to_replace='0000-00-00', value='3/10/2014')



#df3/10/2014


#df.to_pickle('cleanerdf.pkl')