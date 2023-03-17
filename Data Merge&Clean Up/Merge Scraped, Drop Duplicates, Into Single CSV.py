import pandas as pd
import datetime

start_date = "01-01-2017"
end_date = "16-09-2021"
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

#Create a dataframe with same columns and drop all rows
df = pd.read_csv('D:\z - S Scraper\Data\Chart Data\Spotify\Viral 50\Individual\Pre-Song Data\{}.csv'.format('2017-01-01'))
df.drop(df.index, inplace=True)

for date in date_list:
    df_con = pd.read_csv('D:\z - S Scraper\Data\Chart Data\Spotify\Viral 50\Individual\Pre-Song Data\{}.csv'.format(date))
    df = pd.concat([df, df_con], ignore_index=True)

df.drop_duplicates(subset=['Track Name', 'Artist'], keep='first', inplace=True)


df.drop(df.columns[[0]], axis = 1, inplace = True)
df.reset_index(inplace = True)
df.drop(df.columns[[0]], axis = 1, inplace = True)


df.to_csv('Merged{} to {}.csv'.format(start_date, end_date))
