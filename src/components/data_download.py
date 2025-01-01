import os
from kaggle.api.kaggle_api_extended import KaggleApi

class DataDownloader:
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name

    def download(self):
        # Set Kaggle API credentials
        os.environ['KAGGLE_USERNAME'] = 'omarionini'
        os.environ['KAGGLE_KEY'] = 'a6fdd13fa12a40e8bbb69afc883e2771'

        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files(self.dataset_name, path='data/', unzip=True)