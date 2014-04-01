class Zoo():

    def __init__(self):
        self.capacity = 0
        self.budget = 0
        self.animals = []

    def get_capacity(self):
        return self.capacity

    def get_budget(self):
        return self.budget

    def get_animals(self):
        return self.animals

    def get_income(self):
        return len(self.animals) * 60
