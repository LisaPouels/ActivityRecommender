import NetflixData

def split_seasons(data):
    season_str = 'Season'
    types = []
    serie = []

    for movie in data['Title']:
        if season_str in movie or "Part":
            type = 'Series'
            types.append(type)
            parts = movie.split(':')
            serie_name = parts[0]
            serie.append(serie_name)
        else:
            type = 'Film'
            types.append('type')
            serie.append(movie)

    data['Type'] = types
    data['Serie'] = serie

    return data

split_data_1 = split_seasons(NetflixData.df_netflix_1)
split_data_2 = split_seasons(NetflixData.df_netflix_2)
split_data_3 = split_seasons(NetflixData.df_netflix_3)
split_data_4 = split_seasons(NetflixData.df_netflix_4)

            