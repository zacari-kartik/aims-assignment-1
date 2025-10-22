import pandas as pd
poke = {'evolution': ['charmander', 'charmeleon', 'charizard', 'mega charizard x', 'mega charizard y', 'charmeleon', 'charizard']}
df = pd.DataFrame(poke)
print(df)
evolution_order = {'charmander': 1, 'charmeleon': 2, 'charizard': 3, 'mega charizard x': 4, 'mega charizard y': 5}
df['evolution_encoded'] = df['evolution'].map(evolution_order)
print(df)
