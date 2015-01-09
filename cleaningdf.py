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
            replacementDate = df[df.Team.str.contains(matchTeam) & df.Opponent.str.contains(matchOpponent) & df.Season.str.contains(matchSeason)].Date.values[0]
        except:
            replacementDate = '0000-00-00'
        
        if replacementDate != '0000-00-00':
            rowIndex = relevantRow.Date.index[0]
            df.loc[rowIndex, 'Date'] = replacementDate
    return df

def gameBefore(df):
    wrongDate = df['Date'] == '0000-00-00'
    for i in range((len(df[wrongDate]))):
        relevantRow = df[wrongDate][i:i+1]
        
        
        if int(df[wrongDate][i,i+1].Week.values[0] > 1):
            matchTeam = relevantRow.Team.values[0]
            matchSeason = relevantRow.Season.values[0]
    
    return df
            
                        
def isDuplicate(df):
    wrongDate = df['Date'] == '0000-00-00'
    rowIndex = []
    for i in range((len(df[wrongDate]))):
        relevantRow = df[wrongDate][i:i+1]
        
        matchTeam = relevantRow.Team.values[0]
        matchOpponent = relevantRow.Opponent.values[0]
        matchSeason = relevantRow.Season.values[0]
        matchWeek = relevantRow.Week.values[0]
        
        if len(df[df.Team.str.contains(matchTeam) &
                df.Opponent.str.contains(matchOpponent) &
                df.Season.str.contains(matchSeason) &
                df.Week.str.contains(matchWeek)]) > 1:
            
            rowIndex.append(relevantRow.Date.index[0])
    return rowIndex


def main():
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
    
        
    wrongDate = df['Date'] == '0000-00-00'
    print('Bad Date Entries: ' + str(len(df[wrongDate])))
    # Fixing problematic dates...

    duplicateEntries = isDuplicate(df)
    df = df.drop(df.index[duplicateEntries])
    
    wrongDate = df['Date'] == '0000-00-00'
    print('Bad Date Entries: ' + str(len(df[wrongDate])))    
    
    #df = findOpposite(df)
    
main()
