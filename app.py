from flask import Flask, request, render_template, jsonify
from src.components.model_builder import Recommender

# Initialize the Recommender
recommender = Recommender('data/df_new.csv')
recommender.build()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    if search:
        suggestions = recommender.df_new[recommender.df_new['original_title'].str.contains(search, case=False, na=False)]['original_title'].tolist()
    else:
        suggestions = []
    return jsonify(matching_results=suggestions)

@app.route('/recommend', methods=['POST'])
def recommend():
    title = request.form['title']
    recommendations = recommender.get_recommendations(title)
    if not recommendations:
        return jsonify(error=f"Movie '{title}' not found in the dataset. Please check the movie title and try again.")
    return jsonify(recommended=recommendations)

if __name__ == '__main__':
    app.run(debug=True)