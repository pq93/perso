import numpy as np
import pandas as pd

data = pd.DataFrame(data = np.zeros((2,1), dtype = 'int32'),index=1+np.arange(2),columns=['Title'])
print(data)
