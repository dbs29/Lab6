import json
from datetime import datetime, timedelta
import requests
import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean, cityblock, cosine
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Task(object):
    def __init__(self, data):
        self.df = pd.read_csv(data)

    def t1(self, name):
        return []

    def t2(self, name):
        return []
    
    def t3(self, name):
        return []
        
if __name__ == "__main__":
    # using the class movie ratings data we collected in http://data.cs1656.org/movie_class_responses.csv
    t = Task('http://data.cs1656.org/movie_class_responses.csv')
    print(t.t1('BabyKangaroo'))
    predicted_rating = 0.0
weights_sum = 0.0
ratings = df.iloc[0][1:-1]
for user in df.columns[1:-1]:
    if (not np.isnan(sim_weights[user])):
        predicted_rating += ratings[user] * sim_weights[user]
        weights_sum += sim_weights[user]

predicted_rating /= weights_sum
print ("predicted rating: %f" % predicted_rating)
    print('------------------------------------')
    print(t.t2('BabyKangaroo'))
    print('------------------------------------')
    print(t.t3('BabyKangaroo'))
    print('------------------------------------')
