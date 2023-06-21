# Part 1: Nested Dictionaries

cookbook = {
   'Sandwish' : {
            'ingredients' : ["ham", "bread", "cheese", "tomatoes"],
            'meal'        : "lunch",
            'prep_time'   : 10
   },
   'Cake'     : {
            'ingredients' : ["flour", "sugar", "eggs"],
            'meal'        : "dessert",
            'prep_time'   : 60
    },
   'Salade'   : {
            'ingredients' : ["avocado", "arugula", "tomatoes", "spinach"],
            'meal'        : "lunch",
            'prep_time'   : 15
   }
}

# Part 2: A series of Helpful Fuctions

#1.function that print all recipe names
def printRecipeName(menu) :
    for recipeName in menu.keys():
        print(f'{recipeName}')

#2.function that takes a recipe name and print its details
def printRecipeDetails(recipeName, menu):
    for name in menu.keys() :
        if name == recipeName :
            print(f'Recipe for {recipeName} is')
            for key, details in menu[name].items() :
                print(f'{key} : {details}')

#3.function that takes a recipe name and delete it
def deleteRecipe(recipeName, menu):
    for name in menu.keys():
        if name == recipeName:
            recipeToDelete = name
            break
    del menu[recipeToDelete]

#4.function that add a recipe from uset input
def addRecipe(cookbook):
    name = input("Enter a name:\n")

    ingredients = []
    print("Enter ingredients:")
    while True :
        item = input()
        if(item == ""):
            break
        ingredients.append(item)
    
    mealType = input("Enter a meal type:\n")

    prepTime = input("Enter a preparation time:\n")
    
    while(not prepTime.isdigit()):
        print("\nyou should intput time as digits!\n")
        prepTime = input("Enter a preparation time:\n")
    
    prepTime = int(prepTime)
    
    newRecipe = {
        'ingredients' : ingredients,
        'meal'        : mealType,
        'prep_time'   : prepTime
    }
    
    cookbook[name] = newRecipe

def print_availble_list():
    print("List of availble option!\n\t1: Add a recipe\n\
    \t2: Delete a recipe\n\
    \t3: Print a recipe\n\
    \t4: Print the cookbook\n\
    \t5: Quit\n")

def switch(option):
    if option == "1":
        addRecipe(cookbook)
    elif option == "2":
        print("Please enter a recipe name you want to delete:")
        name = input(">> ")
        deleteRecipe(name ,cookbook)
    elif option == "3":
        print("Please enter a recipe name to get its detatls:")
        name = input(">> ")
        printRecipeDetails(name, cookbook)
    elif option == "4":
        printRecipeName(cookbook)
    elif option == "5":
        print("\nCookbook closed. Goodbye !")
        return ("Quit")

def run_cookbook(cookbook):
    print("Welcom to this Python Cookbook  !")
    print_availble_list()
    while True:
        print("Please select an option:")
        option = input(">> ")
        if (not option.isdigit() or (option.isdigit() and (int(option) > 5 or int(option) < 1))):
            print("\nSorry, this option does not exist.")
            print_availble_list()
        if (switch(option) == "Quit"):
            return 0

run_cookbook(cookbook)