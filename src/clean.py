import pandas as pd

df = pd.read_excel(‘data/seven-major-felony-offenses-by-precinct-2000-2017.xls', skiprows=2, skip_footer = 20)
df.PCT.fillna(method='ffill', inplace=True)
df.CRIME = df.CRIME.astype('str')
df = df[~df.CRIME.str.contains('TOTAL')]
df = df.fillna(0)
df.PCT = df.PCT.astype('int')
for i in df.columns[2:]:
    df[i] = df[i].astype('int')
df.CRIME = df.CRIME.map(lambda precinct: precinct.rstrip(' '))
crimes = pd.Series.unique(df.CRIME)
crimesMax = {}

for crime in crimes:
    subset = df[df.CRIME == crime]
    subset = subset.drop(subset.columns[[0, 1]], axis = 1)
    crimesMax[crime] = max(subset.max())

df['Max'] = df.apply(lambda row: crimesMax[row.CRIME], axis = 1)
df.to_csv(‘data/clean-crimesPCT-data.csv')
