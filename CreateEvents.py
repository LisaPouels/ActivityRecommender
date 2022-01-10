import pandas as pd

events = ['Escaperoom', 'Football Match', 'Art Museum', 'History Museum', 'Ballet', 'Classical Concert',
'Shopping Centre', 'Food Court', 'Nature Museum', 'Festival', 'Swimming Pool', 'Go Karting', 'Lasergaming', 'Paintball',
'Playground', 'Tea House']

categories = ['Crime, Mysteries, Horror, Thrillers', 'Sports, Action', 'Art, Romantic', 'Documentaries, History', 
'Art, Romantic, Dramas, Music', 'Classic, Romantic, Music', 'Children & Family, Comedies, Romantic', 'Comedies, Reality', 
'Documentaries, Science & Nature', 'International, Music', 'Kids, Adventure, Children & Family, Comedies', 
'Action & Adventure, Comedies, Sports', 'Action & Adventure, Sci-Fi, Crime, Sports', 
'Action & Adventure, Crime, Comedies, Sports', 'Kids, Teen, Children & Family, Action & Adventure', 'Romantic, Drama, British']


events_data = pd.DataFrame()
events_data['Event'] = events
events_data['Category'] = categories
