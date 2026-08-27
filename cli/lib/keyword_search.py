from .search_utils import load_movies, stop_words
import string
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
STOP_WORDS = stop_words()


def search_command(query):
    movie_list = load_movies()
    empty_movies_list = []
    query = query.translate(str.maketrans('', '', string.punctuation)).lower()
    split_query = query.split()
    # init empty list for kept tokens in query
    kept_tokens = []

    # filtering the tokens that are not in stop words
    for q_token in split_query:
        if q_token not in STOP_WORDS:
            kept_tokens.append(stemmer.stem(q_token))

    for movie in movie_list:
        # init empty list for kept titles
        kept_titles = []
        # Remove punctuation from movie title and query
        movie_no_punct = movie['title'].translate(str.maketrans('', '', string.punctuation)).lower()
        title_tokens = movie_no_punct.split()

        for title_token in title_tokens:
            if title_token not in STOP_WORDS:
                kept_titles.append(title_token)

        for q in kept_tokens:
            if any(q in title_word for title_word in kept_titles):
                empty_movies_list.append(movie)
                break
    return empty_movies_list[:5]





