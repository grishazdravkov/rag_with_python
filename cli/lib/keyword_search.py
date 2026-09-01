import pickle
from .search_utils import load_movies, stop_words
import string
from nltk.stem import PorterStemmer
from collections import defaultdict
import os

stemmer = PorterStemmer()
STOP_WORDS = stop_words()


class InvertedIndex:
    def __init__(self) -> None:
        self.index = defaultdict(set)
        self.docmap = {}

    def __add_document(self, doc_id, text):
        tokens = tokenize_text(text)
        for token in tokens:
            self.index[token].add(doc_id)

    def get_documents(self, term):
        sorted_term =sorted(self.index[term])
        return sorted_term

    def build(self):
        movies = load_movies()
        for movie in movies:
            self.docmap[movie['id']] = movie
            self.__add_document(movie['id'], f"{movie['title']} {movie['description']}")

    def save(self):
        os.makedirs("cache", exist_ok=True)
        with open('cache/index.pkl', 'wb') as f:
            pickle.dump(self.index, f)

        with open('cache/docmap.pkl', 'wb') as f:
            pickle.dump(self.docmap, f)


def build_command():
    inv_index = InvertedIndex()
    inv_index.build()
    inv_index.save()
    docs = inv_index.get_documents("merida")
    print(f"First document for token 'merida' = {docs[0]}")


def search_command(query):
    movie_list = load_movies()
    empty_movies_list = []

    kept_tokens = tokenize_text(query)

    for movie in movie_list:
        # init empty list for kept titles
        kept_titles = tokenize_text(movie['title'])
        for q in kept_tokens:
            if any(q in title_word for title_word in kept_titles):
                empty_movies_list.append(movie)
                break
    return empty_movies_list[:5]


def tokenize_text(text: str) -> list[str]:
    query = text.translate(str.maketrans('', '', string.punctuation)).lower()
    split_query = query.split()
    kept_tokens = []
    for q_token in split_query:
        if q_token not in STOP_WORDS:
            kept_tokens.append(stemmer.stem(q_token))
    return kept_tokens
