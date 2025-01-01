#this is the project initiation file

def main():

    '''
    # Download dataset
    from src.components.data_download import DataDownloader
    downloader = DataDownloader("tmdb-movie-metadata")
    downloader.download()
    '''

    # Preprocess data
    from src.components.data_preprocess import Preprocessor
    preprocessor = Preprocessor('data/tmdb_5000_movies.csv', 'data/tmdb_5000_credits.csv')
    preprocessor.preprocess()
    preprocessor.save_data('data/df_new.csv')


    # Build model
    #from src.components.model_builder import Recommender
    #model_builder = Recommender('data/df_new.csv')
    #model_builder.build()


main()

