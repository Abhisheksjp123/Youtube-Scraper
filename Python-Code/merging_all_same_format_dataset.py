#merging all scraped/ same format csvs
#importing
import pandas as pd
import numpy as np
import os
#%%
# getting all the file names as list
csv_files = os.listdir(r"C:\Users\abhis\Desktop\YT_FIN")
#%%
#creating df to contain all data
df = pd.DataFrame()
#%%
#creating loop to add all csv to df one by one
#csv_files = csv_files[0:2]
for file in csv_files:
  df_temp = pd.DataFrame()
  df_temp = pd.read_csv(r"C:\Users\abhis\Desktop\YT_FIN\{}".format(file))
  df_temp["Channel"] = file
  df = pd.concat([df,df_temp])
#%%
# saving it as csv
df.to_csv(r"C:\Users\abhis\Desktop\YT_FIN\YT_FIN_COMB.csv")