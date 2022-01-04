import pandas as pd

events = ['Escaperoom', 'Football Match', 'Art Museum', 'History Museum', 'Ballet', 'Classical Concert', 'Christmas Market',
'Shopping Centre', 'Food Court', 'Nature Museum']

categories = ['Crime, Mysteries, Horror, Thrillers', 'Sports, Action', 'Art, Romantic', 'Documentaries, History', 
'Art, Romantic, Dramas', 'Classic, Romantic', 'Children & Family, Comedies', 'Children & Family, Romantic', 
'Comedies, Reality', 'Documentaries']


events_data = pd.DataFrame()
events_data['Event'] = events
events_data['Category'] = categories
