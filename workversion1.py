import numpy as np
import pandas as pd
import warnings
import matplotlib
import matplotlib.pyplot as plt

Train_data=pd.read_csv('/home/zxx/competition/01data/used_car_train_20200313.csv', sep=' ')
TestA_data = pd.read_csv('/home/zxx/competition/01data/used_car_testA_20200313.csv', sep=' ')
print('train data shape:',Train_data.shape)
print('TestA_data shape:',TestA_data.shape)
print('train data info:',Train_data.info)
print('TestA_data info:',TestA_data.info)
