# import matplotlib.pyplot as plt
# import numpy as np
#
#
# # Creating dataset
# np.random.seed(10)
# data = np.random.normal(100, 20, 200)
# print(data)
# fig = plt.figure(figsize =(10, 7))
#
# # Creating plot
# plt.boxplot(data)
#
# # show plot
# plt.show()

import pandas as pd
import numpy as np

#initialize a dataframe
df = pd.DataFrame(
	[[21, 72, 67.1],
	[23, 78, 69.5],
	[32, 74, 56.6],
	[52, 54,]],
	columns=['a', 'b', 'c'])

isempty = np.where(df)
print('Is the DataFrame empty :', isempty)
