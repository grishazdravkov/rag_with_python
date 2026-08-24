from .search_utils import load_movies


def search_command(query):
    movie_list = load_movies()
    empty_movies_list = []

    for movie in movie_list:
        if query in movie['title']:
            empty_movies_list.append(movie)

    return empty_movies_list[:5]





