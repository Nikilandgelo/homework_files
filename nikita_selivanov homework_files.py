import pprint
import os

def create_dictionary(list_file: list):
    cook_book = {}
    is_title = True
    for string_file in list_file:
        string_file = string_file.rstrip()
        if is_title == True:
            name_meal = string_file
            is_title = False
            is_number_ingredients = True
        elif is_number_ingredients == True:
            amount_ingredients = int(string_file)
            index_ingredients = amount_ingredients
            cook_book[name_meal] = [{'ingredient_name': '', 'quantity': '', 'measure': ''} for n in range(amount_ingredients)]
            is_number_ingredients = False
        elif string_file == "":
            is_title = True
        else:
            current_ingredient = string_file.split("|")
            cook_book.get(name_meal)[amount_ingredients - index_ingredients]["ingredient_name"] = current_ingredient[0]
            cook_book.get(name_meal)[amount_ingredients - index_ingredients]["quantity"] = current_ingredient[1]
            cook_book.get(name_meal)[amount_ingredients - index_ingredients]["measure"] = current_ingredient[2]
            index_ingredients -= 1
    return cook_book

def get_shop_list_by_dishes(dishes: list, persons: int):
    with open("recipes.txt", encoding = "utf-8") as recipes:
        dict_available_meals = create_dictionary(recipes.readlines())
        pprint.pprint(dict_available_meals, sort_dicts = False)
        print()
    shop_list = {}
    for dish in dishes:
        if dish in dict_available_meals:
            for ingredient in dict_available_meals.get(dish):
                if ingredient.get('ingredient_name') in shop_list:
                    shop_list[ingredient.get('ingredient_name')] = {'measure': ingredient.get('measure'),
                    'quantity': int(shop_list[ingredient.get('ingredient_name')].get('quantity')) + int(ingredient.get('quantity')) * persons}        
                else:
                    shop_list[ingredient.get('ingredient_name')] = {'measure': ingredient.get('measure'), 'quantity': int(ingredient.get('quantity')) * persons}
        else:
            print("Список заказываемых блюд неккоректен")
            return
    return shop_list

pprint.pprint(get_shop_list_by_dishes(["Салат крабовый", "Утка по-пекински"], 5), sort_dicts = False)
print()
get_shop_list_by_dishes(["Салат крабовый", "Утка по-пекински", "Шашлык"], 2)

def merge_files():
    list_all_files = []
    for files in os.listdir("files/"):
        with open("files/" + files, encoding = "utf-8") as text_file:
            counter_strings = 0
            while True:
                string_file = text_file.readline().rstrip()
                if string_file == "":
                    break
                counter_strings += 1
            text_file.seek(0,0)
            list_all_files.append([counter_strings, text_file, text_file.read()])
    list_all_files.sort()
    with open("result.txt", "w", encoding = "utf-8") as result_file:
        for write_file in list_all_files:
            result_file.write(write_file[1].name.split("/")[-1] + "\n")
            result_file.write(str(write_file[0]) + "\n")
            result_file.write(write_file[2] + "\n")
    
merge_files()