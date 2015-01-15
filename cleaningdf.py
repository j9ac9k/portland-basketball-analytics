# -*- coding: utf-8 -*-
__author__ = "ogi"

import pandas as pd

def findOpposite(df):
    wrongDate = df['Date'] == '0000-00-00'
    for i in range((len(df[wrongDate]))):
        relevantRow = df[wrongDate][i:i+1]
        
        #is there a date on the second listing of the game...
        matchTeam = relevantRow.Opponent.values[0]
        matchOpponent = relevantRow.Team.values[0]
        matchSeason = relevantRow.Season.values[0]
        
        try:
            replacementDate = df[df.Team.str.startswith(matchTeam) & df.Opponent.str.startswith(matchOpponent) & df.Season.str.startswith(matchSeason)].Date.values[0]
        except:
            replacementDate = '0000-00-00'
        
        if replacementDate != '0000-00-00':
            rowIndex = relevantRow.Date.index[0]
            df.loc[rowIndex, 'Date'] = replacementDate
    return df

def gameBeforeOrAfter(df):
    wrongDate = df['Date'] == '0000-00-00'
    #for i in range((len(df[wrongDate]))):
    for i in df[wrongDate].index:
        #relevantRow = df[wrongDate][i:i+1]
        #rowIndex = relevantRow.Date.index[0]
        
        matchTeam = df.Team[i]
        matchSeason = df.Season[i]
        
        weekPlusOne = str(int(df.Week[i]) + 1)
        weekMinusOne = str(int(df.Week[i]) - 1)
        
        weekAhead = df[df.Team.str.startswith(matchTeam) & df.Season.str.startswith(matchSeason) & df.Week.str.startswith(weekPlusOne)]       
        
        if int(weekMinusOne) > 0:        
            weekBehind = df[df.Team.str.startswith(matchTeam) & df.Season.str.startswith(matchSeason) & df.Week.str.startswith(weekMinusOne)] 
        else:
            weekBehind = pd.DataFrame()
        
        if not weekAhead.empty:
            #remove 7 from days and apply to date
            if int(weekAhead.Date.values[0].split('/')[1]) > 7:
                replacementDate = weekAhead.Date.values[0]                
                splitDate = replacementDate.split('/')
                splitDate[1] = str(int(splitDate[1]) - 7)
                replacementDate = str(splitDate[0] + '/' + splitDate[1] + '/' + splitDate[2])
                df.iloc[i].Date = replacementDate

        
        elif not weekBehind.empty:
            if int(weekBehind.Date.values[0].split('/')[1]) < 23:                
                replacementDate = weekBehind.Date.values[0]                
                splitDate = replacementDate.split('/')
                splitDate[1] = str(int(splitDate[1]) + 7)
                replacementDate = str(splitDate[0] + '/' + splitDate[1] + '/' + splitDate[2])
                df.iloc[i].Date = replacementDate
    
    return df
            
                        
def isDuplicate(df):
    wrongDate = df['Date'] == '0000-00-00'
    rowIndex = []
    for i in range((len(df[wrongDate]))):
        relevantRow = df[wrongDate][i:i+1]
        
        matchTeam = relevantRow.Team.values[0]
        matchTime = relevantRow.Time.values[0]
        matchSeason = relevantRow.Season.values[0]
        matchWeek = relevantRow.Week.values[0]
        
        if len(df[df.Team.str.startswith(matchTeam) &
                df.Time.str.startswith(matchTime) &
                df.Season.str.startswith(matchSeason) &
                df.Week.str.startswith(matchWeek)]) > 1:
            
            rowIndex.append(int(relevantRow.Date.index[0]))
    return rowIndex



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
#df = df.drop('Diff', 1)

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

# Resetting Index...
df = df.reset_index(drop=True)    
wrongDate = df['Date'] == '0000-00-00'
print('Starting Bad Date Entries: ' + str(len(df[wrongDate])))
# Fixing problematic dates...

# Is the entry a duplicate?
df = df.drop(df.index[isDuplicate(df)])
df = df.reset_index(drop=True)
wrongDate = df['Date'] == '0000-00-00'
print('After removing duplicate entries with 1 bad date entry: ' + str(len(df[wrongDate])))    


df['Date'] = pd.to_datetime(df['Date'])


df.to_pickle('cleanerdf.pkl')