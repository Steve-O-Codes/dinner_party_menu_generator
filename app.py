#######################################
# Python Dinner Party Menu Generator
#######################################

# step 1 - import random and webbroswer module
import random
import webbrowser 


# step 2 - import files and store as list of tuples

def save_file(path):
    open_file = open(f".\menu_files\{path}")
    menu_file = list(open_file)
    menu_file = [(item.strip("\n").split(",")[0],item.strip("\n").split(",")[1]) for item in menu_file]
    open_file.close()
    
    return menu_file

desserts = save_file('desserts.txt')
mains = save_file('mains.txt')
starters = save_file('starters.txt')


# step 3 - define functions to generate a random menu and update a menu item
def gen_randoms(item_1 = starters, item_2 = mains, item_3 = desserts):
    starter = random.choice(item_1)
    main = random.choice(item_2)
    dessert = random.choice(item_3)
    
    return starter, main, dessert

def update_menu(to_update, starter, main, dessert, item_1 = starters, item_2 = mains, item_3 = desserts):
    if to_update == "main":
        main = random.choice(item_2)
    elif to_update == "starter":
        starter = random.choice(item_1)
    else:
        dessert = random.choice(item_3)
        
    return starter, main, dessert


if __name__ == "__main__":
    print("\n\n****************************************************")
    print("\n\nWelcome to the dinner party menu generator:\n\n")
    print("""        _
       |-|
       |~|
       |:|   
      .'.'.
     /   ::\
     |_____|     __          _
     |:.:;.|   <:__:>     .-'o\
     |_____|   \  ::/  .o' O. o\
     |   ::|    '..'  |--o.--o--|
     |   ;:|     ||   |._._o_._.|
     \_____/    .''.
               '----'     """)
    print("****************************************************\n\n")
    starter,main,dessert = gen_randoms()
    print("Your dinner menu is:")
    print(f"Starter: {starter[0]}")
    print(f"Main: {main[0]}")
    print(f"Dessert: {dessert[0]}\n\n")
    
    while True:
        print("Please enter one of the following:")
        print("1. Open recipes")
        print("2. To swap out a menu item")
        print("3. To generate a new menu")
        print("4. Exit")
        print("Please make a sekection from 1 - 4\n")
        user_input = int(input("Please make your selection: "))
        
        if user_input == 1:
            webbrowser.open(starter[1], new=1, autoraise=True)
            webbrowser.open(main[1], new=2, autoraise=True)
            webbrowser.open(dessert[1], new=2, autoraise=True)
            break
        elif user_input == 2:
            user_item = input("Please enter the name of the dish to be swapped - starter, main or desssert").strip().lower()
            starter,main,dessert = update_menu(user_item, starter, main, dessert)            
            print("Your dinner menu is:")
            print(f"Starter: {starter[0]}")
            print(f"Main: {main[0]}")
            print(f"Dessert: {dessert[0]}\n\n")
            continue
        elif user_input == 3:
            print("\nSelecting new menu........")
            print("Your new menu is:")
            starter,main,dessert = gen_randoms()
            print("Your dinner menu is:")
            print(f"Starter: {starter[0]}")
            print(f"Main: {main[0]}")
            print(f"Dessert: {dessert[0]}\n\n")
            continue
        elif user_input == 4:
            print("Goodbye...")
            break
        else:
            print("You did not enter valid input, please try again....\n\n")
            continue
            
            
            
            
    
    