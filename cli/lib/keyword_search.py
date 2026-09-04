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

    def load(self):
        with open('cache/index.pkl', 'rb') as f:
            self.index = pickle.load(f)

        with open('cache/docmap.pkl', 'rb') as f:
            self.docmap = pickle.load(f)


def build_command():
    inv_index = InvertedIndex()
    inv_index.build()
    inv_index.save()
    docs = inv_index.get_documents("")
    print(f"First document for token 'merida' = {docs[0]}")


def search_command(query):
    try:
        inv_index = InvertedIndex()
        inv_index.load()
    except FileNotFoundError as e:
        print(f"Error while loading inverted index: {e}")
        exit(1)

    results = []
    kept_tokens = tokenize_text(query)
    seen_ids = set()

    for token in kept_tokens:
        document_id = inv_index.get_documents(token)
        for doc in document_id:
            if doc not in seen_ids:
                seen_ids.add(doc)
                results.append(inv_index.docmap[doc])
                if len(results) == 5:
                    return results
    return results



def tokenize_text(text: str) -> list[str]:
    query = text.translate(str.maketrans('', '', string.punctuation)).lower()
    split_query = query.split()
    kept_tokens = []
    for q_token in split_query:
        if q_token not in STOP_WORDS:
            kept_tokens.append(stemmer.stem(q_token))
    return kept_tokens
