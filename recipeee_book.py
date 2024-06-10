class Recipe_book:
    def __init__(self,recipe_name,ingredients,cooking_methods):
        self.recipe_name = recipe_name
        self.ingredients = ingredients
        self.cooking_methods = cooking_methods
        
    def create_recipes(self):
        a = self.ingredients.split(',')
        with open(f'{self.recipe_name}.txt','a') as f:
            f.write(f'{self.recipe_name}\nINGREDIENTS :- \n ')
            for i in a:
                f.write(f'{i}\n')
            f.write(f'COOKING INSTRUCTIONS :- \n{self.cooking_methods}\n')
        with open(f'{self.recipe_name}.txt','r') as f:
            b=f.read()
            print(b)

    def search_recipes(self):
        with open (f'{self.recipe_name}.txt','r') as f:
            b=f.read()
            print(b)
            print('-------------------------')
            print()


i=1
recipes = []
recipe_count = []
while i >= 1:
    print('Recipe Book \n1. Create Recipes \n2. search Recipes \n3. Exit ')
    ch = [ 1 , 2 , 3 , 4 ]
    choice = int(input( 'Enter your choice (1/2/3/4) : ' ))
    
    if choice in ch:
        if choice == 1:
            print()
            recipe_name = input( 'Enter recipe name : ' )
            recipes.append(recipe_name)
            print()
            ingredients = input( 'Enter the ingredients (separate ingredients with comma) : ')
            cooking_methods = input ( 'Enter cooking instructions : ' )
            recipe_1 = Recipe_book(recipe_name,ingredients,cooking_methods)
            print()
            recipe_1.create_recipes()
        if choice == 2:
            print()
            print('------Recipe List------')
            for i in range(len(recipes)):
                recipe_count.append(i+1)
                print(f'{i+1}. {recipes[i]}')
            i=1
            while i>=1:
                recipe_num = int(input( 'Enter recipe choice from the above list : ' ))
                if recipe_num in recipe_count:
                    recipe_name = recipes[recipe_num-1]
                    print()
                    recipe_2 = Recipe_book(recipe_name,ingredients,cooking_methods)
                    recipe_2.search_recipes()
                    break
                else:
                    print('Enter Valid Choice ')

        elif choice == 3:
            print()
            exit()

    else:
        print('Enter Valid Choice ')
        print()








 
