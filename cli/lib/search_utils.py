import json
import os
from pathlib import Path
import string


def load_movies():
    # Walk up to the base directory of the project
    root_path = Path(__file__).parent.parent.parent
    # Join the root directory where the data is stored
    movies_path = os.path.join(root_path, "data/movies.json")
    with open(movies_path) as file:
        movies = json.load(file)

    movies_list = movies['movies']
    return movies_list


def stop_words():
    stop_words_list = []
    root_path = Path(__file__).parent.parent.parent
    stopwords_path = os.path.join(root_path, "data/stopwords.txt")
    with open(stopwords_path) as file:
        stopwords = file.read().splitlines()

    for stopword in stopwords:
        new_word = stopword.translate(str.maketrans('', '', string.punctuation)).lower()
        stop_words_list.append(new_word)

    return stop_words_list

if __name__ == "__main__":
    #print(load_movies())
    print(stop_words())

