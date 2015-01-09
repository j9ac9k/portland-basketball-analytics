# -*- coding: utf-8 -*-
__author__ = "ogi"

import pandas as pd
import numpy as np


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


# removing entries with meaningless data
df = df[~df['Week'].str.contains('week')]

# removing pick to play games
df = df[~df['Team'].str.contains('to play')]
df = df[~df['Opponent'].str.contains('to play')]

df = df[~df['Team'].str.contains('P2P')]
df = df[~df['Opponent'].str.contains('P2P')]





#df = df[df['Week']contains(int)]


#df['Week'] = df['Week'].astype(np.int8)


#df.convert_objects(convert_dates=True, convert_numeric=True, copy=True)

#df = df                dtype={'Week': np.int8,
#                             'Diff': np.int8,
#                             'Team': object,
#                             'Opponent': object,
#                             'Pts4': np.int16,
#                             'Pts Ag': np.int16,
#                             'Time': object,
#                             'Location': str,
#                             'Season': str,
#                             'Date': np.datetime64}


#df = noNanData.str.replace('@ ', '')