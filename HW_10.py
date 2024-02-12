import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'})

categories = data['whoAmI'].unique()

one_hot_encoded = pd.DataFrame()

for category in categories:
    one_hot_encoded[category] = (data['whoAmI'] == category).astype(int)

one_hot_encoded.head()
