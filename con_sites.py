# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 10:09:18 2017

@author: MGuidry
"""

import urllib2
from bs4 import BeautifulSoup
import csv

sites=['allenbwest.com',
       'americanthinker.com',
       'bizpacreview.com',
       'breitbart.com',
       'chicksontheright.com',
       'conservativepost.com',
       'conservativereview.com',
       'conservativetribune.com',
       'dailycaller.com',
       'dailywire.com',
       'drudgereport.com',
       'foxnews.com',
       'freebeacon.com',
       'freedomdaily.com',
       'freerepublic.com',
       'frontpagemag.com',
       'hotair.com',
       'ijr.com',
       'infowars.com',
       'legalinsurrection.com',
       'lifezette.com',
       'louderwithcrowder.com',
       'lucianne.com',
       'mu.nu',
       'nationalreview.com',
       'newsbusters.org',
       'newsmax.com',
       'observer.com',
       'pjmedia.com',
       'powerlineblog.com',
       'redstate.com',
       'rightwingnews.com',
       'rushlimbaugh.com',
       'spectator.org',
       'theamericanconservative.com',
       'theblaze.com',
       'thefederalist.com',
       'thegatewaypundit.com',
       'therightscoop.com',
       'townhall.com',
       'truthrevolt.org',
       'twitchy.com',
       'washingtonexaminer.com',
       'washingtontimes.com',
       'weaselzippers.us',
       'weeklystandard.com',
       'westernjournalism.com',
       'wnd.com',
       'youngcons.com']
       
ranking_dict=dict()     
     
for site in sites:
    url='http://www.alexa.com/siteinfo/'+site
    req=urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    pageFile = urllib2.urlopen(req)
    html = pageFile.read()
    soup=BeautifulSoup(html)
    trs=soup.findAll('tr')
    rank_hit=False
    for tr in trs:
        tds=tr.findAll('td')
        for td in tds:
            a=td.findAll('a')
            if(any(['/topsites/countries/US' in aa['href'] for aa in a])):
                rank_hit=True
        if(rank_hit):
            ranking=tds[2].getText()
            rank_hit=False
    # print site, ranking
    ranking_int=int(ranking.replace(',',''))
    ranking_dict[site]=ranking_int
print 'Alexa Rank','Site'
print '(in US)'
for key in sorted(ranking_dict,key=ranking_dict.get):
    print '%5d' % ranking_dict[key],key

with open('con_sites.csv','wb') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['Alexa Rank (in US)','Site'])
    for key in sorted(ranking_dict,key=ranking_dict.get):
        writer.writerow([ranking_dict[key],key])
