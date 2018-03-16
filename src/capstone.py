import pandas as import pd
import numpy as np


## Load CSV files of season data from 2007/08-2016/17 Mens NCAA Division 1 Basketball

df_16_17 = pd.read_csv('data/2016-2017_NCAA.csv')
df_15_16 = pd.read_csv('data/2015-2016_NCAA.csv')
df_14_15 = pd.read_csv('data/2014-2015_NCAA.csv')
df_13_14 = pd.read_csv('data/2013-2014_NCAA.csv')
df_12_13 = pd.read_csv('data/2012-2013_NCAA.csv')
df_11_12 = pd.read_csv('data/2011-2012_NCAA.csv')
df_10_11 = pd.read_csv('data/2010-2011_NCAA.csv')
df_09_10 = pd.read_csv('data/2009-2010_NCAA.csv')
df_08_09 = pd.read_csv('data/2008-2009_NCAA.csv')
df_07_08 = pd.read_csv('data/2007-2008_NCAA.csv')

# Convert row 0 to column names for each dataframe

df_16_17.columns = df_16_17.iloc[0]
df_15_16.columns = df_15_16.iloc[0]
df_14_15.columns = df_14_15.iloc[0]
df_13_14.columns = df_13_14.iloc[0]
df_12_13.columns = df_12_13.iloc[0]
df_11_12.columns = df_11_12.iloc[0]
df_10_11.columns = df_10_11.iloc[0]
df_09_10.columns = df_09_10.iloc[0]
df_08_09.columns = df_08_09.iloc[0]
df_07_08.columns = df_07_08.iloc[0]

# Drop column 0 which has been converted to column names

df_16_17_drop_0 = df_16_17.drop([0])
df_15_16_drop_0 = df_15_16.drop([0])
df_14_15_drop_0 = df_14_15.drop([0])
df_13_14_drop_0 = df_13_14.drop([0])
df_12_13_drop_0 = df_12_13.drop([0])
df_11_12_drop_0 = df_11_12.drop([0])
df_10_11_drop_0 = df_10_11.drop([0])
df_09_10_drop_0 = df_09_10.drop([0])
df_08_09_drop_0 = df_08_09.drop([0])
df_07_08_drop_0 = df_07_08.drop([0])

# Add season columns to all dataframes
df_16_17_drop_0['Season'] = '2016-2017'
df_15_16_drop_0['Season'] = '2015-2016'
df_14_15_drop_0['Season'] = '2014-2015'
df_13_14_drop_0['Season'] = '2013-2014'
df_12_13_drop_0['Season'] = '2012-2013'
df_11_12_drop_0['Season'] = '2011-2012'
df_10_11_drop_0['Season'] = '2010-2011'
df_09_10_drop_0['Season'] = '2009-2010'
df_08_09_drop_0['Season'] = '2008-2009'
df_07_08_drop_0['Season'] = '2007-2008'

# Make list of all dataframes
years = [df_16_17_drop_0,
         df_15_16_drop_0,
         df_14_15_drop_0,
         df_13_14_drop_0,
         df_12_13_drop_0,
         df_11_12_drop_0,
         df_10_11_drop_0,
         df_09_10_drop_0,
         df_08_09_drop_0,
         df_07_08_drop_0]

# Concatenate all dataframes
df_main = pd.concat(years)

# drop teams not in NCAA tournament
df_tourney = df_main[df_main['School'].str.contains('NCAA')]

# reset indexes
df_tourney = df_tourney.reset_index(drop=True)

# Make list of play-in game losing teams
play_in_game_losers = [
df_tourney.index[(df_tourney.School == 'Coppin State NCAA') & (df_tourney.Season == '2007-2008')],
df_tourney.index[(df_tourney.School == 'Alabama State NCAA') & (df_tourney.Season == '2008-2009')],
df_tourney.index[(df_tourney.School == 'Winthrop NCAA') & (df_tourney.Season == '2009-2010')],
df_tourney.index[(df_tourney.School == 'Arkansas-Little Rock NCAA') & (df_tourney.Season == '2010-2011')],
df_tourney.index[(df_tourney.School == 'Alabama-Birmingham NCAA') & (df_tourney.Season == '2010-2011')],
df_tourney.index[(df_tourney.School == 'Alabama State NCAA') & (df_tourney.Season == '2010-2011')],
df_tourney.index[(df_tourney.School == 'Southern California NCAA') & (df_tourney.Season == '2010-2011')],
df_tourney.index[(df_tourney.School == 'Mississippi Valley State NCAA') & (df_tourney.Season == '2011-2012')],
df_tourney.index[(df_tourney.School == 'Iona NCAA') & (df_tourney.Season == '2011-2012')],
df_tourney.index[(df_tourney.School == 'Lamar NCAA') & (df_tourney.Season == '2011-2012')],
df_tourney.index[(df_tourney.School == 'University of California NCAA') & (df_tourney.Season == '2011-2012')],
df_tourney.index[(df_tourney.School == 'Liberty NCAA') & (df_tourney.Season == '2012-2013')],
df_tourney.index[(df_tourney.School == 'Middle Tennessee NCAA') & (df_tourney.Season == '2012-2013')],
df_tourney.index[(df_tourney.School == 'Long Island University NCAA') & (df_tourney.Season == '2012-2013')],
df_tourney.index[(df_tourney.School == 'Boise State NCAA') & (df_tourney.Season == '2012-2013')],
df_tourney.index[(df_tourney.School == "Mount St. Mary's NCAA") & (df_tourney.Season == '2013-2014')],
df_tourney.index[(df_tourney.School == 'Xavier NCAA') & (df_tourney.Season == '2013-2014')],
df_tourney.index[(df_tourney.School == 'Texas Southern NCAA') & (df_tourney.Season == '2013-2014')],
df_tourney.index[(df_tourney.School == 'Iowa NCAA') & (df_tourney.Season == '2013-2014')],
df_tourney.index[(df_tourney.School == 'Manhattan NCAA') & (df_tourney.Season == '2014-2015')],
df_tourney.index[(df_tourney.School == 'Brigham Young NCAA') & (df_tourney.Season == '2014-2015')],
df_tourney.index[(df_tourney.School == 'North Florida NCAA') & (df_tourney.Season == '2014-2015')],
df_tourney.index[(df_tourney.School == 'Boise State NCAA') & (df_tourney.Season == '2014-2015')],
df_tourney.index[(df_tourney.School == 'Fairleigh Dickinson NCAA') & (df_tourney.Season == '2015-2016')],
df_tourney.index[(df_tourney.School == 'Vanderbilt NCAA') & (df_tourney.Season == '2015-2016')],
df_tourney.index[(df_tourney.School == 'Southern NCAA') & (df_tourney.Season == '2015-2016')],
df_tourney.index[(df_tourney.School == 'Tulsa NCAA') & (df_tourney.Season == '2015-2016')],
df_tourney.index[(df_tourney.School == 'New Orleans NCAA') & (df_tourney.Season == '2016-2017')],
df_tourney.index[(df_tourney.School == 'Wake Forest NCAA') & (df_tourney.Season == '2016-2017')],
df_tourney.index[(df_tourney.School == 'North Carolina Central NCAA') & (df_tourney.Season == '2016-2017')],
df_tourney.index[(df_tourney.School == 'Providence NCAA') & (df_tourney.Season == '2016-2017')],
]

#Drop play-in game losers from data frame
df_tourney_no_play_in = df_tourney.drop([int(i[0]) for i in play_in_game_losers])

# Create new column 'Tournament_Wins'
df_tourney_no_play_in['Tournament_Wins'] = 0
