
from gettext import find
from typing import ItemsView
import re
from bs4 import BeautifulSoup
import requests
from google_sheet_1 import records_data



def get_cr_menu():
    '''
    This gets the menu from CR
    :return:
        A list of dictionaries
        a list of the items from the dining hall. Each item is a string
    '''
    import json

    url = "https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    source = doc.prettify()

    m = re.search("model: ({.*})", source)
    model = m.group(1)
    json = json.loads(model)

    todays_food_items = []

    for item in range(0, len(json['Menu']['MenuProducts'])):
        data = json['Menu']['MenuProducts'][item]['Product']
        item_dict = {'name': data['MarketingName'], 'ContainsEggs': data['ContainsEggs'], 'ContainsFish': data['ContainsFish'], 'ContainsMilk': data['ContainsMilk'], 'ContainsPeanuts': data['ContainsPeanuts'], 'ContainsShellfish': data['ContainsShellfish'],
                     'ContainsSoy': data['ContainsSoy'], 'ContainsTreeNuts': data['ContainsTreeNuts'], 'ContainsWheat': data['ContainsWheat'], 'IsGlutenFree': data['IsGlutenFree'], 'IsHalal': data['IsHalal'], 'IsVegan': data['IsVegan'], 'IsVegetarian': data['IsVegetarian']}
        todays_food_items.append(
            item_dict)
    return todays_food_items


def get_russell_menu():
    '''
    This gets the menu from Russle dinding hall

    :return:
        A list of strings.
        A list of the items from the dining hall. Each item is a dictionary
    '''
    import json
    url = "https://udel.campusdish.com/LocationsAndMenus/RussellDiningHall"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    source = doc.prettify()

    m = re.search("model: ({.*})", source)
    model = m.group(1)
    json = json.loads(model)

    todays_food_items = []

    for item in range(0, len(json['Menu']['MenuProducts'])):
        data = json['Menu']['MenuProducts'][item]['Product']
        item_dict = {'name': data['MarketingName'], 'ContainsEggs': data['ContainsEggs'], 'ContainsFish': data['ContainsFish'], 'ContainsMilk': data['ContainsMilk'], 'ContainsPeanuts': data['ContainsPeanuts'], 'ContainsShellfish': data['ContainsShellfish'],
                     'ContainsSoy': data['ContainsSoy'], 'ContainsTreeNuts': data['ContainsTreeNuts'], 'ContainsWheat': data['ContainsWheat'], 'IsGlutenFree': data['IsGlutenFree'], 'IsHalal': data['IsHalal'], 'IsVegan': data['IsVegan'], 'IsVegetarian': data['IsVegetarian']}
        todays_food_items.append(
            item_dict)
    return todays_food_items


def get_pencader_menu():
    '''
    This gets the menu from pencader
    :return:
        A list of dictionaries of the items on the menu
        A list of the items on the menu
    '''
    import json
    url = "https://udel.campusdish.com/LocationsAndMenus/PencaderDiningHall"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    source = doc.prettify()

    m = re.search("model: ({.*})", source)
    model = m.group(1)
    json = json.loads(model)

    todays_food_items = []

    for item in range(0, len(json['Menu']['MenuProducts'])):
        data = json['Menu']['MenuProducts'][item]['Product']
        item_dict = {'name': data['MarketingName'], 'ContainsEggs': data['ContainsEggs'], 'ContainsFish': data['ContainsFish'], 'ContainsMilk': data['ContainsMilk'], 'ContainsPeanuts': data['ContainsPeanuts'], 'ContainsShellfish': data['ContainsShellfish'],
                     'ContainsSoy': data['ContainsSoy'], 'ContainsTreeNuts': data['ContainsTreeNuts'], 'ContainsWheat': data['ContainsWheat'], 'IsGlutenFree': data['IsGlutenFree'], 'IsHalal': data['IsHalal'], 'IsVegan': data['IsVegan'], 'IsVegetarian': data['IsVegetarian']}
        todays_food_items.append(
            item_dict)
    return todays_food_items


def get_all_menus():
    '''
    This function scrapes the web and gets all of the menus for the dining halls.
    Args:
        N/A
    returns:
        A list of the dining hall lists. The first element in the list is the menu at CR, the
        second element is the menu at Russle, the third is the menu at Pencader. It returns a list
        of lists of dictionaries
    '''
    cr_menu = get_cr_menu()
    russle_menu = get_russell_menu()
    pencader_menu = get_pencader_menu()

    return [cr_menu, russle_menu, pencader_menu]



def egg_allergy(menu):
    '''
    filters out all of the menu items that contain eggs

    args:
        menu: list of dict) a menu at a dining hall for the day

    returns:
        list of dict) a new menu of todays dining hall food items that don't contain eggs
    '''
    egg_free_menu = []
    for item in menu:
        if not item['ContainsEggs']:
            egg_free_menu.append(item)
    return egg_free_menu

def fish_allergy(menu):
    '''
    filters out all of the menu items that contain fish

    args:
        menu: list of dict) a menu at a dining hall for the day

    returns:
        list of dict) a new menu of todays dining hall food items that don't contain fish
    '''
    fish_free_menu = []
    for item in menu:
        if not item['ContainsFish']:
            fish_free_menu.append(item)
    return fish_free_menu

def lactose_intollerant(menu):
    '''
    filters out all of the menu items that contain lactose

    args:
        menu: list of dict) a menu at a dining hall for the day

    returns:
        list of dict) a new menu of todays dining hall food items that don't contain lactose
    '''
    lactose_free_menu = []
    for item in menu:
        if not item['ContainsMilk']:
            lactose_free_menu.append(item)
    return lactose_free_menu

def peanut_allergy(menu):
    '''
    filters out all of the menu items that contain peanuts

    args:
        menu: list of dict) a menu at a dining hall for the day

    returns:
        list of dict) a new menu of todays dining hall food items that don't contain peanuts
    '''
    peanut_free_menu = []
    for item in menu:
        if not item['ContainsPeanuts']:
            peanut_free_menu.append(item)
    return peanut_free_menu

def tree_nut_allergy(menu):
    '''
    filters out all of the menu items that contain tree nuts

    args:
        menu: list of dict) a menu at a dining hall for the day

    returns:
        list of dict) a new menu of todays dining hall food items that don't contain tree nuts
    '''
    tree_nut_free_menu = []
    for item in menu:
        if not item['ContainsTreeNuts']:
            tree_nut_free_menu.append(item)
    return tree_nut_free_menu

def shellfish_allergy(menu):
    '''
    filters out all of the menu items that contain shellfish

    args:
        menu: list of dict) a menu at a dining hall for the day

    returns:
        list of dict) a new menu of todays dining hall food items that don't contain shellfish
    '''
    shellfish_free_menu = []
    for item in menu:
        if not item['ContainsShellfish']:
            shellfish_free_menu.append(item)
    return shellfish_free_menu

def soy_allergy(menu):
    '''
    filters out all of the menu items that contain soy

    args:
        menu: list of dict) a menu at a dining hall for the day

    returns:
        list of dict) a new menu of todays dining hall food items that don't contain soy
    '''
    soy_free_menu = []
    for item in menu:
        if not item['ContainsSoy']:
            soy_free_menu.append(item)
    return soy_free_menu

def wheat_allergy(menu):
    '''
    filters out all of the menu items that contain wheat

    args:
        menu: list of dict) a menu at a dining hall for the day

    returns:
        list of dict) a new menu of todays dining hall food items that don't contain wheat
    '''
    wheat_free_menu = []
    for item in menu:
        if not item['ContainsWheat']:
            wheat_free_menu.append(item)
    return wheat_free_menu

def gluten_free(menu):
    '''
    filters out all of the menu items that contain gluten

    args:
        menu: list of dict) a menu at a dining hall for the day

    returns:
        list of dict) a new menu of todays dining hall food items that don't contain gluten
    '''
    gluten_free_menu = []
    for item in menu:
        if item['IsGlutenFree']:
            gluten_free_menu.append(item)
    return gluten_free_menu

def vegan(menu):
    '''
    filters out all of the menu items that are not vegan

    args:
        menu: list of dict) a menu at a dining hall for the day

    returns:
        list of dict) a new menu of todays dining hall food items that are all vegan
    '''
    vegan_menu = []
    for item in menu:
        if item['IsVegan']:
            vegan_menu.append(item)
    return vegan_menu

def vegetarian(menu):
    '''
    filters out all of the menu items that are not vegetarian

    args:
        menu: list of dict) a menu at a dining hall for the day

    returns:
        list of dict) a new menu of todays dining hall food items that are all vegetarian
    '''
    vegetarian_menu = []
    for item in menu:
        if item['IsVegetarian']:
            vegetarian_menu.append(item)

    return vegetarian_menu


# Can add this later although I don't know how to ask proper permission
# def is_halal(menu):
#     pass



def find_valid_menu(dining_hall_menu, record):
    '''
    Finds a menu that fits the constraints of a given record. It acts like a filtration system
    and adds whatever menu items that fit the requirements onto the list.

    args:
        dining_hall_menu: list of dict) this is the menu of the day for a particular dining hall

        record: this is the record data of the person

    returns:
        list of dict) it returns a menu that fits the constrainsts of the persons record.
    '''

    choice_list = dining_hall_menu

    if record['Are you vegan or vegetarian?'] == 'Vegetarian':
        choice_list = vegetarian(choice_list)
    elif record['Are you vegan or vegetarian?'] == 'Vegan':
        choice_list = vegan(choice_list)
    elif record['Do you have an Egg Allergy?'] == 'Yes':
        choice_list = egg_allergy(choice_list)
    elif record['Do you have a Peanut Allergy?'] == 'Yes':
        choice_list = peanut_allergy(choice_list)
    elif record['Do you have a Tree Nut Allergy?'] == 'Yes':
        choice_list = tree_nut_allergy(choice_list)
    elif record['Do you have a Fish Allergy?'] == 'Yes':
        choice_list = fish_allergy(choice_list)
    elif record['Do you have a Shellfish Allergy?'] == 'Yes':
        choice_list = shellfish_allergy(choice_list)
    elif record['Do you have a Soy Allergy?'] == 'Yes':
        choice_list = soy_allergy(choice_list)
    elif record['Do you have a Wheat Allergy?'] == 'Yes':
        choice_list = wheat_allergy(choice_list)
    elif record['Are you Gluten Free?'] == 'Yes':
        choice_list = gluten_free(choice_list)
    elif record['Are you Lactose Intolerant?'] == 'Yes':
        choice_list = lactose_intollerant(choice_list)

    return choice_list



def highest_proteins(menu, record):
    '''
    does the same thing as highest_vegetables() but it does it with proteins.

    args: same as highest_vegetables()

    returns: same as highest_vegetables() but proteins instead of vegetables

    '''
    proteins = {
        'Chicken': ['Chicken', 'Turkey'],
        'Beef': ['Beef', 'Burger', 'Hotdog', 'Hot Dog', 'Steak', 'Ribs', 'Corndog', 'Corn Dog'],
        'Pork': ['Pork', 'Bacon', 'Sausage', 'Ham'],
        'Eggs': ['Egg'],
        'Fish': ['Fish', 'Salmon', 'Tilapia', 'Tuna', 'Herring', 'Mackerel', 'Cod '],
        'Beans': ['Bean', 'Legume'],
        'Tofu': ['Tofu', 'Bean Curd'],
    }
    highest_protein_names = []
    highest_protein_name = ''
    highest_protein_value = 0

    for item in menu:
        for protein in proteins:
            for food in proteins[protein]:
                if food in item['name']:
                    if record[protein] != '':
                        valid_ascii_name = ''
                        for letter in item['name']:
                            if letter not in '®©³²@#$%^&*()_+™':
                                valid_ascii_name += letter
                        if int(record[protein]) > highest_protein_value:
                            highest_protein_value = int(record[protein])
                            highest_protein_name = valid_ascii_name
                            highest_protein_names.clear()
                            highest_protein_names.append(valid_ascii_name)
                        elif int(record[protein]) == highest_protein_value:
                            highest_protein_names.append(valid_ascii_name)

    return highest_protein_value, highest_protein_names

def highest_carbs(menu, record):
    '''
    This does the same thing as the highest_vegetables function but it does it with carbs

    args: same as highest_vegetables()

    returns: same as highest_vegetables() but it returns the carbs

    '''
    carbs = {
    'Rice': ['Rice','Brown Rice'],
    'Potatoes': ['Potato', 'French Fries', 'Chips'],
    'Bread': ['Toast', 'Bread', 'Baguette', 'Bagel'],
    'Pasta': ['Pasta','Noodles','Tortelloni','Bucatini', 'Macaroni', 'Spaghetti',
        'Penne','Lasagna','Rigatoni','Bowtie','Farfalle','Capellini']
    }

    highest_carb_names = []
    highest_carb_name= ''
    highest_carb_value = 0

    for item in menu:
        for carb in carbs:
            for food in carbs[carb]:
                if food in item['name']:
                    if record[carb] != '':
                        valid_ascii_name = ''
                        for letter in item['name']:
                            if letter not in '®©³²@#$%^&*()_+™':
                                valid_ascii_name += letter
                        if int(record[carb]) > highest_carb_value:
                            highest_carb_value = int(record[carb])
                            highest_carb_name = valid_ascii_name
                            highest_carb_names.clear()
                            highest_carb_names.append(valid_ascii_name)
                        elif int(record[carb]) == highest_carb_value:
                            highest_carb_names.append(valid_ascii_name)

    return highest_carb_value, highest_carb_names

def highest_vegetables(menu, record):
    '''
    This fucntion returns the highest scoring vegetable meals for a perticular person.
    it is basically a max() function for the vegetables, and then it adds whatever is on
    the menu for the day to a list, and then it returns that list.

    args:
        menu: list of dict) this is a valid menu of the person

        record: dict) this is the record data of a person

    returns:
        highest_vegetable_value: int) this is the vlaue of the highest vegetables

        highest_vegetable_names: list of str) this is all of the highest scoring vegetables

    '''
    vegetables = {
        'Leafy Greens': ['Kale','Collard Greens','Green Bean', 'Broccoli'],
        'Peppers': ['Peppers'],
        'Corn': ['Corn', 'Maize'],
    }

    highest_vegetable_names = []
    highest_vegetable_name= ''
    highest_vegetable_value = 0

    for item in menu:
        for vegetable in vegetables:
            for food in vegetables[vegetable]:
                if food in item['name']:
                    if record[vegetable] != '':
                        valid_ascii_name = ''
                        for letter in item['name']:
                            if letter not in '®©³²@#$%^&*()_+™':
                                valid_ascii_name += letter
                        if int(record[vegetable]) > highest_vegetable_value:
                            highest_vegetable_value = int(record[vegetable])
                            highest_vegetable_name = valid_ascii_name
                            highest_vegetable_names.clear()
                            highest_vegetable_names.append(valid_ascii_name)
                        elif int(record[vegetable]) == highest_vegetable_value:
                            highest_vegetable_names.append(valid_ascii_name)

    return highest_vegetable_value, highest_vegetable_names


def calculate_highest_scoring_meal(menu, record):
    '''
    This function finds the highest scoring meal consisting of proteins, carbs, and vegetables for
    a particular person

    args:
        menu: list of dict) this is the menu of valid items. It is just a menu of all the dining hall
                            food for the day that fits the constraints of the users record

        record: dict) the data about the user

    returns:
        highest_meal_score: int) this is an integer of the highest meals total score

        highest_meal_name: list of str) this is a list of strings that consists of the names of the
                            foods of the highest scoring meal

    '''
    highest_protein = highest_proteins(menu, record)
    highest_carb = highest_carbs(menu, record)
    highest_vegetable = highest_vegetables(menu,record)

    highest_meal_name = {
        'protein': highest_protein[1],
        'carb': highest_carb[1],
        'vegetable': highest_vegetable[1]
    }
    highest_meal_score = highest_protein[0] + highest_carb[0] + highest_vegetable[0]

    return highest_meal_score, highest_meal_name


def get_valid_menus(record):
    '''
    This function just gets all of the valid menus for a particular record

    args:
        record: dict) The data of a record of a person

    returns:
        list of dict) a list of all of the filtered menu items.
    '''
    all_menus = get_all_menus()

    valid_cr_menu = None
    valid_russell_menu = None
    valid_pencader_menu = None

    n = 0
    for dining_hall in all_menus:
        n += 1
        if n == 1:
            valid_cr_menu = find_valid_menu(dining_hall, record)
        elif n == 2:
            valid_russell_menu = find_valid_menu(dining_hall, record)
        else:
            valid_pencader_menu = find_valid_menu(dining_hall, record)

    all_valid_menus = [valid_cr_menu, valid_russell_menu, valid_pencader_menu]

    return all_valid_menus


def format_top_meals(meal_score, dining_hall, meal_name):
    '''
    This function is basically just takes the data and fromats it a certain way so that it is easy for the user to read

    args:
        meal_score: int) This is the value of the meal that scored the highest at a particular dining hall

        dining_hall: str) This is the name of the dining hall that has the score, and is going to be displayed

        meal_name: dict) This is all of the meals that scored the highest value, their keys are all 'protein','carb', 'vegetable'
    '''

    line_1 = '-- ' + str(dining_hall).upper() + ' has a max value of ' + str(meal_score) + ' --'
    line_2 = 'Proteins: '
    line_3 = 'Carbs: '
    line_4 = 'Vegetables: '

    if meal_score == 0:
        closed_line = '-- ' + str(dining_hall).upper() + ' is closed today --' + "\n"
        return closed_line

    if meal_name['protein'] == []:
        line_2 += "We couldn't find a protein, we do not suggest going here"
    else:
        line_2 += str(meal_name['protein'])

    if meal_name['carb'] == []:
        line_3 += "We couldn't find a carbohydrate, we do not suggest going here"
    else:
        line_3 += str(meal_name['carb'])

    if meal_name['vegetable'] == []:
        line_4 += "We couldn't find a vegetable, but there are awlays salads"
    else:
        line_4 += str(meal_name['vegetable'])


    return (line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4 + "\n")

def top_meal(record):
    '''
    This function finds the top meals of the day for each dining hall for the record that is passed through it.

    args:
        record: dict) the record data of each person

    return: A string like this
            -- DINING HALL has a value of # --
            Protein: []
            Carbs: []
            Vegetables: []
    '''
    all_valid_menus = get_valid_menus(record)

    cr_meal_score = 0
    cr_meal_name = ''

    russell_meal_score = 0
    russell_meal_name = ''

    pencader_meal_score = 0
    pencader_meal_name = ''


    n = 0
    for valid_menu in all_valid_menus:
        n += 1
        if n == 1:
            cr_meal_score = calculate_highest_scoring_meal(valid_menu, record)[0]
            cr_meal_name = calculate_highest_scoring_meal(valid_menu,record)[1]
        elif n == 2:
            russell_meal_score = calculate_highest_scoring_meal(valid_menu, record)[0]
            russell_meal_name = calculate_highest_scoring_meal(valid_menu,record)[1]

        else:
            pencader_meal_score = calculate_highest_scoring_meal(valid_menu, record)[0]
            pencader_meal_name = calculate_highest_scoring_meal(valid_menu,record)[1]


    meal_scores = {'cr': cr_meal_score, 'russell': russell_meal_score, 'pencader': pencader_meal_score}
    meal_names = [cr_meal_name, russell_meal_name, pencader_meal_name]

    formatted_results = ''
    for score, meal_name in zip(meal_scores, meal_names):
        formatted_results += format_top_meals(meal_scores[score], score, meal_name)
        formatted_results += "\n"
    return formatted_results


def format_overall_scores(dining_hall_scores):
    formated_scores = 'CR: ' + str(dining_hall_scores['cr']) + ', RUSSELL: ' + str(dining_hall_scores['russell']) + ', PENCADER: ' + str(dining_hall_scores['pencader'])
    return formated_scores

def find_overall_scores(record):
    '''
    This function finds the overall scores of the dining halls. It takes all the meals and their scores and
    adds them up for one particular dining hall

    args:
        record: dict) the record data of the person

    returns:
        dict) a dictionary of all the dining halls maped to their total value

    '''
    all_valid_menus = get_valid_menus(record)

    # Can impliment functionality for plant based meats as well
    all_foods = {
        'Rice': ['Rice','Brown Rice'],
        'Leafy Greens': ['Kale','Collard Greens','Green Bean', 'Brocoli'],
        'Beans': ['Bean', 'Legume'],
        'Potatoes': ['Potato', 'French Fries', 'Chips'],
        'Tofu': ['Tofu', 'Bean Curd'],
        'Corn': ['Corn', 'Maize'],
        'Peppers': ['Peppers'],
        'Bread': ['Toast', 'Bread', 'Baugett', 'Bagel'],
        'Pasta': ['Pasta','Noodles','Tortelloni','Bucantini', 'Macaroni', 'Spaghetti',
                'Penne','lasagna','Rigatoni','Bowtie','Farfelle','Capellini'],
        'Eggs': ['Egg'],
        'Fish': ['Fish', 'Salmon', 'Tilapia', 'Tuna', 'Herring', 'Mackerel', 'Cod '],
        'Chicken': ['Chicken', 'Turkey'],
        'Beef': ['Beef', 'Burger', 'Hotdog', 'Hot Dog', 'Steak', 'Ribs', 'Corndog', 'Corn Dog'],
        'Pork': ['Pork', 'Bacon', 'Sausage', 'Ham'],
    }

    counted_menu_items = {}
    dining_hall_scores = {'cr': 0,'russell': 0, 'pencader': 0}

    n = -1
    for valid_menu in all_valid_menus:
        n += 1
        for food_item in valid_menu:
            for food in all_foods:
                for alternate_name in all_foods[food]:
                    if alternate_name in food_item['name']:
                        if food_item['name'] not in counted_menu_items:
                            counted_menu_items[food_item['name']] = record[food]
                        else:
                            if record[food] > counted_menu_items[food_item['name']]:
                                counted_menu_items[food_item['name']] = record[food]

        for item in counted_menu_items:
            if counted_menu_items[item] != '':
                if n == 0:
                    dining_hall_scores['cr'] += int(counted_menu_items[item])
                elif n == 1:
                    dining_hall_scores['russell'] += int(counted_menu_items[item])
                else:
                    dining_hall_scores['pencader'] += int(counted_menu_items[item])

    formated_scores = format_overall_scores(dining_hall_scores)

    return formated_scores


