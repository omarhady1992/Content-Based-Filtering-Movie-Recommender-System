# Recommender System

This project is a machine learning-based recommender system that uses content-based filtering to suggest items to users.

## Steps to Run the Project

1. **Install Requirements and Create Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

2. **Run `main.py`**
    - This script will download the data, preprocess it, and create the model.
    ```bash
    python main.py
    ```

3. **Run `app.py`**
    - This script will start the application.
    ```bash
    python app.py
    ```

## Content-Based Filtering

Content-based filtering is a recommendation technique that uses the features of items to recommend similar items to users. It relies on the idea that if a user likes an item, they will also like items that are similar to it.

## Data

The dataset used in this project contains information about 5000 movies from the tmdb kaggle dataset their features. This data is essential for training the content-based filtering model.

## Code Explanation

- `main.py`: This script handles the downloading, preprocessing of data, and creation of the recommendation model.
- `app.py`: This script starts the application, allowing users to interact with the recommender system.

## Project Structure

The project is organized into the following files:

- `requirements.txt`: Contains the list of dependencies required to run the project.
- `main.py`: Script to download, preprocess data, and create the recommendation model.
- `app.py`: Script to start the application.
- `data/`: Directory to store the dataset.
- `src/components`: Directory of the three components
- `src/components/data_download.py`: contains the data downloading component using kaggle api
- `src/components/data_preprocess.py`: contains the data preprocessing component (feature selection and engineering)
-`src/components/model_builder.py`: contains the data model component (cosine similarity matrix builder and recommendation fetching function)

-`templates/index.html`: simple front-end for the web app
     

## Data

The dataset used in this project is the TMDB 5000 Movies Dataset. It contains information about 5000 movies, including features such as genres, cast, crew, keywords, and more. This data is used to train the content-based filtering model.

## Content-Based Filtering

Content-based filtering is a recommendation technique that uses the features of items to recommend similar items to users. It relies on the idea that if a user likes an item, they will also like items that are similar to it. In this project, the features of movies are used to recommend similar movies to users.