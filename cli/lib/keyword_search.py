from .search_utils import load_movies
import string


def search_command(query):
    movie_list = load_movies()
    empty_movies_list = []

    for movie in movie_list:

        # Remove punctuation from movie title and query
        movie_no_punct = movie['title'].translate(str.maketrans('', '', string.punctuation))
        query = query.translate(str.maketrans('', '', string.punctuation))
        split_query = query.split()
        for q in split_query:
            if q.lower() in movie_no_punct.lower():
                empty_movies_list.append(movie)
    return empty_movies_list[:5]





