from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import requests

app = Flask(__name__)

try:
    similarity = np.load('similarity.npy', allow_pickle=False)
    df = pd.read_csv('movies_data.csv')
    titles = df["title"].tolist()
except FileNotFoundError:
    similarity = None
    titles = ["Error: movies_data.csv not found"]
except KeyError:
    titles = ["Error: 'title' column not found in CSV"]

@app.route('/', methods=['GET', 'POST'])
def index():
    def fetch_poster(movie_id):
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        response = requests.get(url)
        data = response.json()
        return "http://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')

    if similarity is None:
        return render_template('index.html', names=titles, selected=None, recommendations=["Error loading files"])

    selected_name = None
    recommendations = []
    posters = []

    if request.method == 'POST':
        selected_name = request.form.get('name_dropdown', '')
        if selected_name in titles:
            idx = titles.index(selected_name)
            sim_scores = similarity[idx]
            similar_indices = sim_scores.argsort()[::-1][1:6]  # Top 5
            recommendations = [titles[i] for i in similar_indices]
            print(f"Recommendations for {selected_name}: {recommendations}")  # Debug

            for i in similar_indices:
                movie_id = df.iloc[i]['movie_id']
                poster = fetch_poster(movie_id)
                posters.append(poster)
        else:
            recommendations = ["Movie not found in the dataset."]
    else:
        recommendations = ["Select a movie to see recommendations."]

    movie_data = list(zip(posters or [], recommendations or []))
    print(f"Movie data: {movie_data}")  # Debug
    return render_template('index.html', names=titles, selected=selected_name, recommendations=recommendations, posters=posters, movie_data=movie_data)
        
    

    

if __name__ == '__main__':
    app.run(debug=True)