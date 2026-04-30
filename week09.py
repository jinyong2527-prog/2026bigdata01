import numpy as np
import pandas as pd

arr2d = np.array(
    [
        [1, 2, 3],
        [6, 4, 5],
        [7, 8, 9]
    ]
)
# df_2dlist = pd.DataFrame(arr2d, columns=['국', '영', '수'], index=[1, 2, 3])

# Creating Dataframes
df = pd.DataFrame({'국':[1, 6, 7], '영':[2, 4, 8], '수':[3, 5, 9]}, index=[1, 2, 3])
df_2dlist = pd.DataFrame([[1, 2, 3], [6, 4, 5], [7, 8, 9]], columns=['국', '영', '수'], index=[1, 2, 3])
df_dict = pd.DataFrame({'국':[1, 6, 7], '영':[2, 4, 8], '수':[3, 5, 9]}, index=[1, 2, 3])
print(arr2d)
print(df_2dlist)
print(df_dict)

df = pd.DataFrame({'국':[1, 6, 7], '영':[2, 4, 8], '수':[3, 5, 9]}, index=[1, 2, 3])
print(df)
# df_new = pd.melt(df)
# df_new = pd.melt(df).rename(columns={'variable': 'var', 'value': 'val'})
df_new = pd.melt(df).rename(columns={'variable': 'var', 'value': 'val'}).query('val > 5')
print(df_new)

# Creating Dataframes
df_2dlist = pd.DataFrame([[1, 2, 3], [6, 4, 5], [7, 8, 9]], columns=['국', '영', '수'], index=[1, 2, 3])
df_dict = pd.DataFrame({'국':[1, 6, 7], '영':[2, 4, 8], '수':[3, 5, 9]}, index=[1, 2, 3])
print(arr2d)
print(df_2dlist)
print(df_dict)
print(df_dict)

df = pd.DataFrame({'국':[1, 6, 7], '영':[2, 4, 8], '수':[3, 5, 9]}, index=[1, 2, 3])
print(df)
# df_new = pd.melt(df)
# df_new = pd.melt(df).rename(columns={'variable': 'var', 'value': 'val'})
df_new = pd.melt(df).rename(columns={'variable': 'var', 'value': 'val'}).query('val > 5')
print(df_new)

df = pd.DataFrame({'국':[1, 6, 7], '영':[2, 4, 8], '수':[3, 5, 9], '미세먼지':[10, 3, 11]}, index=[1, 2, 3])
print(df)
# df_new = pd.melt(df)
# df_new = pd.melt(df).rename(columns={'variable': 'var', 'value': 'val'})
df_new = pd.melt(df).rename(columns={'variable': 'var', 'value': 'val'}).query('val > 5')
df_new = df.drop(columns=['수', '미세먼지'])
print(df_new)