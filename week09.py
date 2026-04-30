import numpy as np
import pandas as pd

arr2d = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)

df_dict = pd.DataFrame(arr2d, columns=['a','b','c'],index=[1,2,3])
print(df_dict)
print(arr2d)