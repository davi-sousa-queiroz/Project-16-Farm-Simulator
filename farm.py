import time

class Farm:

    def __init__(self, farm_name):

        self.farm_name = farm_name
        self.coins = 0

        self.seeds = self._init_seeds()
        self.crops = self._init_crops()
        self.seed_prices = self._init_seed_prices()
        self.seed_to_crops = self._init_seed_to_crops()

    def _init_seeds(self):
        return {
            "Corn Seeds" : 0,
            "Carrot Seeds" : 0,
            "Watermelon Seeds" : 0,
            "Pumpkin Seeds" : 0,
            "Orange Seeds" : 0,
            "Apple Seeds" : 0,
            "Magic Seeds" : 0}

    def _init_crops(self):
        return {"Corn" : 0,
                "Carrots" : 0,
                "Watermelons" : 0,
                "Pumpkins" : 0,
                "Oranges" : 0,
                "Apples" : 0,
                "Magic Plants" : 0}

    def _init_seed_prices(self):
        return {"Corn Seeds" : 10,
                "Carrot Seeds" : 20,
                "Watermelon Seeds" : 30,
                "Pumpkin Seeds" : 40,
                "Orange Seeds" : 50,
                "Apple Seeds" : 60,
                "Magic Seeds" : 100}

    def _init_seed_to_crops(self):
        return {"Corn Seeds" : "Corn",
                "Carrot Seeds" : "Carrots",
                "Watermelon Seeds" : "Watermelons",
                "Pumpkin Seeds" : "Pumpkins",
                "Orange Seeds" : "Oranges",
                "Apple Seeds" : "Apples",
                "Magic Seeds" : "Magic Plants"
        }

    def view_farm(self):
        farm_name = self.farm_name.capitalize()
        print(f"\n========== {farm_name} ==========")
        print(f"==========\t  Coins: {self.coins}    ===========")
        print("=====================================")

    def view_inventory(self):
        print(f"\n========== SEEDS ==========")
        for key, value in self._init_seeds().items():
            print(f"{key}: {value}")
        print("\n========== CROPS ==========")
        for key, value in self._init_crops().items():
            print(f"{key}: {value}")