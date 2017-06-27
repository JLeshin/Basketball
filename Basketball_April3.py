

#We first we scrape the data from espn.com and nba.com that we will use in our simulation. We create 4 dataframes that 
#will contain our source vectors of data. We use different methods for espn.com and nba.com because of the 
#different formats of source code for each site.

    
import requests
import pandas as pd
from numpy import *

url = "http://stats.nba.com/league/team/#!/advanced/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'}

with requests.Session() as session:
    session.headers = headers
    session.get(url, headers=headers)

    params = {
        'DateFrom': '',
        'DateTo': '',
        'GameScope': '',
        'GameSegment': '',
        'LastNGames': '0',
        'LeagueID': '00',
        'Location': '',
        'MeasureType': 'Advanced',
        'Month': '0',
        'OpponentTeamID': '0',
        'Outcome': '',
        'PaceAdjust': 'N',
        'PerMode': 'Totals',
        'Period': '0',
        'PlayerExperience': '',
        'PlayerPosition': '',
        'PlusMinus': 'N',
        'Rank': 'N',
        'Season': '2014-15',
        'SeasonSegment': '',
        'SeasonType': 'Regular Season',
        'StarterBench': '',
        'VsConference': '',
        'VsDivision': ''
    }

    response = session.get('http://stats.nba.com/stats/leaguedashteamstats', params=params)
    
results = response.json()
headers = results['resultSets'][0]['headers']
rows = results['resultSets'][0]['rowSet']
dataNBAadv=pd.DataFrame(rows)

    

url = "http://stats.nba.com/league/team/#!/misc/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'}

with requests.Session() as session:
    session.headers = headers
    session.get(url, headers=headers)

    params = {
        'DateFrom': '',
        'DateTo': '',
        'GameScope': '',
        'GameSegment': '',
        'LastNGames': '0',
        'LeagueID': '00',
        'Location': '',
        'MeasureType': 'Misc',
        'Month': '0',
        'OpponentTeamID': '0',
        'Outcome': '',
        'PaceAdjust': 'N',
        'PerMode': 'Totals',
        'Period': '0',
        'PlayerExperience': '',
        'PlayerPosition': '',
        'PlusMinus': 'N',
        'Rank': 'N',
        'Season': '2014-15',
        'SeasonSegment': '',
        'SeasonType': 'Regular Season',
        'StarterBench': '',
        'VsConference': '',
        'VsDivision': ''
    }

    response = session.get('http://stats.nba.com/stats/leaguedashteamstats', params=params)
    results = response.json()
    headers = results['resultSets'][0]['headers']
    rows = results['resultSets'][0]['rowSet']

    
    dataNBAmisc=pd.DataFrame(rows)



from bs4 import BeautifulSoup 


url="http://espn.go.com/nba/statistics/team/_/stat/team-comparison-per-game"
r=requests.get(url)
soup=BeautifulSoup(r.content)



Rows=[]
   

tds=soup.find_all("td")
for i in range(0,11):
    Rows.append([])
    for x in tds[7+15*i:7+15*(i+1)]:
        Rows[i].append(x.text)

for i in range(11,21):
    Rows.append([])
    for x in tds[194+15*(i-11):194+15*(i-10)]:
        Rows[i].append(x.text)
        
        
for i in range(21,31):
    Rows.append([])
    for x in tds[366+15*(i-21):366+15*(i-20)]:
        Rows[i].append(x.text)

#print Rows

data1=pd.DataFrame(Rows)
data1.columns=[data1.loc[0].values]



url="http://espn.go.com/nba/statistics/team/_/stat/offense-per-game"
r=requests.get(url)
soup2=BeautifulSoup(r.content)


Offense=[]
   

tds=soup2.find_all("td")
for i in range(0,11):
    Offense.append([])
    for x in tds[14*i:14*(i+1)]:
        Offense[i].append(x.text)

for i in range(11,21):
    Offense.append([])
    for x in tds[168+14*(i-11):168+14*(i-10)]:
        Offense[i].append(x.text)
        
        
for i in range(21,31):
    Offense.append([])
    for x in tds[322+14*(i-21):322+14*(i-20)]:
        Offense[i].append(x.text)



data2=pd.DataFrame(Offense)
data2.columns=[data2.loc[0].values]



url="http://espn.go.com/nba/statistics/team/_/stat/defense-per-game"
r=requests.get(url)
soup3=BeautifulSoup(r.content)

  
Defense=[]
   

tds=soup3.find_all("td")
for i in range(0,11):
    Defense.append([])
    for x in tds[14*i:14*(i+1)]:
        Defense[i].append(x.text)

for i in range(11,21):
    Defense.append([])
    for x in tds[168+14*(i-11):168+14*(i-10)]:
        Defense[i].append(x.text)
        
        
for i in range(21,31):
    Defense.append([])
    for x in tds[322+14*(i-21):322+14*(i-20)]:
        Defense[i].append(x.text)



data3=pd.DataFrame(Defense)
data3.columns=[data3.loc[0].values]



url="http://espn.go.com/nba/statistics/team/_/stat/miscellaneous-per-game"
r=requests.get(url)
soup4=BeautifulSoup(r.content)

  
Misc=[]
   

tds=soup4.find_all("td")
for i in range(0,11):
    Misc.append([])
    for x in tds[6+13*i:6+13*(i+1)]:
        Misc[i].append(x.text)

for i in range(11,21):
    Misc.append([])
    for x in tds[168+13*(i-11):168+13*(i-10)]:
        Misc[i].append(x.text)
        
        
for i in range(21,31):
    Misc.append([])
    for x in tds[317+13*(i-21):317+13*(i-20)]:
        Misc[i].append(x.text)



data4=pd.DataFrame(Misc)

#We next scrape betting data from bovada.lv . We put this data into a table called "Gamble" that will have three columns (actually
#"Gamble" itself has 3 rows; we will take its transpose to get something with 3 columns).
#The first column consists of matchups (pairs of team names separated by an empty line). The second column consists of the line
#for each game (and perhaps also the vig if it's not -110 each). The third column consists of over unders (and again perhaps
#also the vig). 

url="http://sports.bovada.lv/sports-betting/nba-basketball-lines.jsp"
r=requests.get(url)
soup=BeautifulSoup(r.content)

g_data=soup.find_all("div", {"class":"competitor-name"})
X=[]
for item in g_data:
    X.append(item.text)
for x in X:
    if x=="Competitor":
        X.remove(x)
for i in range(len(X)):
    if "Clippers" in X[i]:
        X[i]="Clippers"
for i in range(len(X)):
    if "Lakers" in X[i]:
        X[i]="Lakers"
 

#if x=="line-normal" or x=="line-restricted":

g_data=soup.find_all(True, {'class':['line-restricted','line-normal']})
Y=[]
for item in g_data:
        Y.append(item.text)

        
g_data=soup.find_all(True, {'class':['total-number','total-empty']})
Z=[]
for item in g_data:
    Z.append(item.text)
W=[]
s=0
for i in range(len(Z)):
    W.append([])
    if Z[i]=="-":
        W[i+s]="-"

    if Z[i]!="-":
        W.append([])
        W[i+s]=Z[i]
        W[i+s+1]=Z[i]
        s=s+1

Gamble=[X,Y,W]
#We turn it into a Pandas dataframe:
G=pd.DataFrame(Gamble)



#WebSim takes two NBA teams as inputs and simulates a game between the two, returning three outputs: Team 1's score, Teams 2's 
#score, and the total number of possessions in the simulated game. 

def WebSim(Team1, Team2):    

    #The aforementioned "source" vectors of data are pulled from data frames that we have created

    source1T1=data1[data1['TEAM'].str.contains(Team1)].values
    source2T1=data2[data2['TEAM'].str.contains(Team1)].values
    source3T1=data3[data3['TEAM'].str.contains(Team1)].values
    source1NBAT1=dataNBAadv[dataNBAadv.iloc[:,1].str.contains(Team1)].values
    source2NBAT1=dataNBAmisc[dataNBAmisc.iloc[:,1].str.contains(Team1)].values
    
    source1T2=data1[data1['TEAM'].str.contains(Team2)].values
    source2T2=data2[data2['TEAM'].str.contains(Team2)].values
    source3T2=data3[data3['TEAM'].str.contains(Team2)].values
    source1NBAT2=dataNBAadv[dataNBAadv.iloc[:,1].str.contains(Team2)].values
    source2NBAT2=dataNBAmisc[dataNBAmisc.iloc[:,1].str.contains(Team2)].values
    
    #We define the following quantities from our source vectors that will be used in the simulation.

    TotalPoss_1=float(source2T1[0,4])+float(source1T1[0,13])+.5*(float(source2T1[0,10])-.04*float(source2T1[0,4]))
    
    #This is the expected number of possessions for Team 1. It is computed by adding Team 1's total FGA/Game to its TO's/Game
    #to the number of FT trips per game. Number of FT trips per game is estimated by first removing And 1's from the total
    #number of FT attempts per game (And1's are estimated to occur on 1/25 FG attempts) and then dividing by 2. 
    
    ## ****NOTE: Throughout this program, we have not accounted for fouls on 3 PT shot attempts. 
    
    AdjTotalPoss_1=TotalPoss_1*(float(source1NBAT1[0,2]*48)/float(source1NBAT1[0,6]))
    
    #AdjTotalPoss_1 is TotalPoss_1 adjusted for a 48 minute game. Not used in the simulation.
    
    O_TORate_1=float(source1T1[0,13])/float(TotalPoss_1) #Team 1 turnover rate
    
    O_2PTRate_1=float(float(source2T1[0,4])-float(source2T1[0,7]))/float(TotalPoss_1) #Team 1 2 pt FG attempt rate
    
    O_3PTRate_1=float(source2T1[0,7])/float(TotalPoss_1) #Team 1 3 pt FG attempt rate
    
    O_FTRate_1=.5*(float(source2T1[0,10])-.04*float(source2T1[0,4]))/(TotalPoss_1) #Team 1 (estimated) FT rate
    
    O_RebRate_1=float(source1T1[0,10]) #Team 1 Offensive rebound rate
    
    O_FG2Perc_1=float(float(source2T1[0,3])-float(source2T1[0,6]))/float(float(source2T1[0,4])-float(source2T1[0,7]))
     #Team 1 2 pt FG%
    
    O_FG3Perc_1=float(source1T1[0,7]) #Team 1 3 pt FG%
    
    D_TORate_1= float(source1T1[0,14])/float(TotalPoss_1) #Rate at which Team 1 forces turnovers
    
    D_2PTRate_1=float(float(source3T1[0,4])-float(source3T1[0,7]))/float(TotalPoss_1) #Rate at which Team 1 allows 2 pt FGs
    
    D_3PTRate_1=float(source3T1[0,7])/float(TotalPoss_1) #Rate at which Team 1 allows 3 pt FGs
    
    D_FTRate_1=.5*(float(source3T1[0,10])-.04*float(source3T1[0,4]))/float(TotalPoss_1) #(Estimated) rate at which Team 1
    #allows FT trips
    
    D_RebRate_1=float(source1T1[0,11]) #Team 1 defensive rebound rate
    
    D_FG2Perc_1=float(float(source2T1[0,3])-float(source2T1[0,6]))/float(float(source2T1[0,4])-float(source2T1[0,7])) #Team 1 2 pt FG% allowed
    
    D_FG3Perc_1=float(source1T1[0,8]) #Team 1 3 pt FG% allowed 
    
    PtsPerTO_1=float(float(source2NBAT1[0,7])/float(source2NBAT1[0,2]))/float(source1T1[0,14]) #Points scored per TO forced
    
    PtsPerTOAllowed_1=float(float(source2NBAT1[0,11])/float(source2NBAT1[0,2]))/float(source1T1[0,13]) #Points allowed per own TO
    
    FTPerc_1=float(source1T1[0,9]) #Team 1 FT%
    
    O_NonTOFG2_1=(O_FG2Perc_1-O_TORate_1*O_2PTRate_1*(PtsPerTO_1/2))/(1-O_TORate_1*O_2PTRate_1)
    # Team 1 2pt FG % on 2pt FGs that do not come off TO's; computed using the formula TORate*FG2Rate*(PtsperTO/2)+
    #(1-TORate*FG2Rate)*z=O_FG2Perc, and solving for z, which is O_NonTOFG2.
    
    O_NonTOFG3_1=(O_FG3Perc_1-O_TORate_1*O_3PTRate_1*(PtsPerTO_1/3))/(1-O_TORate_1*O_3PTRate_1)
    # Team 1 3 pt FG % on non-TO 3 pt FGs
    
    D_NonTOFG2_1=(D_FG2Perc_1-D_TORate_1*D_2PTRate_1*(PtsPerTOAllowed_1/2))/(1-D_TORate_1*D_2PTRate_1)
    # Team 1 2 pt FG % allowed on non-TO 2pt FGs
    
    D_NonTOFG3_1=(D_FG3Perc_1-D_TORate_1*D_3PTRate_1*(PtsPerTOAllowed_1/3))/(1-D_TORate_1*D_3PTRate_1)
    # Team 1 3 pt FG % allowed on non-TO 3pt FGs
    

    
    #We have all the analogous stats for Team 2:
    

    TotalPoss_2=float(source2T2[0,4])+float(source1T2[0,13])+.5*(float(source2T2[0,10])-.04*float(source2T2[0,4]))
    AdjTotalPoss_2=TotalPoss_2*(float(source1NBAT2[0,2]*48)/float(source1NBAT2[0,6]))
    O_TORate_2=float(source1T2[0,13])/float(TotalPoss_2)
    O_2PTRate_2=float(float(source2T2[0,4])-float(source2T2[0,7]))/float(TotalPoss_2)
    O_3PTRate_2=float(source2T2[0,7])/float(TotalPoss_2)
    O_FTRate_2=.5*(float(source2T2[0,10])-.04*float(source2T2[0,4]))/(TotalPoss_2)
    O_RebRate_2=float(source1T2[0,10])
    O_FG2Perc_2=float(float(source2T2[0,3])-float(source2T2[0,6]))/float(float(source2T2[0,4])-float(source2T2[0,7]))
    O_FG3Perc_2=float(source1T2[0,7]) 
    D_TORate_2= float(source1T2[0,14])/float(TotalPoss_2)
    D_2PTRate_2=float(float(source3T2[0,4])-float(source3T2[0,7]))/float(TotalPoss_2)
    D_3PTRate_2=float(source3T2[0,7])/float(TotalPoss_2)
    D_FTRate_2=.5*(float(source3T2[0,10])-.04*float(source3T2[0,4]))/float(TotalPoss_2)
    D_RebRate_2=float(source1T2[0,11])
    PtsPerTO_2=float(float(source2NBAT2[0,7])/float(source2NBAT2[0,2]))/float(source1T2[0,14])
    PtsPerTOAllowed_2=float(float(source2NBAT2[0,11])/float(source2NBAT2[0,2]))/float(source1T2[0,13])
    FTPerc_2=float(source1T2[0,9])
    D_FG2Perc_2=float(float(source2T2[0,3])-float(source2T2[0,6]))/float(float(source2T2[0,4])-float(source2T2[0,7]))
    D_FG3Perc_2=float(source1T2[0,8])
    O_NonTOFG2_2=(O_FG2Perc_2-O_TORate_2*O_2PTRate_2*(PtsPerTO_2/2))/(1-O_TORate_2*O_2PTRate_2)
    O_NonTOFG3_2=(O_FG3Perc_2-O_TORate_2*O_3PTRate_2*(PtsPerTO_2/3))/(1-O_TORate_2*O_3PTRate_2)
    D_NonTOFG2_2=(D_FG2Perc_2-D_TORate_2*D_2PTRate_2*(PtsPerTOAllowed_1/2))/(1-D_TORate_2*D_2PTRate_2)
    D_NonTOFG3_2=(D_FG3Perc_2-D_TORate_2*D_3PTRate_2*(PtsPerTOAllowed_2/3))/(1-D_TORate_2*D_3PTRate_2)
    
    #NBASim will be defined below. It is the function that runs a simulation based on the inputs. 
  
    return NBASim(O_TORate_1, O_2PTRate_1, O_3PTRate_1, O_FTRate_1, O_RebRate_1, 
        D_TORate_1, D_2PTRate_1, D_3PTRate_1, D_FTRate_1, D_RebRate_1,
       
        PtsPerTO_1, PtsPerTOAllowed_1, TotalPoss_1, FTPerc_1, O_NonTOFG2_1, O_NonTOFG3_1, D_NonTOFG2_1, D_NonTOFG3_1,

        O_TORate_2, O_2PTRate_2, O_3PTRate_2, O_FTRate_2, O_RebRate_2, 
        D_TORate_2, D_2PTRate_2, D_3PTRate_2, D_FTRate_2, D_RebRate_2,
       
        PtsPerTO_2, PtsPerTOAllowed_2, TotalPoss_2, FTPerc_2, O_NonTOFG2_2, O_NonTOFG3_2, D_NonTOFG2_2, D_NonTOFG3_2)
        
        

def NBASim(O_TORate_1, O_2PTRate_1, O_3PTRate_1, O_FTRate_1, O_RebRate_1, #Frequency of various outcomes
       D_TORate_1, D_2PTRate_1, D_3PTRate_1, D_FTRate_1, D_RebRate_1,
       
       PtsPerTO_1, PtsPerTOAllowed_1, TotalPoss_1, FTPerc_1, O_NonTOFG2_1, O_NonTOFG3_1, D_NonTOFG2_1, D_NonTOFG3_1,

       O_TORate_2, O_2PTRate_2, O_3PTRate_2, O_FTRate_2, O_RebRate_2, #Frequency of various outcomes
       D_TORate_2, D_2PTRate_2, D_3PTRate_2, D_FTRate_2, D_RebRate_2,
       
       PtsPerTO_2, PtsPerTOAllowed_2, TotalPoss_2, FTPerc_2, O_NonTOFG2_2, O_NonTOFG3_2, D_NonTOFG2_2, D_NonTOFG3_2):

    Poss=TotalPoss_1+TotalPoss_2 # Total number of possessions for the game
    
    #Taking averages to compute various rates-- eg OffTO_1 is the average between the rate at which Team 1 turns it over and the
    #rate at which Team 2 forces turnovers.
    OffTO_1=.5*(O_TORate_1+D_TORate_2)
    Off2PT_1=.5*(O_2PTRate_1+D_2PTRate_2)
    Off3PT_1=.5*(O_3PTRate_1+D_3PTRate_2)
    OffFT_1=.5*(O_FTRate_1+D_FTRate_2)
    OffReb_1=.5*(O_RebRate_1+(1-D_RebRate_2))

    OffPtsPerTO_1=.5*(PtsPerTO_1+PtsPerTOAllowed_2)

    OffTO_2=.5*(O_TORate_2+D_TORate_1)
    Off2PT_2=.5*(O_2PTRate_2+D_2PTRate_1)
    Off3PT_2=.5*(O_3PTRate_2+D_3PTRate_1)
    OffFT_2=.5*(O_FTRate_2+D_FTRate_1)
    OffReb_2=.5*(O_RebRate_2+(1-D_RebRate_1))

    OffPtsPerTO_2=.5*(PtsPerTO_2+PtsPerTOAllowed_1)

    FG2Perc_1=.5*(O_NonTOFG2_1+D_NonTOFG2_2)
    FG3Perc_1=.5*(O_NonTOFG3_1+D_NonTOFG3_2)
    FG2Perc_2=.5*(O_NonTOFG2_2+D_NonTOFG2_1)
    FG3Perc_2=.5*(O_NonTOFG3_2+D_NonTOFG3_1)

#Team1_Offense is defined iteratively: Team1_Offense of the first iteration returns Team1_Offense of the second, 
#Team 1 of the second returns Team1 of the third iteration, etc, and eventually some iteration is going to return 
#something as p increases
    def Team1_Offense(Score1,Score2,p):
        if p<Poss:
            #Depending on which random number comes up, Team 1 either turns it over, shoots a 2pt FG, shoots a 3pt FG, or shoots FTs
            r=random.random()            
            if r<OffTO_1:                
                Score2=Score2+OffPtsPerTO_2
                p=p+2               
                (Score1,Score2,p)=Team1_Offense(Score1, Score2,p) 
                       
            elif r>OffTO_1 and r<OffTO_1+Off2PT_1:
                p=p+1
                t=random.random()
                if t<FG2Perc_1:   #If an average player gets an And1 on 1/25 shot attempts, then
                    #he gets it on about 1/10-1/12 makes, and converts the FT say about 75% of those 
                    #attempts. So, this adds approx .08 points to every 2pt fg
                    
                    #The random t variable determines whether the shot is made or missed
                    Score1=Score1+2.08
                    (Score2,Score1,p)=Team2_Offense(Score2,Score1,p)
                    
                else: 
                    u=random.random()
                    #The random u variable determines whether a miss is rebounded by the offense or defense
                    if u<OffReb_1:
                        (Score1,Score2,p)=Team1_Offense(Score1,Score2,p)
                        
                    else:
                        (Score2,Score1,p)=Team2_Offense(Score2,Score1,p)
                        
            elif r>OffTO_1+Off2PT_1 and r<OffTO_1+Off2PT_1+Off3PT_1:
                p=p+1
                t=random.random()
                if t<FG3Perc_1:
                    Score1=Score1+3  
                    (Score2,Score1,p)=Team2_Offense(Score2,Score1,p)
                    
                    
                else:
                    u=random.random()
                    
                    if u<OffReb_1:
                        (Score1,Score2,p)=Team1_Offense(Score1,Score2,p)
                        
                    else:
                        (Score2,Score1,p)=Team2_Offense(Score2,Score1,p)
                        
            elif r>OffTO_1+Off2PT_1+Off3PT_1 and r<OffTO_1+Off2PT_1+Off3PT_1+OffFT_1:           
                Score1=Score1+2*FTPerc_1 #Recall: we are assuming all FT attempts come off 2pt FG attempts
                p=p+1
                (Score2,Score1,p)=Team2_Offense(Score2,Score1,p)
                
            else:(Score1, Score2,p)=Team1_Offense(Score1,Score2,p) #ie else: replay the poss. it is necessary to have this here
            #because the way we have set it up, it is possible that OffTO_2+Off2PT_2+Off3PT_2+OffFT_2<1
            
        return [Score1,Score2,p]

    def Team2_Offense(Score2,Score1,p):
        if p<Poss:
            
            r=random.random()            
            if r<OffTO_2:
                Score1=Score1+OffPtsPerTO_1    
                p=p+2
                (Score2, Score1,p)=Team2_Offense(Score2, Score1,p)  
                
            elif r>OffTO_2 and r<OffTO_2+Off2PT_2:                
                p=p+1
                t=random.random()
               
                if t<FG2Perc_2:
                    Score2=Score2+2.08 
                    (Score1, Score2,p)=Team1_Offense(Score1,Score2,p)                    
                    
                else:
                    u=random.random()                    
                    if u<OffReb_2:

                        (Score2,Score1,p)=Team2_Offense(Score2,Score1,p)
                        
                    else:
                        (Score1,Score2,p)=Team1_Offense(Score1,Score2,p)    
                        
                        
            elif r>OffTO_2+Off2PT_2 and r<OffTO_2+Off2PT_2+Off3PT_2:
                p=p+1 
                t=random.random()
                if t<FG3Perc_2:
                    Score2=Score2+3   
                    (Score1, Score2,p)=Team1_Offense(Score1,Score2,p)                    
                    
                else:
                    u=random.random()
                    
                    if u<OffReb_2:
                        (Score2,Score1,p)=Team2_Offense(Score2,Score1,p)
                       
                    else:
                        (Score1,Score2,p)=Team1_Offense(Score1,Score2,p)   
                        
            elif r>OffTO_2+Off2PT_2+Off3PT_2 and r<OffTO_2+Off2PT_2+Off3PT_2+OffFT_2:
                Score2=Score2+2*FTPerc_2    
                p=p+1

                (Score1, Score2,p)=Team1_Offense(Score1,Score2,p)
                
            else:(Score1, Score2,p)=Team2_Offense(Score1,Score2,p) 

        return [Score2,Score1,p]
        
        

    #The game starts here. 
    Score1=0
    Score2=0
    p=0
    s=random.random()
    #The value of s decides who start with the ball. By running enough simulations, this does not end up favoring either team.
    #if p<Poss:
    if s<.5:
        (Score1, Score2,p)=Team1_Offense(Score1,Score2,p)
    else: 
        (Score2, Score1, p)=Team2_Offense(Score2,Score1,p)

    return [Score1, Score2, p]
 
#nSims runs WebSim m times and returns the average scores and difference 
def nSims(m,Team1,Team2):
    s1=0
    s2=0
    #p=0
    for i in range(m):
        s1=WebSim(Team1,Team2)[0]+s1
        s2=WebSim(Team1,Team2)[1]+s2
        #p=WebSim(Team1,Team2)[2]+p
    return s1/m,s2/m,s1/m-s2/m   

 


Table=G.T
#This takes the transpose of the the dataframe G, so Table now has 3 columns

length=range(len(Table))
#This is the number of rows in the Table, if we wish to know it.

#TableSims(m,k) will simulate the first m games listed on Bovada, k times each, and add the result in a fourth column.
#Column 6 will be added, which will have the sum and difference of the teams' projected scores. Column 5 will simply
#designate whether the corresponding entry in Column 6 is the sum or difference. Finally a blank column (Column 7) titled "Comments"
#will be inserted.

def TableSims(m,k): 
    Scores=[]
    SumAndDiff=[]
    for i in length[0:(2*m-1):2]: 
        Scores.append([])
        Scores.append([])
        SumAndDiff.append([])
        SumAndDiff.append([])
        Scores[i]=nSims(k,Table.loc[i,0][1:int(ceil(len(Table.loc[i,0])/3))+1],Table.loc[i+1,0][1:int(ceil(len(Table.loc[i+1,0])/3))+1])[0]
        Scores[i+1]=nSims(k,Table.loc[i,0][1:int(ceil(len(Table.loc[i,0])/3))+1],Table.loc[i+1,0][1:int(ceil(len(Table.loc[i+1,0])/3))+1])[1]
        SumAndDiff[i]=["Sum",Scores[i]+Scores[i+1]]
        SumAndDiff[i+1]=["Diff",Scores[i]-Scores[i+1]] 
    
    #The ceiling business is to make sure that each full team name 'City + Name' only contains the city 
    # so that espn can read it since espn tables only list city names.

    from pandas import concat

    #We turn each of the vectors defined above into dataframes so that they can be merged with the previously defined "Table".
    Score=pd.DataFrame(Scores)
    SD=pd.DataFrame(SumAndDiff)

    BigT=concat([Table,Score,SD],axis=1) #axis=1 instructs to concatenate along columns (axis=0 for rows is default)

    #The next 11 lines insert a blank row into the BigT after every two rows
    M=[]
    for i in range(1):
        M.append([])

    N=pd.DataFrame(M)

    df2=BigT
    k=0
    for i in range(len(BigT))[2:len(BigT):2]:
        df2 = concat([df2[:i+k], N,df2[i+k:]])
        k=k+1
    
    #Finally, we add the final blank column in Final
    df3=concat([df2.T[0:],N])
    
    Final=df3.T
    
    Final.columns=['Team','Spread','Total','Simulation','Sum/Diff','Sum or Diff Number','Comments']
    
    return Final

#We can then export the file to Excel:
def ToExcel(data,filename):


    data.to_excel('/Users/Dahlia/Documents/MY DOCS/JONAH_python_stuff/basketball/'+filename+'.xlsx', sheet_name='filename', index=False)       




