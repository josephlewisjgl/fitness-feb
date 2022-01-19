import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

'''
# Fitness Feb Tracker and Leader Board

The contest begins on February 1st and finished February 28th. 

The main competition is for kilometres run/walked.

For evidence to be counted it must be sent to the SnapChat group chat as a picture of either:
'''
st.write('- Treadmill showing kilometres alongside the time taken')
st.write('- Screen shots of Nike/Strava app with kilometres and time')
st.write('- Pictures of smart watches with kilometres and time')

df = pd.read_excel('Data.xlsx', 0)

df.sort_values('KM', inplace=True, ascending=False)
df.reset_index(inplace=True)

df['Rank'] = df.index + 1

df.index = df['Rank']
df.drop(['Rank', 'index'], inplace=True, axis=1)

left, right = st.columns([3,1])

with left:
    '''
    ### Rules and Regulations: 
    
    - Evidence must be sent.
    - All recorded kilometres must be your own. Cheaters will have km's taken away.
    - Any entries after March 1st will not be counted.
    - Points awarded for minigames are in the extra competition pot and do not effect the kilometre race.
    
    ### Minigame Points:
    
    - In the first week of the competition everyone should record how many press ups they can do. The person who records the greatest increase by the end of the month will win one £10 PlayStation voucher
    - In the second week of the competition (07/02 - 14/02) the person to run the fastest kilometre will win manager for the day on pro clubs.
    - In the third week of the competition the person to dead lift the greatest percentage of their body weight will win one choice of restaurant/game for a night.
    - In the fourth and final week of the competition the person who takes the nicest picture while on a walk/run will win one night of niceness (noone can be mean like a birthday). 
    
    Punishments and Prizes:
    
    - The outright winner can cash in either a meal at a restaurant (up to £30 in value to be shared between the rest of the competitors) or does not have to pay for a night of drinking.
    - The top three will all get to decide what drinks each member of the bottom three respectively have to drink on a night out (for non-drinkers their meal will be chosen instead).
    - The outright loser has to wear an outfit assembled by the other boys on a night out.
    
    '''
with right:
    '''
    # Ranking 
    '''
    st.table(df)

exp = st.expander('Charted km')

with exp:
    b = px.bar(df, 'KM', 'Boy', orientation='h', template='seaborn', color='Boy')
    st.write(b)