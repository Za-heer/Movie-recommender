# Movie Recommender System

## Overview

The Movie Recommender System is a Python-based application that recommends movies based on user input using content-based filtering. It leverages the TMDB 5000 Movie Dataset, utilizing movie metadata such as genres, keywords, cast, and crew to suggest similar movies. The system features allowing users to input a movie title and receive personalized recommendations.


## Features

Content-Based Recommendations: Suggests movies similar to the user’s input based on features like genres, keywords, cast, and crew.

TMDB 5000 Dataset: Uses a rich dataset from The Movie Database (TMDB) for robust recommendations.

Preprocessed Data: Combines and cleans movie metadata for efficient similarity calculations.



## Dataset

This project uses the TMDB 5000 Movie Dataset, which includes:

Movie titles, genres, keywords, overviews, cast, and crew.

Two CSV files: tmdb_5000_movies.csv and tmdb_5000_credits.csv.The dataset is included in the data/ folder as movies.csv and credits.csv.


## Requirements

To run this project, ensure you have the following installed:


Python 3.8 or higher

pip (Python package manager)

Dependencies listed in requirements.txt


## Installation

Follow these steps to set up the project locally:


## Clone the Repository:

git clone https://github.com/Za-heer/Movie-Recommender-System.git

cd Movie-Recommender-System



## Create a Virtual Environment (recommended):

python -m venv venv


## Activate it:


On Windows:venv\Scripts\activate


On macOS/Linux:source venv/bin/activate




## Install Dependencies:

pip install -r requirements.txt


Contents of requirements.txt:

numpy==1.26.4

pandas==2.2.2

scikit-learn==1.5.0

streamlit==1.36.0



## Prepare the Dataset:

Ensure movies.csv and credits.csv are in the data/ folder.

The notebook.ipynb preprocesses these files to create a pickled file (movie_list.pkl and similarity.pkl) used by the Streamlit app.



## Interact with the App:

Select or type a movie title in the input field.

Click the “Recommend” button to view a list of similar movies.



## Example:

Input: "Inception"

Output: A list of 5 recommended movies with similar characteristics (e.g., genres, cast, keywords).




## Project Structure

### Movie-Recommender-System/
├── data/                    # TMDB dataset

│   ├── movies.csv           # Movie metadata

│   ├── credits.csv          # Cast and crew data

│   ├── movie_list.pkl       # Preprocessed movie data

│   ├── similarity.pkl       # Precomputed similarity matrix

├── app.py                   # Streamlit web interface

├── notebook.ipynb           # Jupyter notebook for data preprocessing

├── requirements.txt         # Project dependencies

└── README.md                # Project documentation



## How It Works

Data Preprocessing (notebook.ipynb):

Merges movies.csv and credits.csv from the TMDB dataset.

Extracts features (e.g., genres, keywords, cast, crew) and combines them into a single text field.

Uses TF-IDF vectorization and cosine similarity to compute a similarity matrix.

Saves preprocessed data as movie_list.pkl and similarity.pkl.



## Recommendation Algorithm (app.py):

Loads preprocessed data and similarity matrix.

Uses content-based filtering with cosine similarity to find movies similar to the user’s input.




## Example Output

Selected Movie: The Dark Knight

### Recommended Movies:

1. The Dark Knight Rises
2. Batman Begins
3. Inception
4. The Prestige
5. Memento


## Customization


Add Features: Modify notebook.ipynb to include additional TMDB metadata (e.g., release year, director) in the recommendation process.

Change Algorithm: Update app.py to experiment with other similarity metrics or recommendation techniques.

Enhance UI: Customize the Streamlit interface in app.py to add visuals (e.g., movie posters) or additional user inputs.


## Contributing

Contributions are welcome! To contribute:


## Fork the repository.

Create a new branch (git checkout -b feature-branch).

Make your changes and commit (git commit -m "Add new feature").

Push to the branch (git push origin feature-branch).

Open a pull request.


## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments


TMDB 5000 Movie Dataset for providing the data.

Built with open-source libraries: pandas, scikit-learn.

Inspired by content-based recommendation system tutorials.


## Contact

For questions or suggestions, open an issue on GitHub or contact mydocument783@gmail.com.

