import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df_new = None
        self.cosine_sim = None
        self.indices = None

    def load_data(self):
        self.df_new = pd.read_csv(self.data_path)

    def create_similarity_matrix(self):
        # Create the count matrix and cosine similarity matrix
        count = CountVectorizer(stop_words='english')
        count_matrix = count.fit_transform(self.df_new['soup'])
        self.cosine_sim = cosine_similarity(count_matrix, count_matrix)

        # Create a reverse map of indices and movie titles
        self.indices = pd.Series(self.df_new.index, index=self.df_new['original_title']).drop_duplicates()

    def get_recommendations(self, title):
        # Check if the title exists in the indices
        if title not in self.indices:
            return []

        # Get the index of the movie that matches the title
        idx = self.indices[title]

        # Get the pairwise similarity scores of all movies with that movie
        sim_scores = list(enumerate(self.cosine_sim[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar movies
        sim_scores = sim_scores[1:11]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top 10 most similar movies
        return self.df_new['original_title'].iloc[movie_indices].tolist()
    
    def build(self):
        self.load_data()
        self.create_similarity_matrix()
        

