from shared_functions import *


food_items = []


def main():
    """Main function for interactive CLI food recommendation system"""
    try:
        print("\n Interactive Food Recommendation System")
        print("=" * 50)
        print("Loading food database...")

        global food_items
        food_items = load_food_data('./FoodDataSet.json')

        print(f"\n Loaded {len(food_items)} food items successfully")

        
        collection = create_similarity_search_collection(
            "interactive_food_search",
            {'description': 'A collection for interactive food search'}
        )

        
        populate_similarity_collection(collection, food_items)

        interactive_food_chatbot(collection)

    except Exception as error:
        print(f"\n Error initializing system: {error}")


def interactive_food_chatbot(collection):
    """Interactive CLI chatbot for food recommendations"""

    print("\n" + "=" * 50)
    print(" INTERACTIVE FOOD SEARCH CHATBOT")
    print("=" * 50)

    print("Commands:")
    print("  • Type any food name or description to search")
    print("  • 'help' - Show available commands")
    print("  • 'quit' or 'exit' - Exit the system")
    print("  • Ctrl+C - Emergency exit")
    print("-" * 50)

    while True:
        try:
            user_input = input("\n🔍 Search for food: ").strip()

            if not user_input:
                print("   Please enter a search term or 'help'")
                continue

            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n Thank you for using the system. Goodbye!")
                break

            elif user_input.lower() in ['help', 'h']:
                show_help_menu()

            else:
                handle_food_search(collection, user_input)

        except KeyboardInterrupt:
            print("\n\n System interrupted. Goodbye!")
            break

        except Exception as e:
            print(f"\n Error processing request: {e}")


def show_help_menu():
    """Display help information"""

    print("\n HELP MENU")
    print("-" * 30)

    print("Search Examples:")
    print("  • 'chocolate dessert'")
    print("  • 'Italian food'")
    print("  • 'sweet treats'")
    print("  • 'baked goods'")
    print("  • 'low calorie'")

    print("\nCommands:")
    print("  • 'help' - Show this menu")
    print("  • 'quit' - Exit system")


def handle_food_search(collection, query):
    """Handle food similarity search"""

    print(f"\n🔍 Searching for '{query}'...")
    print("   Please wait...")

    results = perform_similarity_search(collection, query, 5)


    if not results:
        print("\n❌ No matching foods found.")
        print("\n💡 Try keywords like:")
        print("   • 'Italian', 'dessert', 'cheese'")
        return

    print(f"\n Found {len(results)} recommendations:")
    print("=" * 60)

    for i, result in enumerate(results, 1):
        percentage = result['similarity_score'] * 100

        print(f"\n{i}. 🍽 {result['food_name']}")
        print(f"    Match Score: {percentage:.1f}%")
        print(f"    Cuisine: {result['cuisine_type']}")
        print(f"    Calories: {result['food_calories_per_serving']}")
        print(f"    Description: {result['food_description']}")

        if i < len(results):
            print("   " + "-" * 50)

    print("=" * 60)

    suggest_related_searches(results)


def suggest_related_searches(results):
    """Suggest related searches"""

    print("\n You may also try:")
    seen = set()

    for r in results:
        cuisine = r['cuisine_type']
        if cuisine not in seen:
            print(f"   • {cuisine} food")
            seen.add(cuisine)

if __name__ == "__main__":
    main()