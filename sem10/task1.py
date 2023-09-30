import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

categories = list(set(data['whoAmI']))
one_hot_dict = {category: [1 if item == category else 0 for item in data['whoAmI']] for category in categories}

one_hot_df = pd.DataFrame(one_hot_dict)

data = pd.concat([data, one_hot_df], axis=1)

data.drop(columns=['whoAmI'], inplace=True)

data.head()
print(data)
