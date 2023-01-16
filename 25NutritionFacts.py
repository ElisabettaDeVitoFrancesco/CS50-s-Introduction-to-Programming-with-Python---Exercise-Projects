# Ask to choose a food item
def main():
    raw_food = input("Item: ").title()
    calories(raw_food)

# create dictionaries with the raw food items and the relate calories
# text from the website copied into dictionaries inside a list

raw_fruits = [
    {"Fruits": "Apple", "Calories" : 130, "Calories from Fat" : 0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 260, "Potassium (%DV)": 7, "Total Carb. (g)": 34, "Total Carb. (%DV)": 11,
    "Dietary Fiber (g)": 5, "Dietary Fiber (%DV)": 20,	"Sugars (g)": 25, "Protein (g)": 1,
    "Vitamin A (%DV)": 2,	"Vitamin C (%DV)" : 8, "Calcium (%DV)" : 2, "Iron (%DV)" : 2},

    {"Fruits": "Avocado", "Calories" : 50, "Calories from Fat" : 35, "Total Fat (g)" : 4.5, "Total Fat (%DV)": 7, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 140, "Potassium (%DV)": 4, "Total Carb. (g)": 3, "Total Carb. (%DV)": 1,
    "Dietary Fiber (g)": 1, "Dietary Fiber (%DV)": 4,	"Sugars (g)": 0, "Protein (g)": 1,
    "Vitamin A (%DV)": 0,	"Vitamin C (%DV)" : 4, "Calcium (%DV)" : 0, "Iron (%DV)" : 2},

    {"Fruits": "Banana", "Calories" : 110, "Calories from Fat" : 0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 450, "Potassium (%DV)": 13, "Total Carb. (g)": 30, "Total Carb. (%DV)": 10,
    "Dietary Fiber (g)": 3, "Dietary Fiber (%DV)": 12, "Sugars (g)": 19, "Protein (g)": 1,
    "Vitamin A (%DV)": 2,	"Vitamin C (%DV)" : 15, "Calcium (%DV)" : 0, "Iron (%DV)" : 2},

    {"Fruits": "Cantaloupe", "Calories" : 50, "Calories from Fat" : 0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 20,
    "Sodium (%DV)": 1, "Potassium (mg)": 240, "Potassium (%DV)": 7, "Total Carb. (g)": 12, "Total Carb. (%DV)": 4,
    "Dietary Fiber (g)": 1, "Dietary Fiber (%DV)": 4,	"Sugars (g)": 11, "Protein (g)": 1,
    "Vitamin A (%DV)": 120,	"Vitamin C (%DV)" : 80, "Calcium (%DV)" : 2, "Iron (%DV)" : 	2},

    {"Fruits": "Grapefruit", "Calories" : 60, "Calories from Fat" : 0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 160, "Potassium (%DV)": 5, "Total Carb. (g)": 15, "Total Carb. (%DV)": 5,
    "Dietary Fiber (g)": 2, "Dietary Fiber (%DV)": 8,	"Sugars (g)": 11, "Protein (g)": 1,
    "Vitamin A (%DV)": 35,	"Vitamin C (%DV)" : 100, "Calcium (%DV)" : 4, "Iron (%DV)" : 0},

    {"Fruits": "Grapes", "Calories" : 90, "Calories from Fat" : 0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 15,
    "Sodium (%DV)": 1, "Potassium (mg)": 240, "Potassium (%DV)": 7, "Total Carb. (g)": 23, "Total Carb. (%DV)": 8,
    "Dietary Fiber (g)": 1, "Dietary Fiber (%DV)": 4,	"Sugars (g)": 20, "Protein (g)": 0,
    "Vitamin A (%DV)": 0,	"Vitamin C (%DV)" :	2, "Calcium (%DV)" : 	2, "Iron (%DV)" : 0},

    {"Fruits": "Honeydew Melon", "Calories" : 50, "Calories from Fat" : 0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 30,
    "Sodium (%DV)": 1, "Potassium (mg)": 210, "Potassium (%DV)": 6, "Total Carb. (g)": 12, "Total Carb. (%DV)": 4,
    "Dietary Fiber (g)": 1, "Dietary Fiber (%DV)": 4,	"Sugars (g)": 11, "Protein (g)": 1,
    "Vitamin A (%DV)": 2,	"Vitamin C (%DV)" : 45, "Calcium (%DV)" : 	2, "Iron (%DV)" : 	2},

    {"Fruits": "Kiwifruit", "Calories" : 90, "Calories from Fat" : 10, "Total Fat (g)" : 1, "Total Fat (%DV)":2, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 450, "Potassium (%DV)": 13, "Total Carb. (g)": 20, "Total Carb. (%DV)": 7,
    "Dietary Fiber (g)": 4, "Dietary Fiber (%DV)": 16,	"Sugars (g)": 13, "Protein (g)": 1,
    "Vitamin A (%DV)": 2,	"Vitamin C (%DV)" : 240, "Calcium (%DV)" : 	4, "Iron (%DV)" : 	2},

    {"Fruits": "Lemon",	"Calories" : 15, "Calories from Fat" : 0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 75, "Potassium (%DV)": 2, "Total Carb. (g)": 5, "Total Carb. (%DV)": 2,
    "Dietary Fiber (g)": 2, "Dietary Fiber (%DV)": 8,	"Sugars (g)": 2, "Protein (g)": 0,
    "Vitamin A (%DV)": 0,	"Vitamin C (%DV)" : 40, "Calcium (%DV)" : 	2, "Iron (%DV)" : 	0},

    {"Fruits": "Lime",	"Calories" : 20, "Calories from Fat" : 0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 75, "Potassium (%DV)": 2, "Total Carb. (g)": 7, "Total Carb. (%DV)": 2,
    "Dietary Fiber (g)": 2, "Dietary Fiber (%DV)": 8,	"Sugars (g)": 0, "Protein (g)": 0,
    "Vitamin A (%DV)": 0,	"Vitamin C (%DV)" : 35, "Calcium (%DV)" : 	0, "Iron (%DV)" : 	0},

    {"Fruits": "Nectarine",	"Calories" : 60, "Calories from Fat" : 5, "Total Fat (g)" :	0.5, "Total Fat (%DV)":	1, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 250, "Potassium (%DV)": 7, "Total Carb. (g)": 15, "Total Carb. (%DV)": 5,
    "Dietary Fiber (g)": 2, "Dietary Fiber (%DV)": 8,	"Sugars (g)": 11, "Protein (g)": 1,
    "Vitamin A (%DV)": 8,	"Vitamin C (%DV)" : 15, "Calcium (%DV)" : 	0, "Iron (%DV)" : 	2},

    {"Fruits": "Orange", "Calories" : 80, "Calories from Fat" : 0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 250, "Potassium (%DV)": 7, "Total Carb. (g)": 19, "Total Carb. (%DV)": 6,
    "Dietary Fiber (g)": 3, "Dietary Fiber (%DV)": 12,	"Sugars (g)": 14, "Protein (g)": 1,
    "Vitamin A (%DV)": 2,	"Vitamin C (%DV)" : 130, "Calcium (%DV)" : 	6, "Iron (%DV)" : 	0},

    {"Fruits": "Peach",	"Calories" : 60, "Calories from Fat" : 0, "Total Fat (g)" : 0.5, "Total Fat (%DV)":	1, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 230, "Potassium (%DV)": 7, "Total Carb. (g)": 15, "Total Carb. (%DV)": 5,
    "Dietary Fiber (g)": 2, "Dietary Fiber (%DV)": 8,	"Sugars (g)": 13, "Protein (g)": 1,
    "Vitamin A (%DV)": 6,	"Vitamin C (%DV)" : 15, "Calcium (%DV)" : 	0, "Iron (%DV)" : 	2},

    {"Fruits": "Pear",	"Calories" : 100, "Calories from Fat" :	0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 190, "Potassium (%DV)": 5, "Total Carb. (g)": 26, "Total Carb. (%DV)": 9,
    "Dietary Fiber (g)": 6, "Dietary Fiber (%DV)": 24,	"Sugars (g)": 16, "Protein (g)": 1,
    "Vitamin A (%DV)": 0,	"Vitamin C (%DV)" : 10, "Calcium (%DV)" : 	2, "Iron (%DV)" : 	0},

    {"Fruits": "Pineapple",	"Calories" : 50, "Calories from Fat" : 0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 10,
    "Sodium (%DV)": 0, "Potassium (mg)": 120, "Potassium (%DV)": 3, "Total Carb. (g)": 13, "Total Carb. (%DV)": 4,
    "Dietary Fiber (g)": 1, "Dietary Fiber (%DV)": 4,	"Sugars (g)": 10, "Protein (g)": 1,
    "Vitamin A (%DV)": 2,	"Vitamin C (%DV)" : 50, "Calcium (%DV)" : 	2, "Iron (%DV)" : 	2},

    {"Fruits": "Plums",	"Calories" : 70, "Calories from Fat" : 0, "Total Fat (g)" :	0, "Total Fat (%DV)": 0, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 230, "Potassium (%DV)": 7, "Total Carb. (g)": 19, "Total Carb. (%DV)": 6,
    "Dietary Fiber (g)": 2, "Dietary Fiber (%DV)": 8,	"Sugars (g)": 16, "Protein (g)": 1,
    "Vitamin A (%DV)": 8,	"Vitamin C (%DV)" : 10, "Calcium (%DV)" : 	0, "Iron (%DV)" : 	2},

    {"Fruits": "Strawberries", "Calories" : 50, "Calories from Fat" :	0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 170, "Potassium (%DV)": 5, "Total Carb. (g)": 11, "Total Carb. (%DV)": 4,
    "Dietary Fiber (g)": 2, "Dietary Fiber (%DV)": 8,	"Sugars (g)": 8, "Protein (g)": 1,
    "Vitamin A (%DV)": 0,	"Vitamin C (%DV)" : 160, "Calcium (%DV)" : 	2, "Iron (%DV)" : 	2},

    {"Fruits": "Sweet Cherries", "Calories" : 100, "Calories from Fat" :	0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 350, "Potassium (%DV)": 10, "Total Carb. (g)": 26, "Total Carb. (%DV)": 9,
    "Dietary Fiber (g)": 1, "Dietary Fiber (%DV)": 4,	"Sugars (g)": 16, "Protein (g)": 1,
    "Vitamin A (%DV)": 2,	"Vitamin C (%DV)" : 15, "Calcium (%DV)" : 	2, "Iron (%DV)" : 	2},

    {"Fruits": "Tangerine",	"Calories" : 50, "Calories from Fat" : 0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 160, "Potassium (%DV)": 5, "Total Carb. (g)": 13, "Total Carb. (%DV)": 4,
    "Dietary Fiber (g)": 2, "Dietary Fiber (%DV)": 8,	"Sugars (g)": 9, "Protein (g)": 1,
    "Vitamin A (%DV)": 6,	"Vitamin C (%DV)" : 45, "Calcium (%DV)" : 	4, "Iron (%DV)" : 	0},

    {"Fruits": "Watermelon", "Calories" : 80, "Calories from Fat" : 0, "Total Fat (g)" : 0, "Total Fat (%DV)": 0, "Sodium (mg)": 0,
    "Sodium (%DV)": 0, "Potassium (mg)": 270, "Potassium (%DV)": 8, "Total Carb. (g)": 21, "Total Carb. (%DV)": 7,
    "Dietary Fiber (g)": 1, "Dietary Fiber (%DV)": 4,	"Sugars (g)": 20, "Protein (g)": 1,
    "Vitamin A (%DV)": 30,	"Vitamin C (%DV)" : 25, "Calcium (%DV)" : 	2, "Iron (%DV)" : 	4}
]

def calories(item):
    for fruit in raw_fruits: # check among the keys of the dictionary
        # check if this item is in one of the dict of raw fruits
        if fruit["Fruits"] == item:
            # # if yes, print out the related calories
            print("Calories: ", fruit["Calories"]) # output as what was assigned to the key called item
        # if not, ignore (don't print anything)

main()
