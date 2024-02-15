# Importing the required libraries
import warnings
warnings.filterwarnings('ignore')
import os
import requests
import zipfile
import pandas as pd
import numpy as np

# ----------------- Defining the helper function -----------------
def read_data(file_path):
    '''
    This function reads the data from the file and returns the data in a dataframe

    Args:
    file_path: path of the file to be read

    Returns:
    data: dataframe of the data
    '''
    # Creating a header for the dataset
    cols = []

    # reading text file
    with open('OpportunityUCIDataset/dataset/column_names.txt') as f:
        text = f.readlines()

    for i in range(2,245):
        temp = text[i].split(';')[0].split(':')[1].strip()
        # remove the number from start
        temp = temp.split(' ')[1:]
        temp = ' '.join(temp)
        cols.append(temp)

    for i in range(248,255):
        cols.append(text[i].split(':')[1].strip().split(' ')[1])

    # reading a '.dat' file
    data = pd.read_csv(f'OpportunityUCIDataset/dataset/{file_path}', header=None)

    # split each row by space and then store in separate columns
    data = data[0].str.split(' ', expand=True)

    # assign column names
    data.columns = cols

    return data

def main():
    '''
    This function does the following things:
    - It downloads the data from source
    - It extracts the data
    - It stores the data in the data folder
    - It then creates a csv file from the dataa that picks the appropriate required data and discards the rest, this datasete is then used further for analysis.

    Args:
    None

    Returns:
    None
    '''
    # Checking if zip file already exists
    if os.path.exists('opportunity+activity+recognition.zip'):
        print('File already exists')
    else:
        # Downloading the zip file
        print('File does not exist, downloading the file')
        url = 'https://archive.ics.uci.edu/static/public/226/opportunity+activity+recognition.zip'
        # using wget to download the file
        os.system('wget ' + url)

    # unzipping the file
    print('Unzipping the file')
    # deleting the folder if it already exists
    if os.path.exists('OpportunityUCIDataset'):
        os.system('rm -r OpportunityUCIDataset')
        
    with zipfile.ZipFile('opportunity+activity+recognition.zip', 'r') as zip_ref:
        zip_ref.extractall('')

    # ----------------- Now reading the dataset -----------------
    # list all files in the OpportunityUCIDataset/dataset with .dat extension, this is so that I can only get files that can be passed to the function.
    files = os.listdir('OpportunityUCIDataset/dataset')
    files = [f for f in files if f.endswith('.dat')]

    # create dataset folder if not exists
    if not os.path.exists('dataset'):
        os.makedirs('dataset')

    for i in range(len(files)):
        data = read_data(files[i])
        f = files[i].split('.')[0]
        data.to_csv(f'dataset/{f}.csv', index=False)
        print(f'{f}.csv has been created successfully.')

# ----------------- Running the main function -----------------
if __name__ == '__main__':
    # waiting for the user to press any key
    input('Press any key to start the process')
    main()