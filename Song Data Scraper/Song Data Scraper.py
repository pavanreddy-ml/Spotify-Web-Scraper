from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from difflib import SequenceMatcher
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import numpy as np




def scrape_data():
    global Key, camelot, BPM, Album, Length, Release_date, Time_Signature, Loudness_db, Popularity, Acousticness, Danceability, Energy, Instrumentalness, Liveness, Loudness_100, Speechiness, Valence

    Key = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div/div[2]/div[1]').text
    camelot = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div/div[2]/div[2]').text
    BPM = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div/div[2]/div[3]').text
    Album = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div/div[2]/div[5]/a').text
    Length = driver.find_element_by_xpath('//*[@id="length"]/p[2]').text
    Release_date = driver.find_element_by_xpath('//*[@id="release"]/p[2]').text
    Time_Signature = driver.find_element_by_xpath('//*[@id="time"]/p[2]').text
    Loudness_db = driver.find_element_by_xpath('//*[@id="loudness"]/p[2]').text
    Popularity = driver.find_element_by_xpath('//*[@id="popularity"]/div/div').get_attribute("aria-valuenow")
    Acousticness = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div[1]/div[2]/span').text
    Danceability = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/span').text
    Energy = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/span').text
    Instrumentalness = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[2]/span').text
    Liveness = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/div/div[1]/div[3]/div[1]/div[2]/span').text
    Loudness_100 = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div[2]/span').text
    Speechiness = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[1]/div[2]/span').text
    Valence = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div[1]/div[2]/span').text


    Loudness_db = Loudness_db.rstrip(' dB')
    Acousticness = Acousticness.rstrip('%')
    Danceability = Danceability.rstrip('%')
    Energy = Energy.rstrip('%')
    Instrumentalness = Instrumentalness.rstrip('%')
    Liveness = Liveness.rstrip('%')
    Loudness_100 = Loudness_100.rstrip('%')
    Speechiness = Speechiness.rstrip('%')
    Valence = Valence.rstrip('%')


def update_data(ind):
    global Key, camelot, BPM, Album, Length, Release_date, Time_Signature, Loudness_db, Popularity, Acousticness, Danceability, Energy, Instrumentalness, Liveness, Loudness_100, Speechiness, Valence

    df.loc[ind, 'Key'] = Key
    df.loc[ind, 'Camelot'] = camelot
    df.loc[ind, 'BPM'] = BPM
    df.loc[ind, 'Album'] = Album
    df.loc[ind, 'Length'] = Length
    df.loc[ind, 'Release Date'] = Release_date
    df.loc[ind, 'Time Signature'] = Time_Signature
    df.loc[ind, 'Loudness(dB)'] = Loudness_db
    df.loc[ind, 'Popularity'] = Popularity
    df.loc[ind, 'Acousticness'] = Acousticness
    df.loc[ind, 'Danceability'] = Danceability
    df.loc[ind, 'Energy'] = Energy
    df.loc[ind, 'Instrumentalness'] = Instrumentalness
    df.loc[ind, 'Liveness'] = Liveness
    df.loc[ind, 'Loudness %'] = Loudness_100
    df.loc[ind, 'Speechiness'] = Speechiness
    df.loc[ind, 'Valence'] = Valence






def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


#Main Loop
df = pd.read_csv('Data.csv')
rows, columns = df.shape


driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\WebDrivers\chromedriver.exe')
driver.maximize_window()

driver.get('https://songdata.io/')



for index in range(0,rows):
    Track, Artist = df.loc[index, ['Track Name', 'Artist']]
    name = str(Track) + ' ' + str(Artist)

    # if df.loc[index, 'Key'] != np.nan:
    #     continue

    try:
        driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div/div/form/div/div/input').clear()
        driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div/div/form/div/div/input').send_keys(name)
        driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div/div/form/div/div/input').send_keys(Keys.ENTER)
    except:
        driver.find_element_by_xpath('//*[@id="navbar_global"]/ul/li[4]/form/div/div/input').clear()
        driver.find_element_by_xpath('//*[@id="navbar_global"]/ul/li[4]/form/div/div/input').send_keys(name)
        driver.find_element_by_xpath('//*[@id="navbar_global"]/ul/li[4]/form/div/div/input').send_keys(Keys.ENTER)

    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[2]/a')))
    except:
        continue

    Track_ratio = []
    Artist_ratio = []

    for i in range(1,5):
        try:
            Track_search = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div/table/tbody/tr[{}]/td[2]/a'.format(str(i))).text
            Artist_search = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div/table/tbody/tr[{}]/td[3]'.format(str(i))).text
            Track_ratio.append(similar(Track, Track_search))
            Artist_ratio.append(similar(Artist, Artist_search))
        except:
            break


    if len(Track_ratio) == 0:
        continue

    count = 0

    for i in range(0, len(Track_ratio)):
        if (Track_ratio[i] >= 0.6) & (Artist_ratio[i] >= 0.6):
            count += 1
            driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div/table/tbody/tr[{}]/td[2]/a'.format(str(i+1))).click()
            break

    if count == 0:
        continue


    scrape_data()
    update_data(index)


    #print(Key, camelot, BPM, Album, Length, Release_date, Time_Signature, Loudness_db, Popularity, Acousticness, Danceability, Energy, Instrumentalness, Liveness, Loudness_100, Speechiness, Valence, sep='\n')



    df.to_csv('Data Updated.csv')

driver.quit()