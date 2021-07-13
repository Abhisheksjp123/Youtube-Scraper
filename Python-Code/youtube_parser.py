#### This program scrapes youtube.com's page and gives our result as a 
#### list of all the videos in a channel which are currently present there. 
  
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import numpy as np
#%%
#url of the page we want to scrape
url = "https://www.youtube.com/c/MrVivekBindra/videos"
# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome(r"C:\chromedriver.exe") 
driver.get(url) 

# this is just to ensure that the page is loaded
time.sleep(10) 
###  IMP MUST READ###
#SCROLL THROUGHT THE WHOLE PAGE BEFOR RUNNING SCRIPT AFTER THIS TO GET ALL THE VIDEOS
###
#%%
html = driver.page_source


  
# this renders the JS code and stores all
# of the information in static HTML code.
#%%
# Now, we could simply apply bs4 to html variable
#here we parse the html and define the container
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find('div', {'id' : 'contents'})
#here we select all  the title of the videos
job_profiles = all_divs.find_all('a',{'id' : 'video-title'})
lenth = len(job_profiles)


#here we select date uploaded and views of the video
date = all_divs.find_all('span',{'class' : 'style-scope ytd-grid-video-renderer'})

video_time = all_divs.find_all('span',{'class' : 'style-scope ytd-thumbnail-overlay-time-status-renderer'})

title = []
views = []
on = []
duration = []

#extracting title date in list
for i in job_profiles :
  title.append(i.text)

#extracting views and upload date in list
n = 0
while n<lenth*2:
  try:
    views.append(date[n].text)
    on.append(date[n+1].text)
    n = n+2
  except:
    break

#extracting duration in list
for i in video_time :
  duration.append(i.text)


#creating a df and storing everything in that df
titleS = pd.Series(np.array(title),name = "title")
viewsS = pd.Series(np.array(views),name = "views")
onS = pd.Series(np.array(on),name = "upload_date")
durationS = pd.Series(np.array(duration),name = "duration")

df_temp = pd.DataFrame()
df_temp["title"] = titleS
df_temp["views"] = viewsS
df_temp["upload_date"] = onS
df_temp["duration"] = durationS

df_temp.to_csv(r"C:\Users\abhis\Desktop\YT_FIN\MrVivekBindra.csv")


#count = 0
#for i in job_profiles :
#    print(i.text)
#    count = count + 1
#    if(count == 1016) :
#        break
##%%
driver.close()