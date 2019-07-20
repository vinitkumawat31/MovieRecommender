from knn import knn
import pandas as pd
import numpy as np

data = pd.read_csv("movies_data.csv").values
data = data[:,1:]
movie = [7.2, 1, 1, 0, 0, 0, 0, 1, 0]
ans = knn(data.tolist(),5,movie)
print(ans)