import numpy as np

"""
This file contains utility functions for data processing. 
Adapt as needed.

Author: Nicolas
Date: [current date]

"""


if __name__ == '__main__':
    train_data_outputs = np.load('train_data_outputs_20240302.npy')
    train_data_outputs_1 = np.load('train_data_outputs1.npy')
    train_data_outputs_2 = np.load('train_data_outputs2.npy')
    train_data_outputs_3 = np.load('train_data_outputs3.npy')
    train_data_outputs_4 = np.load('train_data_outputs4.npy')
    
    train_data_outputs_result = np.append(train_data_outputs, train_data_outputs_1)
    train_data_outputs_result = np.append(train_data_outputs_result, train_data_outputs_2)
    train_data_outputs_result = np.append(train_data_outputs_result, train_data_outputs_3)
    train_data_outputs_result = np.append(train_data_outputs_result, train_data_outputs_4)
    np.save('train_data_outputs_result', train_data_outputs_result)
    
    train_data_screens = np.load('train_data_screens_20240302.npy')
    train_data_screens_1 = np.load('train_data_screens1.npy')
    train_data_screens_2 = np.load('train_data_screens2.npy')
    train_data_screens_3 = np.load('train_data_screens3.npy')
    train_data_screens_4 = np.load('train_data_screens4.npy')
    train_data_screens_result = np.append(train_data_screens, train_data_screens_1)
    train_data_screens_result = np.append(train_data_screens_result, train_data_screens_2)
    train_data_screens_result = np.append(train_data_screens_result, train_data_screens_3)
    train_data_screens_result = np.append(train_data_screens_result, train_data_screens_4)
    np.save('train_data_screens_result', train_data_screens_result)