books = [
    "Harry Potter magical wizard",
    "Dune desert politics future",
    "1984 dystopian surveillance control",
    "Hunger Games survival dystopian",
    "Lord of the Rings epic fantasy",
]


def similarity(query, text):
    return len(set(query.split()) & set(text.split()))


def perform_similarity_search(query, n_results):
    scored = []

    for book in books:
        score = similarity(query.lower(), book.lower())
        scored.append((score, book))

    scored.sort(reverse=True)

    return scored[:n_results]


def test_limits():
    query = "dystopian future survival"

    for n in [1, 3, 5, 10]:
        print(f"\n Top {n} Results:")

        results = perform_similarity_search(query, n)

        for score, book in results:
            print(f"{book} | score: {score}")


if __name__ == "__main__":
    test_limits()