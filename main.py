from farm import Farm

def menu():
    print("\n1. View Farn")
    print("2. Plant")
    print("3. Sell")
    print("4. Shop")
    print("5. View Inventory")
    print("6. Quit")

def main():
    print("\nName your farm!")
    farm_name = input("\n>> ")
    farm = Farm(farm_name)
    while True:
        menu()
        choice = input("\n>> ")
        if choice == "1":
            farm.view_farm()
        elif choice == "2":
            farm.plant()
        elif choice == "3":
            farm.sell()
        elif choice == "4":
            farm.shop()
        elif choice == "5":
            farm.view_inventory()
        elif choice == "6":
            print("Thank you for playing Farm Simulator!!")
            break
        else:
            print("\nEnter a valid option! (1-6)")

if __name__ == "__main__":
    main()