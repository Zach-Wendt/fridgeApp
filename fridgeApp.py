import csv

def main():
    with open('fridge.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
    print("\n")
    print("Welcome to the fridge!")
    print("\n")
    print("What would you like to do?")
    print("\n")
    print("1. Add a new item to the fridge")
    print("2. Remove an item from the fridge")
    print("3. Edit an item in the fridge")
    print("4. View the fridge")
    print("5. Exit")
    print("\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        edit_item()
    elif choice == 4:
        view_fridge()
    elif choice == 5:
        exit()
    else:
        print("Invalid choice")
        main()

def add_item():
    with open('fridge.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        name = input

main()