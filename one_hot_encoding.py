import pandas as pd
import numpy as np
poke = {'evolution': ['charmander', 'charmeleon', 'charizard', 'mega charizard x', 'mega charizard y', 'charizard', 'charmander']}
df = pd.DataFrame(poke)
print (df)
#here i used the help of ai to get what i was  thinking to code
unique_categories = df['evolution'].unique()
one_hot_df = pd.DataFrame()

for category in unique_categories:
  #if the row in df['evolution'] equals the category, put 1 else put 0
  one_hot_df[category] = np.where(df['evolution'] == category, 1, 0)

print (one_hot_df)
