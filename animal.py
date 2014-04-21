from random import randrange
import sqlite3

class Animal():

    """docstring for Animal"""

    def __init__(self, name, species, gender, age, weight):
        self.name = name
        self.species = species
        self.gender = gender
        self.age = age
        self.weight = weight
        self.cooldown = 0
        self.gestation = self.get_gestation_period()
        self.is_pregnant = False

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age // 365# in years

    def get_weight(self):
        return self.weight

    def increase_age(self, interval):
        self.age += interval # in days

    def increase_weight(self, interval):
        self.weight += self.get_age_weight_ratio() * interval / 30

    def get_age_weight_ratio(self):
        conn = sqlite3.connect("animals.db")
        cursor = conn.cursor()
        query = 'SELECT weight_age_ratio FROM animals WHERE species = ?'
        result = cursor.execute(query, (self.species,)).fetchone()
        return result[0]

    def get_average_weight(self, cursor):
        query = 'SELECT average_weight FROM animals WHERE species = ?'
        result = cursor.execute(query, (self.species,)).fetchone()
        return result[0]

    def grow(self, interval, cursor):
        self.increase_age(interval)
        self.increase_weight(interval)
        if self.get_weight() > self.get_average_weight(cursor):
            self.weight = self.get_average_weight(cursor)
        query = 'UPDATE animal SET age = ?, weight = ? WHERE name = ?'
        cursor.execute(query, (self.age, self.get_weight(), self.get_name()))

    def get_food_type(self):
        conn = sqlite3.connect("animals.db")
        cursor = conn.cursor()
        query = 'SELECT food_type FROM animals WHERE species = ?'
        result = cursor.execute(query, (self.species,)).fetchone()
        return result[0]

    def get_food_weight_ratio(self):
        conn = sqlite3.connect("animals.db")
        cursor = conn.cursor()
        query = 'SELECT food_weight_ratio FROM animals WHERE species = ?'
        result = cursor.execute(query, (self.species,)).fetchone()
        return result[0]

    def eat(self, interval):  # this should return the amount of food eaten by an animal in $$$
        if self.get_food_type() == 'carnivore':
            return self.get_weight() * self.get_food_weight_ratio() * 4 * interval
        if self.get_food_type() == 'herbivore':
            return self.get_weight() * self.get_food_weight_ratio() * 2 * interval

    def get_life_expectancy(self):
        conn = sqlite3.connect("animals.db")
        cursor = conn.cursor()
        query = 'SELECT life_expectancy FROM animals WHERE species = ?'
        result = cursor.execute(query, (self.species,)).fetchone()
        return result[0] 

    def die(self):
        if self.get_age() >= randrange(self.get_life_expectancy()):
            return True
        return False


    def get_gestation_period(self):
        conn = sqlite3.connect("animals.db")
        cursor = conn.cursor()
        query = 'SELECT gestation FROM animals WHERE species = ?'
        result = cursor.execute(query, (self.species,)).fetchone()
        return result[0]

