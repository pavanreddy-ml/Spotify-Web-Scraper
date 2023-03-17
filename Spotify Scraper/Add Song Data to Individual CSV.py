from selenium import webdriver
import pandas as pd
import re
import datetime
import numpy as np


start_date = "01-01-2017"
end_date = "05-01-2017"
date_list = []

def create_date_list(x, y):
    global date_list
    date_list = []
    start = datetime.datetime.strptime(x, "%d-%m-%Y")
    end = datetime.datetime.strptime(y, "%d-%m-%Y")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

    for date in date_generated:
        date_list.append(date.strftime("%Y-%m-%d"))


create_date_list(start_date, end_date)

index1 = 0
index2 = 0


def update_data():
    global index1, index2

    df.loc[index1, 'Key'] = mainframe.loc[index2, 'Key'].item()
    df.loc[index1, 'Camelot'] = mainframe.loc[index2, 'Camelot'].item()
    df.loc[index1, 'BPM'] = mainframe.loc[index2, 'BPM'].item()
    df.loc[index1, 'Album'] = mainframe.loc[index2, 'Album'].item()
    df.loc[index1, 'Length'] = mainframe.loc[index2, 'Length'].item()
    df.loc[index1, 'Release Date'] = mainframe.loc[index2, 'Release Date'].item()
    df.loc[index1, 'Time Signature'] = mainframe.loc[index2, 'Time Signature'].item()
    df.loc[index1, 'Loudness(dB)'] = mainframe.loc[index2, 'Loudness(dB)'].item()
    df.loc[index1, 'Popularity'] = mainframe.loc[index2, 'Popularity'].item()
    df.loc[index1, 'Acousticness'] = mainframe.loc[index2, 'Acousticness'].item()
    df.loc[index1, 'Danceability'] = mainframe.loc[index2, 'Danceability'].item()
    df.loc[index1, 'Energy'] = mainframe.loc[index2, 'Energy'].item()
    df.loc[index1, 'Instrumentalness'] = mainframe.loc[index2, 'Instrumentalness'].item()
    df.loc[index1, 'Liveness'] = mainframe.loc[index2, 'Liveness'].item()
    df.loc[index1, 'Loudness %'] = mainframe.loc[index2, 'Loudness %'].item()
    df.loc[index1, 'Speechiness'] = mainframe.loc[index2, 'Speechiness'].item()
    df.loc[index1, 'Valence'] = mainframe.loc[index2, 'Valence'].item()


mainframe = pd.read_csv('D:\z - S Scraper\Codes\Song Data Scraper\Data Updated.csv')

#Main Loop
for i in date_list:
    df = pd.read_csv('D:\z - S Scraper\Data\Chart Data\Spotify\Viral 50\Individual\Pre-Song Data\{}.csv'.format(i))
    rows, columns = df.shape

    for index1 in range(0, rows):
        Track, Artist = df.loc[index1, ['Track Name', 'Artist']]



        if Track in mainframe['Track Name'].values:
            index2 = mainframe.loc[(mainframe['Track Name'] == Track)].index
            update_data()



    #df.to_csv('{}-With song Data.csv'.format(i))




