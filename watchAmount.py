import NetflixSeasons
import pandas as pd

def watchAmount(data):
    dict_times = {}

    for series in data['Serie']:
        if series not in dict_times:
            dict_times[series] = 0

        dict_times[series] += 1
    
    df_dict = pd.DataFrame.from_dict(dict_times, orient='index', columns=['watch_amount'])
    df_watch_amount = df_dict.reset_index()
    df_watch_amount['Title'] = df_watch_amount['index']
    final_df = df_watch_amount.drop(['index'], axis=1)

    return final_df

watch_amount_1 = watchAmount(NetflixSeasons.split_data_1)
watch_amount_2 = watchAmount(NetflixSeasons.split_data_2)
watch_amount_3 = watchAmount(NetflixSeasons.split_data_3)
watch_amount_4 = watchAmount(NetflixSeasons.split_data_4)
