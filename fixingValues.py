# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 17:04:49 2015

@author: ogi
"""

import time
import pandas as pd
import numpy as np
#import re

from collections import defaultdict

#importing the cleaner data field
df = pd.read_pickle('cleanerdf.pkl')
 
removeConditions = ('\(thu\)',
                    '\(thur\)',
                    '\(wed\)',
                    '\(mon\)',
                    '\(tue\)',
                    '\(sun\)',
                    '\(sat\)',
                    '\(inter\)',
                    '\(wed\) pd 370',
                    '\(no double header wkl\)',
                    '\(game 3\)',
                    '\(game 5\)',
                    '\(scap\)',
                    '\(scappoose\)',
                    '\(8games\)',
                    '\(8 games\)',
                    '\(precision castparts\)',
                    '\(intel\)',
                    '\(asian\)',
                    '\(p2p\)',
                    '\(tdb\)',
                    '\(msft\)',
                    '\($60 joe\)',
                    '\(60 cehck\)',
                    '\(cash 60\)',
                    '\(d level one game\)',
                    '\(ordered jerseys\)',
                    '\(game 3\)',
                    '\($278 + release\)',
                    '\($142\)',
                    '\($346\)',
                    '\(release + $346\)',
                    '\(need 1 players\)',
                    '\($364+relse\)',
                    '\(release forms + $142\)',
                    '\(check-48,196,48cash\)',
                    '\(60 check\)',
                    '\(68 check\)',
                    '\($346+relse\)',
                    '\(release + $340\)',
                    '\($131 cash\)'
                    '\(purvis\)',
                    '\(actually cross',
                    '\(rec\)',
                    '\(jerseys\)',
                    ' no show',
                    '\(wnt 2\)no show. game made',
                    '\( win 1\)',
                    '\(win 1\)',
                    '\(win 2\)',
                    '\(win2\)',
                    '\(wint 1\)',
                    '\(wint 2\)',
                    '\(winter 1\)',
                    '\(winter 2\)',
                    '\(d\) win 2',
                    '\(win 2\) c',
                    '\(win 2\) d',
                    '\(wnt 2\)',
                    '\(tdb\)',
                    '\(sum 2\)',
                    '\(sum 1\)',
                    '\(sum 2\) d',
                    '\(sum1\)',                 
                    '\(sum',
                    '\(sum2 + fall \)',
                    '\(fall 1\)',
                    '\(fall 2\)',
                    '\(fall2\)',
                    '\(e fall 2\)',
                    '\(spr 1\)',
                    '\(spr 2\)',
                    '\(spring 2\)',
                    '\(spring 2 \)',
                    '\(spring 1\)',
                    '\(spring1\)',
                    '\(womens win 2\)'
                    '#2',
                    '#1',
                    '#4',
                    '\(comp\)',
                    '  1\)',
                    '  2\)',
                    ' wed',
                    '\(\)',
                    '\(crosskix\)',
                    '\(spring 1\) e',
                    '\(win 2\) e',
                    '- plus p2p',
                    '\(pcc\)',
                    '\(gbr\)',
                    '\(sat\) e',
                    '\(x-warriors\)',
                    '\(need to contact sara\)',
                    '\( no show first game. ma\)',
                    '\(did shockers replace',
                    '\(d fall 2\)',
                    ' champ game',
                    '\(sum2',
                    '\(tdb',
                    '\(dtb',
                    '\(346',
                    ' \(purvis',
                    ' sunday',
                    ' thursday',
                    ' \(sum',
                    ' \(release forms',
                    ':\)',
                    '\(no double header wk1\)',
                    '\(coed\)',
                    '\(men s\)',
                    '\(release + $364\)',
                    'b- championship ',
                   '#c4 ',
                   'c #1',
                   'c #2',
                   'c #3',
                   'c #4',
                   'c division championship game \(',
                  'coed #1 ',
                  'coed #2 ',
                  'coed #3 ',
                  'coed #4 ',
                  'coed championship game \(',
                   'losers of 840pm\(',
                    '# ',
                    '#1',
                    '#2',
                    '#3',
                    '#4',
                    '#5',
                    '#6',
                    '#7',
                    '#8',
                    '#9',
                    '#10',
                    '#11',
                    '#12',
                    '#13',
                    '#14',
                    '# 15',
                    '#16',
                    '#a1',
                    '#a2',
                    '#a3',
                    '#a4',
                    '#b1',
                    '#b2',
                    '#b3',
                    '#b4',
                    '#c1',
                    '#c2',
                    '#c3',
                    '#c4',
                    '#10',
                    '#11',
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
                    'rec #4',
                    '\(w 1\)',
                    '\(w 2\)',
                    '\(e \)')
                
middleConditions = ('no show first game',
                    "'",
                    '?',
                    '"',
                    '!',
                    ',')

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
                        ['chattanooga flying squirles', 'chattanooga flying squirrels'],
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
                        ['b division championship game ( boxers)', 'boxers'],
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
                        ['rec consolation game (raw dawgs', 'raw dawgz'],
                        ['ram rod no show. game made somehow. goo', 'ram rod'],
                        ['penetrate and finish ($346 + release', 'penetrate and finish'],
                        ['old ballz(pd 480', 'old ballz'],
                        ['old ballzers winner', 'old ballz'],            
                        ['nw merck (gabes', 'nw merck'],
                        ['north ballerz', 'northwest ballerz'],
                        ['b division championship game f(se muddogs', 'se muddogs'],
                        ['drazen ballhogovich s', 'drazen ballhogavichs'],
                        ['bunch of beaches first game. ma', 'bunch of beaches'],
                        ['bro s wit no fros', 'bros with no fros'],
                        ['bosh. o c', 'bosh.0'],
                        ['3j s & rebels', '3js & rebels'],
                        ['midnight mauranders', 'midnight mauraders'],
                        ['a division championship game (mid mauran', 'midnight mauraders'],
                        ['acumed ankle breakrs', 'acumed ankle breakers'],
                        ['advantage-ny', 'advantage ny'],
                        ['ankle breakes', 'ankle breakers'],
                        ['assist s are for quitters', 'assists are for quitters'],
                        ['b division championship game (se muddogs', 'se muddogs'],
                        ['b se muddogs', 'se muddogs'],
                        ['aztecas from latino league', 'aztecas'],
                        ['b boxers', 'boxers'],
                        ['babbitts brigade', 'babbits brigade'],
                        ['ball don t lie', 'ball dont lie'],
                        ['beaverton ballers d', 'beaverton ballers'],
                        ['bosh.o', 'bosh.0'],
                        ['both teams play hard', 'both teams played hard'],
                        ['brookyln', 'brooklyn'],
                        ['burntwood legends2)', 'burntwood legends'],
                        ['c #hashtag', '#hashtag'],
                        ['c blazers jv2', 'blazers jv2'],
                        ['c toolby', 'toolby'],
                        ['c will pay tomorrow', 'will pay tomorrow'],
                        ['c- squad', 'c-squad'],
                        ['c4 shoooters', 'c4 shooters'],
                        ['c4slump busters', 'slump busters'],
                        ['caribbean sunset smooties', 'caribbean sunset smoothies'],
                        ['a life after marriage', 'life after marriage'],
                        ['a mastercraft', 'mastercraft'],
                        ['a tune squad', 'tune squad'],
                        ['a j5', 'j5'],
                        ['a snap fitness ballers', 'snap fitness ballers'],
                        ['a lower the rim', 'lower the rim'],
                        ['22nm veritcal', '22nm vertical'],
                        ['15 dunk it  maybe', 'dunk it maybe'],
                        ['1 silverbacks', 'silverbacks'],
                        ['03 papermakers', 'papermakers'],
                        ['archers of lacrosse', 'archers of loafcrosse'],
                        ['b compview', 'compview'],
                        ['b weiler ducks', 'weiler ducks'],
                        ['ball don', 'ball dont lie'],
                        ['beavermania', 'beaver mania'],
                        ['beaverton mania', 'beaver mania'],
                        ['c4 shooters', 'shooters'],
                        ['clockstoppers', 'clock stoppers'],
                        ['coach s', 'coachs'],
                        ['cook n milkies', 'cook & milkies'],
                        ['court 4 warriors', 'warriors'],
                        ['court 5 ballers', 'ballers'],
                        ['crosskix (hai pham)', 'crosskix'],
                        ['crosskix 1', 'crosskix'],
                        ['crosskix asian', 'crosskix'],
                        ['crosskix b level', 'crosskix'],
                        ['culturual blends', 'cultural blends'],
                        ['d1 xmen', 'd1x-men'],
                        ['d1x', 'd1x-men'],
                        ['d1x men', 'd1x-men'],
                        ['dam this hurts', 'damn this hurts'],
                        ['damn this hurts flakers', 'damn this hurts'],
                        ['damn this hurts*', 'damn this hurts'],
                        ['deception', 'deceptions'],
                        ['dip city d', 'dip city'],
                        ['downntown chuckers', 'downtown chuckers'],
                        ['dragons', 'dragon'],
                        ['dream team (womens win 2)', 'dream team'],
                        ['dream killers', 'dreamkillerz'],
                        ['drinky and the bear', 'drinky and the big bear'],
                        ['drinky & the big bear','drinky and the big bear'],
                        ['duilio s cyclones', 'dulios cyclones'],
                        ['duilio s indis', 'dulios indis'],
                        ['duilio s sooners', 'dulios sooners'],
                        ['early birds', 'pick to play earlybirds'],
                        ['eggs and legs', 'eggs n legs'],
                        ['express profession services', 'express professional services'],
                        ['famous dave s', 'famous daves'],
                        ['fast don t lie', 'fast dont lie'],
                        ['freeoaders', 'freeloaders'],
                        ['future kings)', 'future kings'],
                        ['gang green (pho kings)', 'gang green'],
                        ['gary payton s other glove','gary paytons other glove'],
                        ['gerber team', 'gerber'],
                        ['gnome s a poppin', 'glones a poppin'],
                        ['halo halo comp', 'halo halo'],
                        ['hand down mand down', 'hand down man down'],
                        ['harvery unlimited', 'harvey unlimited'],
                        ['harveys unlimited', 'harvey unlimited'],
                        ['hash tag)', '#hashtag'],
                        ['(60) hatian zoe boys', 'hatian zoe boys'],
                        ['hatian zoe bous', 'hatian zoe boys'],
                        ['hoist', 'hoist it'],
                        ['hoops renegade c', 'hoops renegade'],
                        ['jalontas refs', 'jalontes refs'],
                        ['jenny craig saved my life', 'jenny craig saved our life'],
                        ['john stockton s shorts', 'john stocktons shorts'],
                        ['k. nealy cash cow', 'k. neely cash cow'],
                        ['kat squad 2 e', 'kat squad 2'],
                        ['kenny s roasters', 'kennys roasters'],
                        ['kindred spirits + $142)', 'kindled spirits'],
                        ['kittleson & associates', 'kittelson & associates'],
                        ['knight s fury', 'knights fury'],
                        ['kog s', 'kogs'],
                        ['kpb e', 'kpb'],
                        ['kpff 2 + fall )', 'kpff'],
                        ['land sharks (not apparently a late joi', 'landsharks'],
                        ['lazy t s', 'lazy ts'],
                        ['ldd ($142)', 'ldd'],
                        ['least we look cute', 'at least we look cute'],
                        ['leonardo s pizza', 'leonardos pizza'],
                        ['leonardos', 'leonardos pizza'],
                        ['leonardos pizza pd 370', 'leonardos pizza'],
                        ['let 3 s fly', 'let 3s fly'],
                        ['let s 3s fly', 'let 3s fly'],
                        ['little giants)', 'little giants'],
                        ['mac golden masters d', 'mac golden masters'],
                        ['mac n cheese', 'mac-n-cheese'],
                        ['mac- n cheese', 'mac-n-cheese'],
                        ['mba all stars)', 'mba all-stars'],
                        ['money shots', 'money shot'],
                        ['moneyshots 1', 'money shot'],
                        ['moneyshots 2', 'money shot'],
                        ['nash potato & mcgrady', 'nash potatoes and mcgrady'],
                        ['nash potatoes d', 'nash potatoes and mcgrady'],
                        ['ne indviduals', 'ne individuals'],
                        ['no limit)', 'no limit'],
                        ['northwest ballerz', 'northwest ballers'],
                        ['nw merck (gabe s)', 'nw merck'],
                        ['pacific air services', 'pacific aircraft services'],
                        ['patrick s power bottoms', 'patricks power bottoms'],
                        ['patty s towel boys', 'pattys towel boys'],
                        ['penetrate and finish', 'penetrate & finish'],
                        ['pick and roll', 'pick n roll'],
                        ['pick and rollers', 'pick n roll'],
                        ['pick-n-roll', 'pick n roll'],
                        ['pick-to-play indis', 'pick to play indis'],
                        ['pick-to-play vancouver', 'pick to play vancouver'],
                        ['pickt to play coed', 'pick to play coed'],
                        ['picktoplay ballers', 'pick to play ballers'],
                        ['picktoplay beaverton', 'pick to play beaverton'],
                        ['picktoplay earlybirds', 'pick to play earlybirds'],
                        ['picktoplay eastside', 'pick to play eastside'],
                        ['picktoplay rebels a-b', 'pick to play rebels'],
                        ['pilots (release + $346)', 'pilots'],
                        ['pimps n ballers(teamfiendship', 'pimps & ballers'],
                        ['pimps n ballers', 'pimps & ballers'],
                        ['podunk', 'podunk 2.0'],
                        ['portland basketball hosue team', 'portland basketball house team'],
                        ['rain drops', 'raindrops'],
                        ['ram jam c', 'ram jam'],
                        ['ram rod. game made somehow. goo', 'ramrod'],
                        ['ram rod', 'ramrod'],
                        ['rasheed s bald spot )', 'rasheeds bald spot'],
                        ['rasheed s bald spot', 'rasheeds bald spot'],
                        ['rb legacy tuesday', 'rb legacy'],
                        ['rb', 'rb legacy'],
                        ['rco speed wagon', 'rco speedwagon'],
                        ['re l-town regulators', 'l-town regulators'],
                        ['re let 3s fly', 'let 3s fly'],
                        ['re little giants', 'little giants'],
                        ['re performance insulation', 'performance insulation'],
                        ['re raw dawgz', 'raw dawgz'],
                        ['rebels pick to play', 'pick to play rebels'],
                        ['re run-n-gun', 'run-n-gun'],
                        ['rec championship game (perf ins)', 'performance insulation'],
                        ['rec consolation game (raw dawgs)', 'raw dawgz'],
                        ['rec consolation game( lite em up)', 'lite em up'],
                        ['rec division champioinship game (yikes )', 'yikes'],
                        ['0 the revolution', 'the revolution'],
                        ['02 ballers', 'ballers inc'],
                        ['2 bum wheels', 'bum wheels'],
                        ['3j s landscaping', '3js landscaping'],
                        ['ballers', 'ballers inc'],
                        ['brizzee bros', 'brizee bros'],
                        ['brooklynn', 'brooklyn'],
                        ['bros wit no fros', 'bros with no fros'],
                        ['can t stop our wett ball', 'cant stop our wett ball'],
                        ['fat & slow($131 cash)', 'fat & slow'],
                        ['flop city (release + $346)', 'flop city'],
                        ['its about the buckets', 'its about buckets'],
                        ['kindled spirits', 'kindred spirits'],
                        ['los lobos', 'lobos'],
                        ['nand1 all stars', 'n and 1 all stars'],
                        ['ne phat boys c', 'ne fat boyz'],
                        ['pick n roll', 'pick & roll'],
                        ['rec harvey unlimited', 'harvey unlimited'],
                        ['rec hdwe ballaholics', 'hdwe ballaholics'],
                        ['rec lite em up', 'lite em up'],
                        ['rec money right there', 'money right there'],
                        ['rec rose city rain', 'rose city rain'],
                        ['rec yikes', 'yikes'],
                        ['redlanders)', 'redlanders'],
                        ['rimcheckers )', 'rim checkers'],
                        ['rimcheckers', 'rim checkers'],
                        ['rob s real estate', 'robs real estate services'],
                        ['rob s real estate services', 'robs real estate services'],
                        ['robinson s canby', 'robinsons canby'],
                        ['rogue chap game', 'rogue'],
                        ['run & gun', 'run-n-gun'],
                        ['runnin and gunnin', 'runnin n gunnin'],
                        ['salvation army house team', 'salvation army'],
                        ['scottie dippen', 'scottie dippin'],
                        ['sharpshooters', 'sharp shooters'],
                        ['shin splints (release + $340)', 'shin splints'],
                        ['shoot em up ($346+relse)', 'shoot em up'],
                        ['shockers', 'shocker'],
                        ['sledgejammers (release + $346)', 'sledgejammers'],
                        ['slumpbusters', 'slump busters'],
                        ['spirit mountaineers ($278 + release)', 'spirit mountaineers'],
                        ['spurs 1', 'spurs'],
                        ['standard tv & apliance', 'standard tv and appliance'],
                        ['standard tv & appliance', 'standard tv and appliance'],
                        ['still hoopin it($60 joe)', 'still hoopin it'],
                        ['strokes of justice (tbd)', 'strokes of justice'],
                        ['team 2 c', 'team 2'],
                        ['team d)', 'team d'],
                        ['team degen 1', 'team degen'],
                        ['team degen 2', 'team degen'],
                        ['team roach ($346)', 'team roach'],
                        ['the 360', 'the 360s'],
                        ['the bankers)', 'the bankers'],
                        ['the bravosi and second sons', 'the bravosi second sons'],
                        ['the bravosi and second suns', 'the bravosi second sons'],
                        ['the bravosi second suns', 'the bravosi second sons'],
                        ['the clydsdales', 'the clydesdales'],
                        ['gorillas', 'the gorillas'],
                        ['the high flyers', 'high flyers'],
                        ['magic johnsons', 'the magic johnsons'],
                        ['the money badgers', 'money badgers'],
                        ['the muffin stuffers', 'muffin stuffers'],
                        ['the news team', 'news team'],
                        ['old and flaky', 'the old and flaky'],
                        ['once and future kings', 'the once and future kings'],
                        ['the op s', 'the ops'],
                        ['the outlaws', 'outlaws'],
                        ['ratchet', 'the rackets'],
                        ['the rebels', 'rebels'],
                        ['saints', 'the saints'],
                        ['sharp shooters', 'the sharp shooters'],
                        ['shocker', 'the shockers'],
                        ['the southsiders', 'southsiders'],
                        ['the squadron', 'squadron'],
                        ['tropics', 'the tropics'],
                        ['veterans', 'the veterans'],
                        ['wettersons', 'the wettersons'],
                        ['the wetterson', 'the wettersons'],
                        ['wild turkeys', 'the wild turkeys'],
                        ['the yetties', 'the yetti'],
                        ['thebankers', 'the bankers'],
                        ['there s no dui in team (money shot)', 'money shot'],
                        ['tnt auto group', 'tnt auto'],
                        ['todd s team', 'todds team'],
                        ['tracktown ballers', 'track town ballers'],
                        ['trill-blazers', 'trioll blazers'],
                        ['vick s dogg pound', 'vicks dogg pound'],
                        ['we getz buckets', 'we get buckets'],
                        ['we goin sizzler', 'we going sizzler'],
                        ['we r ..', 'we r'],
                        ['we r indis', 'we r'],
                        ['we r..', 'we r'],
                        ['westide', 'west side'],
                        ['westside', 'west side'],
                        ['westside /patricks power bottoms', 'patricks power bottoms'],
                        ['westside jaegers', 'westside jagers'],
                        ['westside shooters/patricks power bottoms', 'patricks power bottoms'],
                        ['wet j s', 'wet js'],
                        ['wildcats(need to contact annie)', 'wildcats'],
                        ['willies ballin (bomb squad)', 'bomb squad'],
                        ['willies ballin', 'bomb squad'],
                        ['wilson football coaches 1', 'wilson football coaches'],
                        ['wilson football coaches 2', 'wilson football coaches'],
                        ['winners of 840pm(filfs)', 'filfs'],
                        ['winner of log jammin', 'log jammin'],
                        ['winners of 840pm(killing time)', 'killling time'],
                        ['womens championship game (has beens)', 'has beens'],
                        ['womens championship game (too legit)', 'too legit'],
                        ['zone thugs n harmony', 'zone thugz and harmony'],
                        ['zone thugz & harmony', 'zone thugz and harmony'],
                        ['a division championship game (live after', 'life after marriage'],
                        ['richards shotgunners indis', 'richards shotgunners'],
                        ['richards shotgunners revival', 'richards shortergunners'],
                        ['rip city whole team wanted to fight game', 'rip city'],
                        ['mcbuckets get win', 'mcbuckets'],
                        ['mcelroy s team', 'mcelroys team'],
                        ['podunk ballers', 'podunk 2.0'],
                        ['the newborn nabarlek ($346 + release)', 'the newborn nabarlek'],
                        ['up town hoyas', 'uptown hoyas']
                        
                        
                        ])


Team = df.Team
Opponent = df.Opponent

def filter(Team, removeConditions, middleConditions):
    
    Team = Team.str.lower()
    
    for i in removeConditions:
        Team = Team.str.replace(i, '')
    
    for i in middleConditions:
        Team = Team.str.replace(i, ' ')
       
    
    Team = Team.str.replace('  ', ' ')
    Team = Team.str.replace('\(\)', '')
    Team = Team.str.strip()
    
    for problem_name, replacement_name in zip(teamNameReplacements[:, 0].tolist(), teamNameReplacements[:, 1].tolist()):
        Team[Team == problem_name] = replacement_name
    
    
    Team = Team.str.replace('  ', ' ')
    Team = Team.str.replace('\(\)', '')
    Team = Team.str.strip()

       
    teamCounter = defaultdict(int)
    for team in Team:
        teamCounter[team] += 1
        
    return Team


df['Team'] = filter(Team, removeConditions, middleConditions)
df['Opponent'] = filter(Opponent, removeConditions, middleConditions)


df = df[~df.Team.str.contains('grade boys')]
df = df[~df.Team.str.contains('grade girls')]
df = df[~df.Team.str.contains('connor s team')]
df = df[~df.Team.str.contains('scott murphy')]
df = df[~df.Team.str.contains('es goons')]
df = df[~df.Opponent.str.contains('sccs finest')]
df = df[~df.Opponent.str.contains('team wilson')]
df = df[~df.Opponent.str.contains('valley athletics')]


uniqueTeams = sorted(df.Team.unique())

teamCounter = defaultdict(int)
for team in df.Team:
    teamCounter[team] += 1
    
uniqueOpponents = sorted(df.Opponent.unique())

opponentCounter = defaultdict(int)
for opponent in df.Opponent:
    opponentCounter[opponent] += 1
    


df.to_pickle('cleaner2df.pkl')