from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
import numpy as np
import requests

app = FastAPI()

# Mount static files (CSS, JS, Images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Load data
try:
    similarity = np.load('similarity.npy', allow_pickle=False)
    df = pd.read_csv('movies_data.csv')
    titles = df["title"].tolist()
except FileNotFoundError:
    similarity = None
    titles = ["Error: movies_data.csv not found"]
except KeyError:
    titles = ["Error: 'title' column not found in CSV"]


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url)
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')

                   
@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "names": titles, "selected": None, "error": None, "movie_data": []}
    )


@app.post("/", response_class=HTMLResponse)
async def post_index(request: Request, name_dropdown: str = Form(...)):
    selected_name = None
    recommendations = []
    posters = []
    error = None

    if similarity is None:
        error = "Error loading similarity or data file."
    else:
        if name_dropdown in titles:
            top_k = 8
            selected_name = name_dropdown
            idx = titles.index(selected_name)
            sim_scores = similarity[idx]
            similar_indices = np.argpartition(sim_scores, -top_k)[-top_k:]
            similar_indices = similar_indices[np.argsort(sim_scores[similar_indices])[::-1]]
            # similar_indices = sim_scores.argsort()[::-1][1:9]  # Top 5
            recommendations = [titles[i] for i in similar_indices]

            for i in similar_indices:
                movie_id = df.iloc[i]['movie_id']
                poster = fetch_poster(movie_id)
                posters.append(poster)
        else:
            error = "Movie not found in dataset."

    movie_data = list(zip(posters or [], recommendations or []))
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "names": titles, "selected": selected_name, "error": error, "movie_data": movie_data}
    )
