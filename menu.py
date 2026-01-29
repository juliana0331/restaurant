import csv 
import random 
menu_items = []

def load_menu():
    file = open("recipes.csv", "r" , encoding="utf-8")
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        item = {
            "id": int(row[0]),
            "name": row[1],
            "cuisine": row[2],
            "difficlty": row[3],
            "prep_time": int(row[4]),
            "ingredients": row[5].split(","),
            "category": row[6]
        }
        menu_items.append(item)

    file.close()
     
    #load_menu()
    #print(menu_items)

def show_menu():
    print("/n===== RESTURANT MENU =====")
    print("1 _ Add new item")
    print("2 _ View all items")
    print("3 _ Search")
    print("4 _ Delete item")
    print("5 _ Statistics")
    print("6 _ Recommend item")
    print("0 _ Sava and Exit")
load_menu()
def add_new_item():
    name = input("item name: ")
    cuisine = input("cuisine: ")
    difficulty = input("difficulty: ")
    prep_time = int(input("preparation time(minutes): "))
    ingredients = input("ingredients(comma separated): ")
    category = input("category: ")

    new_id = 1
    if menu_items:
        new_id = menu_items[-1]["id"] + 1

    item = {
        "id": new_id,
        "name": name,
        "cuisine": cuisine,
        "difficulty": difficulty,
        "prep_items": prep_time,
        "ingredients": ingredients.split(","),
        "category": category 
    }

    menu_items.append(item)
    with open ("recipes.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            item["id"],
            item["name"],
            item["cuisine"],
            item["difficulty"],
            item["prep_items"],
            ",".join(item["ingredients"]),
            item["category"]
        ])

    print("item added successfully!")



while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_new_item()
        elif choice == "2":
            if not menu_items:
                print("No items available")
            else:
                for item in menu_items:
                    print(f'{item["id"]} _ {item["name"]}')    
        elif choice == "3":
            keyword = input("search by name or category: ").lower().strip()
            found = False

            for item in menu_items:
                if (
                    keyword in item["name"].lower().strip() 
                    or keyword in item["category"].lower().strip()
                ):
                    print(f'{item["id"]}-{item["name"]} ({item["category"]})')
                    found = True
            if not found:
                print("no matching items found")
        elif choice == "4":
            print("Delete item _ coming soon")
        elif choice == "5":
            print("Statistics _ coming soon")
        elif choice == "6":
            print("recommend item _ coming soon")
        elif choice == "0":
            print ("goodbye")
            break
        else:
            print("invalid choice, try again")

            
          


