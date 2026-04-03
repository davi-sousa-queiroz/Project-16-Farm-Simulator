import time

class Farm:

    def __init__(self, farm_name):

        self.farm_name = farm_name
        self.coins = 0

        self.seeds = self._init_seeds()
        self.crops = self._init_crops()
        self.seed_prices = self._init_seed_prices()
        self.seed_to_crops = self._init_seed_to_crops()
        self.seed_rewards = self._init_seed_rewards()
        self.crop_prices = self._init_crop_prices()

    def _init_seeds(self):
        return {
            "Corn Seeds": 1,
            "Carrot Seeds": 0,
            "Watermelon Seeds": 0,
            "Pumpkin Seeds": 0,
            "Orange Seeds": 0,
            "Apple Seeds": 0,
            "Magic Seeds": 0
        }

    def _init_crops(self):
        return {
            "Corn": 0,
            "Carrots": 0,
            "Watermelons": 0,
            "Pumpkins": 0,
            "Oranges": 0,
            "Apples": 0,
            "Magic Plants": 0
        }

    def _init_seed_prices(self):
        return {
            "Corn Seeds": 10,
            "Carrot Seeds": 20,
            "Watermelon Seeds": 30,
            "Pumpkin Seeds": 40,
            "Orange Seeds": 50,
            "Apple Seeds": 60,
            "Magic Seeds": 100
        }

    def _init_seed_to_crops(self):
        return {
            "Corn Seeds": "Corn",
            "Carrot Seeds": "Carrots",
            "Watermelon Seeds": "Watermelons",
            "Pumpkin Seeds": "Pumpkins",
            "Orange Seeds": "Oranges",
            "Apple Seeds": "Apples",
            "Magic Seeds": "Magic Plants"
        }

    def _init_seed_rewards(self):
        return {
            "Corn Seeds": {"crop": 1, "seeds": 3},
            "Carrot Seeds": {"crop": 1, "seeds": 3},
            "Watermelon Seeds": {"crop": 1, "seeds": 3},
            "Pumpkin Seeds": {"crop": 1, "seeds": 3},
            "Orange Seeds": {"crop": 1, "seeds": 3},
            "Apple Seeds": {"crop": 1, "seeds": 3},
            "Magic Seeds": {"crop": 1, "seeds": 3}
        }

    def _init_crop_prices(self):
        return {
            "Corn" : 15,
            "Carrots" : 25,
            "Watermelons" : 40,
            "Pumpkins" : 55,
            "Oranges" : 70,
            "Apples" : 85,
            "Magic Plants" : 150,

        }

    def view_farm(self):
        farm_name = self.farm_name.capitalize()
        print(f"\n========== {farm_name} ==========")
        print(f"==========   Coins: {self.coins}   ==========")
        print("=================================")

    def view_inventory(self):
        print("\n========== SEEDS ==========")
        for key, value in self.seeds.items():
            print(f"{key}: {value}")

        print("\n========== CROPS ==========")
        for key, value in self.crops.items():
            print(f"{key}: {value}")

    def plant(self):
        seeds_list = list(self.seeds.keys())

        print("\n========== PLANT ==========")
        for index, (seed, quantity) in enumerate(self.seeds.items(), start=1):
            print(f"{index:>2}. {seed:<17} | {quantity} |")

        print("\nSelect a seed to plant!")

        try:
            choice = int(input("\n>> "))
        except:
            print("Invalid input")
            return

        if not (1 <= choice <= len(seeds_list)):
            print("\nPlease select a valid seed!")
            return

        selected_seed = seeds_list[choice - 1]

        if self.seeds[selected_seed] <= 0:
            print("\nYou don't have that seed 😕")
            return

        print(f"\nYou selected: {selected_seed}")

        # remove seed
        self.seeds[selected_seed] -= 1

        # simulate growth
        print("\nPlanting...")
        time.sleep(3)

        print("Watering...")
        time.sleep(1)

        print("Growing...")
        time.sleep(1)

        print("Harvesting...")
        time.sleep(1)

        print("Done! 🌾")

        # rewards
        crop_name = self.seed_to_crops[selected_seed]
        reward = self.seed_rewards[selected_seed]

        self.crops[crop_name] += reward["crop"]
        self.seeds[selected_seed] += reward["seeds"]

        print(f"\nYOU GREW A {crop_name}! 🌱")
        print(f"+{reward['crop']} {crop_name}")
        print(f"+{reward['seeds']} {selected_seed}")

    def sell(self):

        print("\n========== SELL ==========")
        print("1. Sell Seeds")
        print("2. Sell Crops")

        choice = input("\n>> ")

        if choice == "1":
            items = self.seeds
            prices = self.seed_prices
        elif choice == "2":
            items = self.crops
            prices = self.crop_prices
        else:
            print("Invalid choice")
            return

        items_list = list(items.keys())

        print("\nWhat do you want to sell?")
        for i, (name, qty) in enumerate(items.items(), start=1):
            print(f"{i}. {name:<17} | {qty} | Price: {prices[name]}")

        try:
            selection = int(input("\n>> "))
        except:
            print("Invalid input")
            return

        if not (1 <= selection <= len(items_list)):
            print("Invalid selection")
            return

        selected_item = items_list[selection - 1]

        if items[selected_item] <= 0:
            print("\nYou don't have any 😕")
            return

        try:
            amount = int(input("How many? >> "))
        except:
            print("Invalid amount")
            return

        if amount <= 0 or amount > items[selected_item]:
            print("Invalid amount")
            return

        total = amount * prices[selected_item]

        items[selected_item] -= amount
        self.coins += total

        print(f"\nSold {amount} {selected_item} for {total} coins 💰")

    def shop(self):

        print("\n========== SHOP ==========")
        print(f"Coins: {self.coins} 💰")

        seeds_list = list(self.seeds.keys())

        print("\nAvailable Seeds:")
        for i, (seed, price) in enumerate(self.seed_prices.items(), start=1):
            print(f"{i}. {seed:<17} | Price: {price}")

        try:
            choice = int(input("\nSelect seed to buy >> "))
        except:
            print("Invalid input")
            return

        if not (1 <= choice <= len(seeds_list)):
            print("Invalid choice")
            return

        selected_seed = seeds_list[choice - 1]
        price = self.seed_prices[selected_seed]

        print(f"\nSelected: {selected_seed} ({price} coins each)")

        try:
            amount = int(input("How many? >> "))
        except:
            print("Invalid amount")
            return

        if amount <= 0:
            print("Invalid amount")
            return

        total_cost = amount * price

        if self.coins < total_cost:
            print("\nNot enough coins 😕")
            return

        self.coins -= total_cost
        self.seeds[selected_seed] += amount

        print(f"\nBought {amount} {selected_seed} for {total_cost} coins 💰")