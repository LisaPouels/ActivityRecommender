import CreateEvents
import MovieInformation
import pandas as pd
import numpy as np
from collections import Counter

movie_1 = MovieInformation.movie_info_1.reset_index(drop=True)
category_list = movie_1['listed_in']

for i in range(0, len(category_list)):
    categories = category_list[i]
    parts = categories.split(', ')
    category_list[i] = parts


events = CreateEvents.events_data
event_cats = events['Category']

for i in range(0, len(event_cats)):
    categories = event_cats[i]
    parts = categories.split(', ')
    event_cats[i] = parts

all_categories = []
for category in category_list:
    for item in category:
        all_categories.append(item)
        

cats = Counter(all_categories).keys()
count = Counter(all_categories).values()

cat_count = pd.DataFrame()
cat_count['Category'] = cats
cat_count['Count'] = count

percent_count = []
for val in count:
    percent_count.append((val/sum(count))*100)

cat_count['Percentage'] = percent_count

sorted_cat_count = cat_count.sort_values(by=['Percentage'], ascending=False)
top_5 = sorted_cat_count.head()

event_weights = []
for i in event_cats:
    weight = 0
    for category in i:
        for cat in top_5['Category']:
            if str(category) in cat:
                weight += 1
        final_weight = weight/len(i)
    event_weights.append(final_weight)

events_df = pd.DataFrame()
events_df['Event'] = events['Event']
events_df['Weights'] = event_weights

sorted_events = events_df.sort_values(by=['Weights'], ascending=False)

print(sorted_events['Event'].head(3))
