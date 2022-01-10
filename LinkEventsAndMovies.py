import CreateEvents
import MovieInformation
import pandas as pd
from collections import Counter

def SplitCategories(category_data):

    for i in range(0, len(category_data)):
        category_list = category_data[i]
        categories = category_list.split(', ')
        category_data[i] = categories

    return category_data

def CatCount(cat_data):
    all_categories = []
    for i in cat_data:
        for category in i:
            all_categories.append(category)
   
    cats = Counter(all_categories).keys()
    count = Counter(all_categories).values()

    cat_count = pd.DataFrame()
    cat_count['Category'] = cats
    cat_count['Count'] = count

    return cat_count

def TopCats(cat_data, n):
    cat_count = CatCount(cat_data)
    sorted_cat_count = cat_count.sort_values(by=['Count'], ascending=False)
    top_5 = sorted_cat_count.head(n)

    return top_5

def EventWeights(event_data, event_cat_data, top_cats):
    event_weights = []
    for i in event_cat_data:
        weight = 0
        for category in i:
            for cat in top_cats['Category']:
                if str(category) in cat or cat in category:
                    weight += 1
            final_weight = weight/len(i)
        event_weights.append(final_weight)

    events_df = pd.DataFrame()
    events_df['Event'] = event_data['Event']
    events_df['Weights'] = event_weights

    return events_df

def RecommendEvents(event_data, event_cat_data, top_cats, n):
    events_df = EventWeights(event_data, event_cat_data, top_cats)
    sorted_events = events_df.sort_values(by=['Weights'], ascending=False)

    recommended_events = sorted_events['Event'].head(n)

    return recommended_events

movie_1 = MovieInformation.movie_info_1.reset_index(drop=True)
movie_categories = movie_1['listed_in']
movie_cats_split = SplitCategories(movie_categories)

events = CreateEvents.events_data
event_cats = events['Category']
event_cats_split = SplitCategories(event_cats)

top_5 = TopCats(movie_cats_split, 5)

recommended_events = RecommendEvents(events, event_cats_split, top_5, 3)
