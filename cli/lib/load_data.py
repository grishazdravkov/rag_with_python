import json
import os
from pathlib import Path


def load_data() -> list:

    # Walk up to the base directory of the project
    root_path = Path(__file__).parent.parent.parent
    #Join the root directory where the data is stored
    movies_path = os.path.join(root_path, "data/movies.json")

    with open(movies_path) as file:
        movies = json.load(file)

    movies_list = movies['movies']
    movies_data = []

    for movie in movies_list:
        print(movie['title'])

