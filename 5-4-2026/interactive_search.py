search_history = []  

books = [
    {"title": "Harry Potter", "genre": "Fantasy"},
    {"title": "Dune", "genre": "Science Fiction"},
    {"title": "1984", "genre": "Dystopian"},
    {"title": "The Hunger Games", "genre": "Dystopian"},
]


def search_books(query):
    results = []
    for book in books:
        if query.lower() in book["title"].lower():
            results.append(book["title"])
    return results


def interactive():
    print("📚 Book Search System")
    print("Type 'history' to view searches, 'exit' to quit\n")

    while True:
        query = input("Search: ")

        if query == "exit":
            break

        elif query == "history":
            print("\n Search History:")
            for i, q in enumerate(search_history, 1):
                print(f"{i}. {q}")
            print()
            continue

        search_history.append(query)

        results = search_books(query)

        if results:
            print(" Results:")
            for r in results:
                print("-", r)
        else:
            print(" No results found")


if __name__ == "__main__":
    interactive()