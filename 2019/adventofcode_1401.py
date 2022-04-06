import json

arr_fuel = []
arr_recipes = []
dict_depot = {}

def dictify_line(_line):
    # Wandelt den String in ein Array mit zwei Dictionaries um

    a_line = _line.split("=>")

    for i in range(0, len(a_line)):
        a_line[i] = " ".join(reversed(a_line[i].strip().replace(", ", " , ").split(" ")))
        a_line[i] = json.loads(str("{'"+ a_line[i].replace(" , ", ",'").replace(" ","':") + "}").replace("'", "\""))

    return a_line[::-1]

def start_cooking():
    # Ersetzt die Inhalte durch deren Zutaten, bis nur noch OREs überbleiben 

    dict_resolved_items = {}
    dict_ingredients_to_add = {}

    for item_fuel in arr_fuel:
        #print("item_fuel " + str(item_fuel))
        for key_fuel in item_fuel[1]:
            to_add = {}

            if key_fuel != "ORE":
                to_add = add_ingredients(read_ingredients(key_fuel), item_fuel[1].get(key_fuel))
                dict_resolved_items[key_fuel] = item_fuel[1].get(key_fuel)

            for key in to_add:
                if key in dict_ingredients_to_add:
                    dict_ingredients_to_add[key] = dict_ingredients_to_add.get(key) + to_add.get(key)
                else:
                    dict_ingredients_to_add[key] = to_add.get(key)
    #print("")
    # Dictionary aufräumen
    for key in dict_resolved_items:
        if dict_resolved_items.get(key) == item_fuel[1].get(key):
            del item_fuel[1][key]
            #print("item replaced => " + str(key))
        else:
            item_fuel[1][key] = item_fuel[1][key] - dict_resolved_items.get(key)

    # Neue Zutaten hinzufügen    -----> funktioniert nicht!!!!!!!
    for key in dict_ingredients_to_add:
        if arr_fuel[0][1].get(key):
            arr_fuel[0][1][key] = arr_fuel[0][1].get(key) + dict_ingredients_to_add.get(key)
        else:
            arr_fuel[0][1][key] = dict_ingredients_to_add.get(key)
        #print(str(key) + " arr_fuel " + str(arr_fuel))

def read_ingredients(_key_fuel):
    # liest die Zutaten für einen Inhalt

    for item_recipes in arr_recipes:
        if item_recipes[0].get(_key_fuel):
            ingredients = item_recipes[1]
            ingredients["bulk"] = item_recipes[0][_key_fuel]
            ingredients["parent"] = _key_fuel

    return ingredients


def add_ingredients(_ingredients, _amount):
    # schaut nach Resten im Depot, fügt Zutaten hinzu und speichert ggf Überschuss im Depot 
    
    ingredients_to_add = {}
    parent_to_replace = _ingredients.get("parent")
    parent_amount_bulk = _ingredients.get("bulk")
    parent_amount_needed = _amount

    #print("")
    #print("add ingredients " + str(_ingredients) + " " + str(parent_amount_needed))

    amount_produced = get_overflow(parent_to_replace)
    #print("Get Overflow " + str(parent_to_replace) + " " + str(amount_produced))

    while amount_produced < parent_amount_needed:
        amount_produced += parent_amount_bulk

        for key in _ingredients:
            if key != "parent" and key != "bulk":
                # Holt bereits produzierte Ingredients aus dem Depot, wenn vorhanden


                    if ingredients_to_add.get(key):
                        ingredients_to_add[key] = ingredients_to_add.get(key) + _ingredients.get(key)
                    else:
                        ingredients_to_add[key] = _ingredients.get(key)

    if amount_produced > parent_amount_needed :
        store_overflow(parent_to_replace, amount_produced - parent_amount_needed)

    #print("ingredients_to_add " + str(ingredients_to_add))
    return ingredients_to_add

def store_overflow(_key, _value):
    #print("store_overflow " + str(_key) + " " + str(_value))

    if _key in dict_depot:
        dict_depot[_key] = dict_depot.get(_key) + _value
    else:
        dict_depot[_key] = _value


def get_overflow(_key):
    if _key in dict_depot:
        amount_stored = dict_depot.get(_key)
        dict_depot[_key] = 0
    else:
        amount_stored = 0

    return amount_stored


with open ('./adventofcode_1401_input.txt') as file:
    for line in file:
        if "FUEL" in line:
            arr_fuel.append(dictify_line(line))
        else:
            arr_recipes.append(dictify_line(line))
print("arr_fuel " + str(arr_fuel))
print("arr_recipes " + str(arr_recipes))
print("")

while len(arr_fuel[0][1]) > 1:
    start_cooking()
    print("arr_fuel " + str(arr_fuel))
    print("depot " + str(dict_depot))
    print("")
    print("")

