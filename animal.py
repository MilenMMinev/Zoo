class Animal():
    def __init__(self):
        self.species = ' '
        self.age = 0
        self.name = ' '
        self.gender = ' '
        self.weight = 0

    def get_species(self):
        return self.species

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_weight(self):
        return self.weight


    def increase_age(self, period):
        self.age += period

    def increase_weight(self, amound):
        self.weight += amound

 
    def grow(self, period):
        self.increase_age(period)
        def increase_weight(self, period):
            querry = 'FROM animals SELECT average_weight WHERE species = ?'
            average_weight = execute(querry, (self.species,))
            if self.weight < average_weight:
                self,weight += period * ratio
                
            self.increase_weight(period * 2)



    def eat(self, food):








