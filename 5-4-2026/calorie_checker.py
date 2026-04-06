foods = [
    {"name": "Apple", "calories": 95},
    {"name": "Burger", "calories": 354},
    {"name": "Pizza", "calories": 285},
    {"name": "Salad", "calories": 150},
    {"name": "Chocolate", "calories": 230},
]


def calorie_checker():
    print(" Calorie Checker")

    budget = int(input("Enter your calorie budget: "))

    while True:
        query = input("\nSearch food (or 'exit'): ")

        if query == "exit":
            break

        found = False

        for food in foods:
            if query.lower() in food["name"].lower():
                found = True
                if food["calories"] <= budget:
                    print(f" {food['name']} fits your budget ({food['calories']} cal)")
                else:
                    print(f" {food['name']} exceeds budget ({food['calories']} cal)")

        if not found:
            print(" Food not found")


if __name__ == "__main__":
    calorie_checker()