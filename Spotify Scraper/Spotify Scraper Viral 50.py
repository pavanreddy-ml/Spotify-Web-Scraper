from selenium import webdriver
import pandas as pd
import re
import datetime

pd.set_option('display.max_columns', 4)

start_date = "17-07-2018"
end_date = "17-09-2021"
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





#Main Loop
driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\WebDrivers\chromedriver.exe')

for date in date_list:
    driver.get('https://spotifycharts.com/viral/us/daily/{}'.format(date))

    rows = len(driver.find_elements_by_xpath('//*[@id="content"]/div/div/div/span/table/tbody/tr'))

    position_list = []
    track_list = []
    artist_list = []
    featured_list = []
    date_column = []

    for r in range(1, rows + 1):
        position = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/span/table/tbody/tr[{}]/td[2]'.format(str(r))).text
        position_list.append(position)

        track_name = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/span/table/tbody/tr[{}]/td[4]/strong'.format(str(r))).text
        track_list.append(track_name)

        artist_name = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/span/table/tbody/tr[{}]/td[4]/span'.format(str(r))).text
        artist_name = artist_name[3:]
        artist_list.append(artist_name)

        featured_artist_temp = re.search('\(feat. (.*)\)', track_name)
        try:
            featured_artist = featured_artist_temp.group(1)
        except:
            featured_artist = ""
        featured_list.append(featured_artist)

        date_column.append(date)


    df = pd.DataFrame(list(zip(date_column, position_list, track_list, artist_list, featured_list, )),
                      columns=['Date', 'Position', 'Track Name', 'Artist', 'Featured Artists',])
    print(df)

    df.to_csv('{}.csv'.format(date))

driver.quit()