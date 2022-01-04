import pandas as pd

filepath = "C:/Users/20193222/Dropbox/school/TUe en Tilburg University/Startups/ActivityRecommender"

df_netflix_1 = pd.read_csv(filepath + '/Data/NetflixViewingHistory_Kim.csv')
df_netflix_2 = pd.read_csv(filepath + '/Data/NetflixViewingHistory_Lieke.csv')
df_netflix_3 = pd.read_csv(filepath + '/Data/NetflixViewingHistory_Lisa.csv')
df_netflix_4 = pd.read_csv(filepath + '/Data/NetflixViewingHistory_Roelle.csv')
df_titles = pd.read_csv(filepath + '/Data/netflix_titles.csv')
