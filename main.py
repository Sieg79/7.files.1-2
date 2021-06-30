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

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = open_file("recipes.txt")
    shop_list_by_dishes = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            shop_list_line = {}
            shop_list_line['measure'] = ingredient['measure']
            shop_list_line['quantity'] = int(ingredient['quantity']) * person_count
            if ingredient['ingredient_name'] not in shop_list_by_dishes:
                shop_list_by_dishes[ingredient['ingredient_name']] = shop_list_line
            else:
                shop_list_by_dishes[ingredient['ingredient_name']]['quantity'] += shop_list_line['quantity']
    return shop_list_by_dishes


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Пюре'], 3))
