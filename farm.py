class Farm:

    def __init__(self, farm_name):

        self.farm_name = farm_name
        self.coins = 0

        self.seeds = self._init_seeds()
        self.crops = self._init_crops()
        self.seed_prices = self._init_seed_prices()

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