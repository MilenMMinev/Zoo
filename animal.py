from random import randrange
import sqlite3


class Animal():

    """docstring for Animal"""

    def __init__(self, name, species, gender, age, weight):
        super(Animal, self).__init__()
        self.name = name
        self.species = species
        self.gender = gender
        self.age = age
        self.weight = weight

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight

    def increase_age(self, period):
        self.age += period

    def increase_weight(self, period):
        self.weight += self.get_age_weight_ratio() * period

    def get_age_weight_ratio(self):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        query = 'SELECT weight_age_ratio FROM animals WHERE species = ?'
        result = cursor.execute(query, (self.species,))
        for ratio in result:
            return ratio[0]

    def get_average_weight(self):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        query = 'SELECT average_weight FROM animals WHERE species = ?'
        result = cursor.execute(query, (self.species,))
        for weight in result:
            return weight[0]

    def grow(self, period):
        self.increase_age(period)
        self.increase_weight(period)
        if self.get_weight() > self.get_average_weight():
            self.weight = self.get_average_weight()

    def get_food_type(self):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        query = 'SELECT food_type FROM animals WHERE species = ?'
        result = cursor.execute(query, (self.species,))
        for food_type in result:
            return food_type[0]

    def get_food_weight_ratio(self):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        query = 'SELECT food_weight_ratio FROM animals WHERE species = ?'
        result = cursor.execute(query, (self.species,))
        for ratio in result:
            return ratio[0]

    def eat(self):  # this should return the amount of food eaten in $$$
        if self.get_food_type() == 'carnivore':
            return self.get_weight() * self.get_food_weight_ratio() * 4
        if self.get_food_type() == 'herbivore':
            return self.get_weight() * self.get_food_weight_ratio() * 2

    def get_life_expectancy(self):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        query = 'SELECT life_expectancy FROM animals WHERE species = ?'
        result = cursor.execute(query, (self.species,))
        for ratio in result:
            return ratio[0]

    def die(self):
        if self.get_age() >= randrange(self.get_life_expectancy()):
            return True
        return False