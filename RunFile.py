import NetflixSeasons
import MovieInformation
import CreateEvents
import LinkEventsAndMovies
import pandas as pd
from collections import Counter

#import data 
filepath = "C:/Users/20193222/Dropbox/school/TUe en Tilburg University/Startups/ActivityRecommender"

df_watch_history = pd.read_csv(filepath + '/Data/NetflixViewingHistory_Kim.csv') #watchHistory
df_neflix_titles = pd.read_csv(filepath + '/Data/netflix_titles.csv') #netflixInfo

#get series names (split off epsides/seasons) (NetflixSeasons)
split_watch_history = NetflixSeasons.split_seasons(df_watch_history)

#get movie information (MovieInformation)
watch_history_info = MovieInformation.get_movie_info(split_watch_history)

#create custom events/activities + categories (CreateEvents)
events = CreateEvents.events_data

#connect movie and event categories and recommend events (LinkEventsAndMovies)
watch_history_info_reset = watch_history_info.reset_index(drop=True)
movie_categories = watch_history_info_reset['listed_in']
movie_cats_split = LinkEventsAndMovies.SplitCategories(movie_categories)

event_cats = events['Category']

top_5 = LinkEventsAndMovies.TopCats(movie_cats_split, 5)

recommended_events = LinkEventsAndMovies.RecommendEvents(events, event_cats, top_5, 3)

print(top_5, recommended_events)