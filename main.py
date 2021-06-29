from pprint import pprint
def open_file(file_name):
    cook_book = {}
    with open(file_name, "r", encoding="utf-8") as recipes_book:
        for line in recipes_book:
            ingredients_list = []
            i = int(recipes_book.readline())
            for ingredients in range(i):
                recipe_line = {}
                ing_list = recipes_book.readline().split('|')
                recipe_line['ingredient_name'] = ing_list[0]
                recipe_line['quantity'] = ing_list[1]
                recipe_line['measure'] = ing_list[2].strip('\n')
                ingredients_list.append(recipe_line)
            recipes_book.readline()
            cook_book[line.strip('\n')] = ingredients_list
    return cook_book


open_file("recipes.txt")
pprint(open_file("recipes.txt"))