import NetflixData
import NetflixSeasons


def get_movie_info(data):
    unique_watched = data['Serie'].unique()
    movie_information = NetflixData.df_titles[['title', 'type', 'country', 'rating', 'listed_in']]
    
    unique_movie_info = movie_information[movie_information['title'].isin(unique_watched)]

    return unique_movie_info

movie_info_1 = get_movie_info(NetflixSeasons.split_data_1)
movie_info_2 = get_movie_info(NetflixSeasons.split_data_2)
movie_info_3 = get_movie_info(NetflixSeasons.split_data_3)
movie_info_4 = get_movie_info(NetflixSeasons.split_data_4)
