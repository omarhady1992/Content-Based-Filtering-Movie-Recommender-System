

#Data Preprocessor
# Description: This file is used to preprocess the dataset and save it in a clean format.
#!/usr/bin/env python
# coding: utf-8

# Load the libraries
import pandas as pd
import numpy as np
import ast
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import PorterStemmer

class Preprocessor:
    def __init__(self, movies_path, credits_path):
        self.movies_path = movies_path
        self.credits_path = credits_path
        self.df_movies = None
        self.df_credits = None
        self.df = None
        self.df_workable = None
        self.df_cbf = None

    def load_data(self):
        try:
            self.df_movies = pd.read_csv(self.movies_path)
            self.df_credits = pd.read_csv(self.credits_path)
        except Exception as e:
            print(f"Error reading the data: {e}")

    def merge_data(self):
        self.df = pd.merge(self.df_movies, self.df_credits, left_on='id', right_on='movie_id')
        print(self.df.shape)

    def preprocess(self):
        self.df_workable = self.df[['id', 'original_title', 'genres', 'keywords', 'cast', 'crew', 'overview', 'popularity', 'runtime', 'release_date']]
        self.df_workable = self.df_workable.dropna()

        # Extract director name from crew column
        self.df_workable['crew'] = self.df_workable['crew'].apply(ast.literal_eval)
        self.df_workable['director'] = self.df_workable['crew'].apply(self.get_director)
        self.df_workable = self.df_workable.drop('crew', axis=1)

        # Extract genres, keywords, and cast
        self.df_workable['genres'] = self.df_workable['genres'].apply(ast.literal_eval).apply(lambda x: [i['name'] for i in x])
        self.df_workable['keywords'] = self.df_workable['keywords'].apply(ast.literal_eval).apply(lambda x: [i['name'] for i in x])
        self.df_workable['cast'] = self.df_workable['cast'].apply(ast.literal_eval).apply(lambda x: [i['name'] for i in x])
        self.df_workable['cast'] = self.df_workable['cast'].apply(lambda x: [str.lower(i.replace(" ", "")) for i in x])

        # Remove spaces from the director name, genres, and keywords
        self.df_workable['director'] = self.df_workable['director'].astype('str').apply(lambda x: str.lower(x.replace(" ", "")))
        self.df_workable['director'] = self.df_workable['director'].apply(lambda x: [x])
        self.df_workable['genres'] = self.df_workable['genres'].apply(lambda x: [str.lower(i.replace(" ", "")) for i in x])
        self.df_workable['keywords'] = self.df_workable['keywords'].apply(lambda x: [str.lower(i.replace(" ", "")) for i in x])

        # Make overview column lower case and change to word list
        self.df_workable['overview'] = self.df_workable['overview'].apply(lambda x: str.lower(x).split())
        self.df_workable['original_title'] = self.df_workable['original_title'].apply(lambda x: str.lower(x))

        # Make a soup column
        self.df_workable['soup'] = self.df_workable['overview'] + self.df_workable['keywords'] + self.df_workable['cast'] + self.df_workable['director'] + self.df_workable['genres']
        self.df_workable['soup'] = self.df_workable['soup'].apply(lambda x: ' '.join(x))

        # Convert release_date to datetime
        self.df_workable['release_date'] = pd.to_datetime(self.df_workable['release_date'], errors='coerce')

        # Create a new dataframe for content-based filtering
        self.df_cbf = self.df_workable[['id', 'original_title', 'soup', 'popularity', 'runtime', 'release_date']]

        # Stemming and lemmatization
        stemmer = PorterStemmer()
        lemmatizer = WordNetLemmatizer()
        self.df_cbf['soup'] = self.df_cbf['soup'].apply(lambda x: ' '.join([stemmer.stem(i) for i in x.split()]))
        self.df_cbf['soup'] = self.df_cbf['soup'].apply(lambda x: ' '.join([lemmatizer.lemmatize(i) for i in x.split()]))

    def save_data(self, output_path):
        self.df_cbf.to_csv(output_path, index=False)

    @staticmethod
    def get_director(crew):
        for member in crew:
            if member['job'] == 'Director':
                return member['name']
        return np.nan

if __name__ == "__main__":
    preprocessor = Preprocessor('data/tmdb_5000_movies.csv', 'data/tmdb_5000_credits.csv')
    preprocessor.load_data()
    preprocessor.merge_data()
    preprocessor.preprocess()
    preprocessor.save_data('data/df_new.csv')