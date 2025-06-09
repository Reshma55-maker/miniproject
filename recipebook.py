#using file handling-
#1.recipe book 

recipes = []  
def load_recipes():
    file = open("recipe_book.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        parts = line.split("|")
        if len(parts) == 3:
            name = parts[0][:-1] if parts[0].endswith("\n") else parts[0]
            ingredients = parts[1].split(",")
            instructions = parts[2]
            if instructions.endswith("\n"):
                instructions = instructions[:-1]
            recipe = {
                "name": name,
                "ingredients": ingredients,
                "instructions": instructions
            }
            recipes.append(recipe)

def save_all_recipes():
    file = open("recipe_book.txt", "w")
    for r in recipes:
        file.write(r["name"] + "|" + ",".join(r["ingredients"]) + "|" + r["instructions"] + "\n")
    file.close()


def add_recipe():
    global recipes
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(",")
    instructions = input("Enter instructions: ")
    recipe = {
        "name": name,
        "ingredients": ingredients,
        "instructions": instructions
    }
    recipes.append(recipe)
    save_all_recipes()
    print("✅ Recipe added.")

def view_recipes():
    if len(recipes) == 0:
        print("No recipes found.")
    else:
        print("\n📚 Recipe List:")
        index = 1
        for r in recipes:
            print(str(index) + ". " + r["name"])
            index += 1

def view_instructions():
    name = input("Enter recipe name to view: ")
    found = False
    for r in recipes:
        if r["name"].lower() == name.lower():
            print("\n📋 " + r["name"])
            print("Ingredients: " + ", ".join(r["ingredients"]))
            print("Instructions: " + r["instructions"])
            found = True
    if not found:
        print("❌ Recipe not found.")


def delete_recipe():
    name = input("Enter recipe name to delete: ")
    for r in recipes:
        if r["name"].lower() == name.lower():
            recipes.remove(r)
            save_all_recipes()
            print("🗑️ Recipe deleted.")
            return
    print("❌ Recipe not found.")

load_recipes()

while True:
    print("\n📘 Recipe Book Menu:")
    print("1. Add Recipe")
    print("2. View All Recipes")
    print("3. View Recipe Instructions")
    print("4. Delete a Recipe")
    print("5. Exit")

    option = input("Choose an option (1-5): ")

    if option == "1":
        add_recipe()
    elif option == "2":
        view_recipes()
    elif option == "3":
        view_instructions()
    elif option == "4":
        delete_recipe()
    elif option == "5":
        print("👋 Goodbye!")
        break
    else:
        print("❗ Please enter a number from 1 to 5.")

#4.hangman game.