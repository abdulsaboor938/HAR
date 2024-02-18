# importing the libraries
import numpy as np
import pandas as pd

def main():
    # function that takes file name as input and returns a processed dataframe
    def process_file(file):
        data = pd.read_csv(file)

        # Selecting the actual required columns for further processing
        # Selecting the actual required columns for further processing
        data = data[[
            'InertialMeasurementUnit RUA accX', 'InertialMeasurementUnit RUA accY', 'InertialMeasurementUnit RUA accZ',
            'InertialMeasurementUnit RUA gyroX', 'InertialMeasurementUnit RUA gyroY', 'InertialMeasurementUnit RUA gyroZ',
            'InertialMeasurementUnit RUA magneticX', 'InertialMeasurementUnit RUA magneticY', 'InertialMeasurementUnit RUA magneticZ',
            'InertialMeasurementUnit RUA Quaternion1', 'InertialMeasurementUnit RUA Quaternion2', 'InertialMeasurementUnit RUA Quaternion3', 'InertialMeasurementUnit RUA Quaternion4', 
            'InertialMeasurementUnit RLA accX', 'InertialMeasurementUnit RLA accY', 'InertialMeasurementUnit RLA accZ', 
            'InertialMeasurementUnit RLA gyroX', 'InertialMeasurementUnit RLA gyroY', 'InertialMeasurementUnit RLA gyroZ',
            'InertialMeasurementUnit RLA magneticX', 'InertialMeasurementUnit RLA magneticY', 'InertialMeasurementUnit RLA magneticZ', 
            'InertialMeasurementUnit RLA Quaternion1', 'InertialMeasurementUnit RLA Quaternion2', 'InertialMeasurementUnit RLA Quaternion3', 'InertialMeasurementUnit RLA Quaternion4',
            'InertialMeasurementUnit LUA accX', 'InertialMeasurementUnit LUA accY', 'InertialMeasurementUnit LUA accZ',
            'InertialMeasurementUnit LUA gyroX', 'InertialMeasurementUnit LUA gyroY', 'InertialMeasurementUnit LUA gyroZ',
            'InertialMeasurementUnit LUA magneticX', 'InertialMeasurementUnit LUA magneticY', 'InertialMeasurementUnit LUA magneticZ',
            'InertialMeasurementUnit LUA Quaternion1', 'InertialMeasurementUnit LUA Quaternion2', 'InertialMeasurementUnit LUA Quaternion3', 'InertialMeasurementUnit LUA Quaternion4', 'InertialMeasurementUnit LLA accX', 'InertialMeasurementUnit LLA accY', 'InertialMeasurementUnit LLA accZ', 'InertialMeasurementUnit LLA gyroX', 'InertialMeasurementUnit LLA gyroY', 'InertialMeasurementUnit LLA gyroZ', 'InertialMeasurementUnit LLA magneticX', 'InertialMeasurementUnit LLA magneticY', 'InertialMeasurementUnit LLA magneticZ', 'InertialMeasurementUnit LLA Quaternion1', 'InertialMeasurementUnit LLA Quaternion2', 'InertialMeasurementUnit LLA Quaternion3', 'InertialMeasurementUnit LLA Quaternion4',
            'Accelerometer DOOR1 accX', 'Accelerometer DOOR1 accY', 'Accelerometer DOOR1 accZ',
            'Accelerometer DOOR2 accX', 'Accelerometer DOOR2 accY', 'Accelerometer DOOR2 accZ',
            'Locomotion', 'LL_Left_Arm_Object', 'LL_Right_Arm_Object', 'ML_Both_Arms'
            ]]
        
        # Drop rows where 'LL_Left_Arm', 'LL_Left_Arm_Object', 'LL_Right_Arm', 'LL_Right_Arm_Object', 'ML_Both_Arms' are all 0
        # data = data[(data['LL_Left_Arm_Object'] != 0) | (data['LL_Right_Arm_Object'] != 0) | (data['ML_Both_Arms'] != 0)]

        # drop rows where 'Locomotion' is 0
        data = data[data['Locomotion'] != 0]

        # drop the rows with missing values
        data = data.dropna()

        # drop rows that contain unwanted records in 'ML_Both_Arms'
        data = data[~data['LL_Left_Arm_Object'].isin([301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 318, 319, 320, 321, 322, 323])]

        # drop rows that contain unwanted records in 'ML_Both_Arms'
        data = data[~data['LL_Right_Arm_Object'].isin([501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 518, 519, 520, 521, 522, 523])]

        # drop rows that contain unwanted records in 'ML_Both_Arms'
        data = data[~data['ML_Both_Arms'].isin([406520, 404520, 406505, 404505, 406519, 404519, 406511, 404511, 406508, 404508, 408512, 407521, 405506])]

        return data

    # creating a dataset by combinig all files

    # list all files in dataset folder
    import os
    import glob
    import pandas as pd
    file_names = os.listdir('dataset')

    # creating a training and testing dataset
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0

    for file in file_names:
        # process the file
        data = process_file('dataset/' + file)
        # append the data to the csv file according to file name
        # list unique values in 'Locomotion' column
        print(data['Locomotion'].unique(), end = ' ')
        if file.split('-')[0] == 'S1':
            if one == 0:
                data.to_csv('S1.csv', index=False)
                one = 1
            else:
                data.to_csv('S1.csv', mode='a', header=False, index=False)
        elif file.split('-')[0] == 'S2':
            if two == 0:
                data.to_csv('S2.csv', index=False)
                two = 1
            else:
                data.to_csv('S2.csv', mode='a', header=False, index=False)
        elif file.split('-')[0] == 'S3':
            if three == 0:
                data.to_csv('S3.csv', index=False)
                three = 1
            else:
                data.to_csv('S3.csv', mode='a', header=False, index=False)
        elif file.split('-')[0] == 'S4':
            if four == 0:
                data.to_csv('S4.csv', index=False)
                four = 1
            else:
                data.to_csv('S4.csv', mode='a', header=False, index=False)
        print(file, 'processed')

    # reading the dataset and creating a copy of the dataset, which is then used to create non-ambient dataset
    one = pd.read_csv('S1.csv')
    onen=one.copy()
    one['Locomotion'] = one[['Locomotion', 'ML_Both_Arms']].max(axis=1)
    one.drop(['LL_Left_Arm_Object', 'LL_Right_Arm_Object', 'ML_Both_Arms'], axis=1, inplace=True)
    onen.drop(['LL_Left_Arm_Object', 'LL_Right_Arm_Object', 'ML_Both_Arms'], axis=1, inplace=True)

    two = pd.read_csv('S2.csv')
    twon=two.copy()
    two['Locomotion'] = two[['Locomotion', 'ML_Both_Arms']].max(axis=1)
    two.drop(['LL_Left_Arm_Object', 'LL_Right_Arm_Object', 'ML_Both_Arms'], axis=1, inplace=True)
    twon.drop(['LL_Left_Arm_Object', 'LL_Right_Arm_Object', 'ML_Both_Arms'], axis=1, inplace=True)

    three = pd.read_csv('S3.csv')
    threen=three.copy()
    three['Locomotion'] = three[['Locomotion', 'ML_Both_Arms']].max(axis=1)
    three.drop(['LL_Left_Arm_Object', 'LL_Right_Arm_Object', 'ML_Both_Arms'], axis=1, inplace=True)
    threen.drop(['LL_Left_Arm_Object', 'LL_Right_Arm_Object', 'ML_Both_Arms'], axis=1, inplace=True)

    four = pd.read_csv('S4.csv')
    fourn=four.copy()
    four['Locomotion'] = four[['Locomotion', 'ML_Both_Arms']].max(axis=1)
    four.drop(['LL_Left_Arm_Object', 'LL_Right_Arm_Object', 'ML_Both_Arms'], axis=1, inplace=True)
    fourn.drop(['LL_Left_Arm_Object', 'LL_Right_Arm_Object', 'ML_Both_Arms'], axis=1, inplace=True)

    train = pd.concat([twon, threen, fourn])
    train['Locomotion'] = train['Locomotion'].replace([1, 2, 5, 4], [1, 2, 5, 4])

    train_a = pd.concat([two, three, four])
    train_a['Locomotion'] = train_a['Locomotion'].replace([406516, 406517, 404516, 404517], [6, 7, 8, 9])
    test = one
    test['Locomotion'] = test['Locomotion'].replace([406516, 406517, 404516, 404517], [6, 7, 8, 9])

    train.to_csv('train-n.csv', index=False)
    train_a.to_csv('train-a.csv', index=False)
    test.to_csv('test.csv', index=False)

if __name__ == "__main__":
    main()