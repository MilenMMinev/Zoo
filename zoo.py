import sqlite3
from random import randrange


class Zoo():

    def __init__(self):
        self.capacity = 0
        self.budget = 0
        self.animals = []
        self.species_list = ['lion', 'tiger', 'red panda', 'kangaroo', 'koala',
                'raccoon', 'baboon', 'impala', 'hippo', 'cougar', 'goat']

    def get_capacity(self):
        return self.capacity

    def get_budget(self):
        return self.budget

    def get_animals(self):
        return self.animals

    def get_income(self):
        conn = sqlite3.connect('animal.db')
        cursor = conn.cursor()
        income = 0
        result = cursor.execute('SELECT name FROM animals WHERE name != 0')
        for row in result:
            income += 60
        return income

    def get_newborn_weight(self, species):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        query = 'SELECT newborn_weight FROM animals WHERE species = ?'
        result = cursor.execute(query, (species, ))
        for item in result:
            return item[0]

    def generate_random_gender(self):
        fate = randrange(2)
        if fate == 0:
            return 'male'
        else:
            return 'female'

    def create_kid(self, species):
        conn = sqlite3.connect('animal.db')
        cursor = conn.cursor()
        query = 'INSERT INTO animals (species, age, name, gender, weight) VALUES(?, 0, ?, ?, ?)'
        cursor.execute(query,
                       (species, 'Mnew', self.generate_random_gender(), self.get_newborn_weight(species)))
        conn.commit()
        conn.close()

    def give_birth(self):
        conn = sqlite3.connect('animal.db')
        cursor = conn.cursor()
        for species in self.species_list:
            male = False
            female = 0
            query = 'SELECT gender FROM animals WHERE species = ?'
            result = cursor.execute(query, (species,))
            for animal in result:
                if animal[0] == 'male':
                    male = True
                if animal[0] == 'female':
                    female += 1
            if male:
                for kids in range(female):
                    self.create_kid(species)

    def accommodate(self, species, name, age, weight):
        if randrange(2) == 1:
            gender = 'male'
        else:
            gender = 'female'
        query = 'INSERT INTO animals VALUES(?, ?, ?, ?, ?)'
        self.cursor.execute(query, (species, name, age, gender, weight))
        self.conn.commit()
        self.conn.close()
