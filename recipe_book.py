class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeBook:   
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def find_recipe(self, keyword):
        found_recipes = []
        for recipe in self.recipes:
            if keyword.lower() in recipe.name.lower():
                found_recipes.append(recipe)
        return found_recipes

def create_recipe():
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    instructions = input("Enter instructions: ")
    return Recipe(name, ingredients, instructions)

def main():
    recipe_book = RecipeBook()

    while True:
        print("\n1. Add Recipe")
        print("2. Search Recipe")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            recipe = create_recipe()
            recipe_book.add_recipe(recipe)
            print("Recipe added successfully!")

        elif choice == "2":
            keyword = input("Enter keyword to search for recipes: ")
            found_recipes = recipe_book.find_recipe(keyword)
            if found_recipes:
                print("\nFound recipes:")
                for idx, recipe in enumerate(found_recipes, start=1):
                    print(f"{idx}. {recipe.name}")
                recipe_choice = input("Select a recipe number to view details (or press Enter to go back): ")
                if recipe_choice:
                    try:
                        selected_recipe = found_recipes[int(recipe_choice) - 1]
                        print(f"\n{selected_recipe.name}\n")
                        print("Ingredients:")
                        for ingredient in selected_recipe.ingredients:
                            print("- " + ingredient.strip())
                        print("\nInstructions:")
                        print(selected_recipe.instructions)
                    except (ValueError, IndexError):
                        print("Invalid selection.")

            else:
                print("No recipes found.")

        elif choice == "3":
            print("Exiting the recipe book.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
