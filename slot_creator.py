import pandas as pd
from collections import Counter

start_range = '09.07.2024'

# csv file contains columns like:
# date,time,A,B
# all entries for match days that teams are playing (A is home, B is away games)
df = pd.read_csv('match_days.csv', sep='\t')


df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')

df = df.sort_values(by='date')
df = df.reset_index(drop=True)

# filter only mondays
df = df[df['date'].dt.day_name() == 'Monday'].copy()

# add empty mondays
start_date = df['date'].min()
end_date = df['date'].max()
all_mondays = pd.date_range(start=start_range, end=end_date, freq='W-MON')

existing_mondays = df['date']
missing_mondays = all_mondays.difference(existing_mondays)
missing_data = pd.DataFrame({'date': missing_mondays, 'time': ['-'] * len(missing_mondays), 'A': [pd.NA] * len(missing_mondays), 'B': [pd.NA] * len(missing_mondays)})

df = pd.concat([df, missing_data], ignore_index=True)
df = df.sort_values(by='date').reset_index(drop=True)


'''
df = df[df['B'].str.contains('Teamname', case=False, na=False)]

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df_filled)
'''

empty_mondays = df[(df['A'].isna()) & (df['B'].isna())].copy()

teams = ['Teamname I', 'Teamname II', 'Teamname III']

# Count existing gym dates for each team
team_gym_counts = Counter(df['A'].dropna().tolist())

# Include the automatic gym dates where the team is implied by B (other two teams)
for team in df['B'].dropna():
    other_teams = [t for t in teams if t != team]
    for t in other_teams:
        team_gym_counts[t] += 1

# Calculate total required gym dates per team to balance them equally
total_gym_dates = len(df)
equal_share = total_gym_dates // len(teams)

# Find the teams that need more gym dates and distribute the empty Mondays among them
fill_counts = {team: equal_share - team_gym_counts[team] for team in teams}

# Fill empty Mondays with the teams that need more gym dates
filled_teams = []
for team, count in fill_counts.items():
    filled_teams.extend([team] * count)

# Assign teams to empty Mondays
for i, row in empty_mondays.iterrows():
    if filled_teams:
        df.at[i, 'A'] = filled_teams.pop(0)

# Sort and display
df = df.sort_values(by='date').reset_index(drop=True)

# Show the entire DataFrame
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df) 
