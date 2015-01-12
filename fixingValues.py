# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 17:04:49 2015

@author: ogi
"""

import pandas as pd
import numpy as np
#import re

from collections import defaultdict

#importing the cleaner data field
df = pd.read_pickle('cleanerdf.pkl')

print("Starting Unique Teams: " + str(len(df.Team.unique())))


#Unique team Names)
df['Team'] = df['Team'].str.lower()
df['Opponent'] = df['Opponent'].str.lower()

print("After 'str.lower()' Unique Teams: " + str(len(df.Team.unique())))

teamCounter = defaultdict(int)
for team in df.Team:
    teamCounter[team] += 1
    
endConditions = (   '(thu)',
                    '(thur)',
                    '(wed)',
                    '(mon)',
                    '(tue)',
                    '(sun)',
                    '(sat)',
                    '(inter)',
                    '(wed) pd 370',
                    '(no double header wkl)',
                    '(game 3)',
                    '(game 5)',
                    '(scap)',
                    '(scappoose)',
                    '(8games)',
                    '(8 games)',
                    '(precision castparts)',
                    '(intel)',
                    '(asian)',
                    '(p2p)',
                    '(tdb)',
                    '(msft)',
                    '($60 joe)',
                    '(60 cehck)',
                    '(cash 60)',
                    '(d level one game)',
                    '(ordered jerseys)',
                    '(game 3)',
                    '($278 + release)',
                    '($142)',
                    '($346)',
                    '(release + $346)',
                    '(need 1 players)',
                    '($364+relse)',
                    '(release forms + $142)',
                    '(check-48,196,48cash)',
                    '(60 check)',
                    '(68 check)',
                    '($346+relse)',
                    '(release + $340)',
                    '($131 cash)'
                    '(purvis)',
                    '(actually cross',
                    '(rec)',
                    '(jerseys)',
                    ' no show',
                    '(wnt 2)no show. game made',
                    '( win 1)',
                    '(win 1)',
                    '(win 2)',
                    '(win2)',
                    '(wint 1)',
                    '(wint 2)',
                    '(winter 1)',
                    '(winter 2)',
                    '(d) win 2',
                    '(win 2) c',
                    '(win 2) d',
                    '(wnt 2)',
                    '(tdb)',
                    '(sum 2)',
                    '(sum 1)',
                    '(sum 2) d',
                    '(sum1)',                 
                    '(sum',
                    '(sum2 + fall )',
                    '(fall 1)',
                    '(fall 2)',
                    '(fall2)',
                    '(e fall 2)',
                    '(spr 1)',
                    '(spr 2)',
                    '(spring 2)',
                    '(spring 2 )',
                    '(spring 1)',
                    '(spring1)',
                    '(womens win 2)'
                    '#2',
                    '#1',
                    '#4',
                    '(comp)',
                    '  1)',
                    '  2)',
                    ' wed',
                    '()',
                    '(crosskix)',
                    '(spring 1) e',
                    '(win 2) e',
                    '- plus p2p',
                    '(pcc)',
                    '(gbr)',
                    '(sat) e',
                    '(x-warriors)',
                    '(need to contact sara)',
                    '( no show first game. ma)',
                    '(did shockers replace',
                    '(d fall 2)',
                    ' champ game',
                    '(sum2',
                    '(tdb',
                    '(dtb',
                    '(346',
                    ' (purvis',
                    ' sunday',
                    ' thursday',
                    ' (sum',
                    ' (release forms',
                    ')'
                )
                
middleConditions = ('no show first game',
                    "'",
                    '?',
                    '"',
                    '!',
                    ',')

replacements = (['&', ' and '],
                [' n ', ' and '],
                [' mand ', ' man '],
                [' flaky ', ' flakey '],
                ['second suns', 'second sons'],
                ['  ', ' '])

startConditions = ('b- championship ',
                   '#c4 ',
                   'c #1',
                   'c #2',
                   'c #3',
                   'c #4',
                   'c division championship game (',
                  'coed #1 ',
                  'coed #2 ',
                  'coed #3 ',
                  'coed #4 ',
                  'coed championship game (',
                   'losers of 840pm(',
                    '# ',
                    '#1 ',
                    '#2 ',
                    '#3 ',
                    '#4 ',
                    '#5 ',
                    '#6 ',
                    '#7 ',
                    '#8 ',
                    '#9 ',
                    '#10 ',
                    '#11 ',
                    '#12 ',
                    '#13 ',
                    '#14 ',
                    '#16 ',
                    '#a1 ',
                    '#a2 ',
                    '#a3 ',
                    '#a4 ',
                    '#b1 ',
                    '#b2 ',
                    '#b3 ',
                    '#b4 ',
                    '#c1 ',
                    '#c2 ',
                    '#c3 ',
                    '#c4 '
                    '#10 ',
                    '#11 ',
                    'a #1',
                    'a #2',
                    'a #3',
                    'a #4',
                    'asian league',
                    'c#3',
                    'c# 4',
                    'c#1',
                    'rec #1',
                    'rec #2',
                    'rec #3',
                    'rec #4'
                   )
                   
teamNameReplacements = np.array([
                        ['bravo insurance', 'bravo insurance agency'],
                        ['ankle breakes', 'ankle breakers'],
                        ['bad mam jamas', 'bad mama jamas'],
                        ['bad news', 'bad newz'],
                        ['band of brothers 2', 'band of brothers'],
                        ['both teams play hard', 'both teams played hard'],
                        ['talking about', 'talking bout'],
                        ['sweating out', 'sweatin out'],
                        ['super stokers', 'super strokers'],
                        ['springdale job corps', 'springdale job corp'],
                        ['springdale job corbs', 'springdale job corp'],
                        ['smokin trees and stroking 3s', 'smokn trees and stokin 3s'],
                        ['birdmandbirdman', 'birdmanbirdman'],
                        ['black rose winner', 'black rose'],
                        ['bosh. o', 'bosh.0'],
                        ['bosh.o', 'bosh.0'],
                        ['bucket r us', 'buckets r us'],
                        ['c- squad', 'c-squad'],
                        ['caribean sunset smoothies', 'caribbean sunset smoothies'],
                        ['cash money', 'ca$h money'],
                        ['ch2mhill', 'ch2m hill'],
                        ['chairmen of the boards', 'chairman of the boards'],
                        ['chatanooga flying squirles', 'chattanooga flying squirles'],
                        ['chili cheese fritos', 'chilli cheese fritos'],
                        ['chimm richalds', 'chimm richards'],
                        ['clackamas dope boys in an escalade', 'clackamas dope boyz in an escalade'],
                        ['club pdx', 'club portland'],
                        ['croations united', 'croatians united'],
                        ['drazen ballhogaviches', 'drazen ballhogavichs'],
                        ['eary birds', 'early birds'],
                        ['elite electric group', 'elite electric'],
                        ['expanison', 'expansion'],
                        ['expansion part 2', 'expansion part deux'],
                        ['f league dream team', 'f-league dream team'],
                        ['fast don', 'fast dont lie'],
                        ['fifth quarter all stars', 'fifth quarter all-stars'],
                        ['george fox international', 'george fox internationals'],
                        ['get bucket', 'get buckets'],
                        ['gumby goons', 'gumbys goons'],
                        ['h town', 'h-town'],
                        ['h1n1', 'h1 and 1'],
                        ['hai pham 62', 'hai pham'],
                        ['hai pham team', 'hai pham'],
                        ['harverys unlimited', 'harvery unlimited'],
                        ['has-beens', 'has beens'],
                        ['hdwe', 'hdwe ballaholics'],
                        ['houston comet', 'houston comets'],
                        ['j-j-j jadams', 'j-j-j-jadams'],
                        ['jail blazers', 'jailblazers'],
                        ['jenny craig save my life', 'jenny craig saved my life'],
                        ['jesse and rippers', 'jesse and the rippers'],
                        ['justic league', 'justice league'],
                        ['k nealy cash cow', 'k. nealy cash cow'],
                        ['kenny roasters', 'kennys roasters'],
                        ['kittleson  and  associates', 'kittelson  and  associates'],
                        ['knights fury indis', 'knights fury'],
                        ['land sharks (not, apparently, a late joi', 'landsharks'],
                        ['late joining team hot balls', 'hot balls'],
                        ['lawn duhs', 'lawn-duhs'],
                        ['lets 3s fly', 'let 3s fly'],
                        ['licence to lillard', 'license to lillard'],
                        ['lite em em up', 'lite em up'],
                        ['los lobos from latino league', 'los lobos'],
                        ['mac aa', 'mac aa team'],
                        ['mac a team', 'mac aa team'],
                        ['mac- and cheese', 'mac-n-cheese'],
                        ['mac and cheese', 'mac-n-cheese'],
                        ['maxim (twain-sunday team)', 'maxim'],
                        ['maxim (wed)', 'maxim'],
                        ['mba all stars', 'mba all-stars'],
                        ['mg 503', 'mg503'],
                        ['midnight monkey madeness', 'midnight monkey madness'],
                        ['midnight monkey madenew', 'midnight monkey madness'],
                        ['money badgers ($340)', 'money badgers'],
                        ['moneyshots', 'money shots'],
                        ['muck sticks', 'much sticks'],
                        ['my man (game 4)', 'my man'],
                        ['n.e.p.', 'n.e.p'],
                        ['narpro', 'narpro.com'],
                        ['narwhal', 'narwhals'],
                        ['nash potatoes', 'nash potatoes and mcgrady'],
                        ['nash potato and mcgrady', 'nash potatoes and mcgrady'],
                        ['nash potato  and  mcgrady', 'nash potatoes and mcgrady'],
                        ['nep all stars', 'nep all-stars'],
                        ['nighthawks sunday', 'nighthawks'],
                        ['no tippin pippin', 'no tippin pippen'],
                        ['nobody + p2p', 'nobody'],
                        ['noyes development co. .', 'noyes development co.'],
                        ['nw eite', 'nw elite'],
                        ['nw merck (gabes)', 'nw merck'],
                        ['old ballz(pd 480)', 'old ballz'],
                        ['pacific aircarft services', 'pacific aircraft services'],
                        ['pale blazer', 'pale blazers'],
                        ['pearl indis', 'pearl indys'],
                        ['penetrate and finish ($346 + release)', 'penetrate and finish'],
                        ['pimps  and  ballers', 'pimps and ballers'],
                        ['pimps and ballers(teamfiendship', 'pimps and ballers'],
                        ['pineryderz', 'pineriders'],
                        ['pine riders', 'pineriders'],
                        ['plan b (release forms)', 'p[an b'],
                        ['poke ballers', 'pokeballers'],
                        ['portlandbasketall.com house team', 'portland basketball hosue team'],
                        ['portlandbasketball.com house team', 'portland basketball house team'],
                        ['puke and rallies', 'puke and rally'],
                        ['purple reign', 'purple rain'],
                        ['purple ribbon allstars', 'purple ribbon all-stars'],
                        ['ram rod no show. game made, somehow. goo', 'ram rod'],
                        ['rasheeds bald spot (sum)', 'rasheeds bald spot'],
                        ['ratchets', 'racket'],
                        ['#1 bosh.o', 'bosh.0'],
                        ['2 bulldogs (no double header wk1', '2 bulldogs'],
                        ['5 - for - 5', '5-for-5'],
                        ['4 guys  and  a sub (wint 2)', '4 guys and a sub'],
                        ['54s the mike', '54s and the mike'],
                        ['a division championship game ( mastercra', 'mastercraft'],
                        ['mastercraft (sun)', 'mastercraft'],
                        ['mastercraft (wed)', 'mastercraft'],
                        ['mastercraft 1', 'mastercraft'],
                        ['mastercraft team 1', 'mastercraft'],
                        ['mastercraft team 2', 'mastercraft'],
                        ['mastercraft team a', 'mastercraft'],
                        ['mastercraft team b', 'mastercraft'],
                        ['a division championship game (log jammin', 'log jammin'],
                        ['ak 47', 'ak47'],
                        ['b division championship game ( boxers', 'boxers'],
                        ['zone thugs and harmony', 'zone thugz and harmony'],
                        ['trail-blazers', 'trail blazers'],
                        ['touch of gray', 'touch of grey'],
                        ['tnt autogroup', 'tnt auto group'],
                        ['the wolfpack', 'the wolf pack'],
                        ['the sharpshooters', 'the sharp shooters'],
                        ['the old and flakey', 'the old and flaky'],
                        ['the newborn narbarlek', 'the newborn nabarlek'],
                        ['the m series', 'the m-series'],
                        ['the alumnai', 'the alumni'],
                        ['team redickilous', 'team redickulous'],
                        ['team ca$h money', 'ca$h money'],
                        ['talkin about practice', 'talkin bout practice'],
                        ['sweating out saturday', 'sweatin out saturday'],
                        ['swag nw', 'swag northwest'],
                        ['slump bust', 'slump busters'],
                        ['shake and bake', 'shake-n-bake'],
                        ['sea ballers', 'sea-ballers'],
                        ['s.i.c', 's.i.c.'],
                        ['run  and  gun', 'run-n-gun'],
                        ['rose city tropic', 'rose city tropics'],
                        ['rodmans korean all-stars', 'rodmans korean all stars'],
                        ['robs real estate', 'robs real estate services'],
                        ['robinson', 'robinsons canby'],
                        ['rec division champioinship game (yikes', 'yikes'],
                        ['rec division champioinship game (litle g', 'little giants'],
                        ['rec championship game (perf ins', 'performance insulation'],
                        ['rec consolation game (raw dawgs', 'raw dawgs'],
                        ['ram rod no show. game made somehow. goo', 'ram rod'],
                        ['penetrate and finish ($346 + release', 'penetrate and finish'],
                        ['old ballz(pd 480', 'old ballz'],
                        ['old ballzers winner', 'old ballz'],            
                        ['nw merck (gabes', 'nw merck'],
                        ['north ballerz', 'northwest ballerz']
                        ])

teamToDelete = ('late joining team',
                'ne individuals',
                'ne indviduals',
                'p2p',
                'pick to play',
                'pick to eastside',
                'pick to play ballers',
                'pick to play beaverton',
                'pick to play eastside',
                'pick to play indis',
                'pick to play rebels',
                'pick to play vancouver',
                'pick-to-play clackamas',
                'pick-to-play indis',
                'pick-to-play vancouver',
                'pickt to play coed',
                'picktoplay ballers',
                'picktoplay beaverton',
                'picktoplay earlybirds',
                'picktoplay eastside',
                'picktoplay elite',
                'picktoplay rebels a-b',
                'rebels pick to play')

#for i in df.index:
#    teamName = df.loc[i, 'Team']    
#    if teamName in teamToDelete:
#        df = df.drop(df.index[i])
#df = df.reset_index(drop=True)      


dfOriginal = df
for i in df.index:
    
    df.Team[i] = ' '.join(df.loc[i, 'Team'].split())

    teamName = df.loc[i, 'Team']    
    for endCondition in endConditions:
        if df.Team[i].endswith(endCondition):
            df.Team[i] = teamName.replace(endCondition, '').strip()
    
    teamName = df.loc[i, 'Team']
    for startCondition in startConditions:
        if df.Team[i].startswith(startCondition):
            df.Team[i] = teamName.replace(startCondition, '').strip()

    teamName = df.loc[i, 'Team']
    for middleCondition in middleConditions:
        if middleCondition in teamName:
            df.Team[i] = teamName.replace(middleCondition, '').strip()
    
    teamName = df.loc[i, 'Team']
    for replacement in replacements:
        if replacement[0] in teamName:
            df.Team[i] = teamName.replace(replacement[0], replacement[1]).strip()
    
    teamName = df.loc[i, 'Team']                 
    if teamName in teamNameReplacements[:, 0]:
        df.Team[i] = teamNameReplacements[np.where(teamNameReplacements == teamName)[0], 1][0]
           
#    for j in df2.Team[df.Team.str.endswith(i)].index:
#        df.Team[j] = df2.Team[j].replace(i, '').rstrip()
#    for j in df2.Opponent[df.Opponent.str.endswith[i]].index:
#        df.Opponent[j] = df2.Opponent[j].replace(i, '').rstrip()
        

    
    

print("After removing days from end of team names " + str(len(df.Team.unique())))
uniqueTeams = list(df.Team.unique())

teamCounter = defaultdict(int)
for team in df.Team:
    teamCounter[team] += 1

#for i in df.index:
#    df.Team[i] = df.Team[i].rstrip('(thu)')
    
#teamCounter2 = defaultdict(int)
#for team in df.Team:
#    teamCounter2[team] += 1
#    
