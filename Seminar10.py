import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

unique_values = data['whoAmI'].unique()
one_hot_view = pd.DataFrame()

for value in unique_values:
    one_hot_view[value] = (data['whoAmI'] == value).astype(int)
