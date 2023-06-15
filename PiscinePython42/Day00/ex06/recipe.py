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

def printRecipeName(menu) :
    for recipeName in menu.keys():
        print(f'{recipeName}')

def printRecipeDetails(recipeName, menu):
    for name in menu.keys() :
        if name == recipeName :
            print(f'the details for {recipeName} is')
            for key, details in menu[name].items() :
                print(f'{key} : {details}')

def deleteRecipe(recipeName, menu):
    for name in menu.keys():
        if name == recipeName:
            recipeToDelete = name
            break
    del menu[recipeToDelete]

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

# # printRecipeDetails("Cake", cookbook)
# deleteRecipe("Cake", cookbook)
# printRecipeName(cookbook)
addRecipe(cookbook)
printRecipeName(cookbook)
printRecipeDetails("www",cookbook)