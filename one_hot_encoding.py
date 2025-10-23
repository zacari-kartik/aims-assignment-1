import pandas as pd
poke = {'evolution': ['charmander', 'charmeleon', 'charizard', 'mega charizard x', 'mega charizard y', 'charizard', 'charmander']}
df = pd.DataFrame(poke)
one_hot = pd.get_dummies(df['evolution'])
print(one_hot)
