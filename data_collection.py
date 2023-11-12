import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize the Kaggle API
api = KaggleApi()
api.authenticate()

# Define the username and name of the dataset you want to download
# dataset_username = 'clmentbisaillon'
# dataset_name = 'fake-and-real-news-dataset'
dataset_username = 'hassanamin'
dataset_name = 'textdb3'

# Download the dataset
api.dataset_download_files(f'{dataset_username}/{dataset_name}', path='./data/', unzip=True)