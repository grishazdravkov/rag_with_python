import json
import os
from pathlib import Path


def load_movies():
    # Walk up to the base directory of the project
    root_path = Path(__file__).parent.parent.parent
    # Join the root directory where the data is stored
    movies_path = os.path.join(root_path, "data/movies.json")
    with open(movies_path) as file:
        movies = json.load(file)

    movies_list = movies['movies']
    return movies_list


if __name__ == "__main__":
    print(load_movies())

