from typing import List, Dict

# DATA
books = [
    {
        "id": "book_1",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "year": 1925,
        "rating": 4.1,
        "pages": 180,
        "description": "A tragic tale of wealth, love, and the American Dream in the Jazz Age",
        "themes": "wealth, corruption, American Dream, social class",
        "setting": "New York, 1920s"
    },
    {
        "id": "book_2",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "year": 1960,
        "rating": 4.3,
        "pages": 376,
        "description": "A powerful story of racial injustice and moral growth in the American South",
        "themes": "racism, justice, moral courage, childhood innocence",
        "setting": "Alabama, 1930s"
    },
    {
        "id": "book_3",
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "year": 1949,
        "rating": 4.4,
        "pages": 328,
        "description": "A chilling vision of totalitarian control and surveillance society",
        "themes": "totalitarianism, surveillance, freedom, truth",
        "setting": "Oceania, dystopian future"
    },
    {
        "id": "book_4",
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "year": 1997,
        "rating": 4.5,
        "pages": 223,
        "description": "A young wizard discovers his magical heritage and begins his education at Hogwarts",
        "themes": "friendship, courage, good vs evil, coming of age",
        "setting": "England, magical world"
    },
    {
        "id": "book_5",
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "year": 1954,
        "rating": 4.5,
        "pages": 1216,
        "description": "An epic fantasy quest to destroy a powerful ring and save Middle-earth",
        "themes": "heroism, friendship, good vs evil, power corruption",
        "setting": "Middle-earth, fantasy realm"
    },
    {
        "id": "book_6",
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "genre": "Science Fiction",
        "year": 1979,
        "rating": 4.2,
        "pages": 224,
        "description": "A humorous space adventure following Arthur Dent across the galaxy",
        "themes": "absurdity, technology, existence, humor",
        "setting": "Space, various planets"
    },
    {
        "id": "book_7",
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Science Fiction",
        "year": 1965,
        "rating": 4.3,
        "pages": 688,
        "description": "A complex tale of politics, religion, and ecology on a desert planet",
        "themes": "power, ecology, religion, politics",
        "setting": "Arrakis, distant future"
    },
    {
        "id": "book_8",
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "genre": "Dystopian",
        "year": 2008,
        "rating": 4.2,
        "pages": 374,
        "description": "A teenage girl fights for survival in a brutal televised competition",
        "themes": "survival, oppression, sacrifice, rebellion",
        "setting": "Panem, dystopian future"
    }
]


# CREATE DOC

def create_documents(books: List[Dict]) -> List[Dict]:
    docs = []
    for book in books:
        text = f"{book['title']} {book['description']} {book['themes']} {book['setting']}"
        docs.append({
            "id": book["id"],
            "text": text.lower(),
            "metadata": book
        })
    return docs


documents = create_documents(books)



# SIMILARITY FUNC

def simple_similarity(query: str, text: str) -> int:
    query_words = set(query.lower().split())
    text_words = set(text.split())
    return len(query_words & text_words)


def similarity_search(query: str, docs: List[Dict], top_k=3):
    results = []
    for doc in docs:
        score = simple_similarity(query, doc["text"])
        results.append((score, doc))

    results.sort(reverse=True, key=lambda x: x[0])
    return results[:top_k]

#METADATA FILTER

def filter_books(docs, genre=None, min_rating=None):
    filtered = []
    for doc in docs:
        book = doc["metadata"]

        if genre and book["genre"] not in genre:
            continue

        if min_rating and book["rating"] < min_rating:
            continue

        filtered.append(doc)

    return filtered

# ADVANCED SEARCH

def advanced_search():
    print("\n 1. Similarity Search: 'magical fantasy adventure'")
    results = similarity_search("magical fantasy adventure", documents)
    for score, res in results:
        print(res["metadata"]["title"], "| score:", score)

    print("\n 2. Filter: Fantasy or Science Fiction")
    filtered = filter_books(documents, genre=["Fantasy", "Science Fiction"])
    for doc in filtered:
        print(doc["metadata"]["title"])

    print("\n 3. Filter: Rating >= 4.0")
    filtered = filter_books(documents, min_rating=4.0)
    for doc in filtered:
        print(doc["metadata"]["title"])

    print("\n 4. Combined Search: Dystopian + High Rating + Similarity")
    filtered = filter_books(documents, genre=["Dystopian"], min_rating=4.0)
    results = similarity_search("survival dystopian rebellion", filtered)

    for score, res in results:
        print(res["metadata"]["title"], "| score:", score)


if __name__ == "__main__":
    advanced_search()