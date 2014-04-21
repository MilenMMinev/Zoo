import sqlite3
from random import randrange
from animal import Animal

class Zoo():

    def __init__(self):
        self.capacity = 100
        self.budget = 2000
        self.animals = []
        self.species_list = ['lion', 'tiger', 'red panda', 'kangaroo', 'koala',
                             'raccoon', 'baboon', 'impala', 'hippo', 'cougar', 'goat']

    def get_capacity(self):
        return self.capacity

    def get_budget(self):
        return self.budget

    def get_animals(self):
        return self.animals

    def table_to_list(self, cursor):
        self.animals = []
        result = cursor.execute('SELECT * FROM animal')
        for item in result:
            self.animals.append(Animal(item[0], item[1], item[2], item[3], item[4]))
    
    def get_income(self, cursor, interval):
        return self.count_animals(cursor) * 60 * interval

    def get_newborn_weight(self, species, cursor):
        query = 'SELECT newborn_weight FROM animals WHERE species = ?'
        result = cursor.execute(query, (species, ))
        for item in result:
            return item[0]

    def get_gestation_period(self, species, cursor):
        query = 'SELECT gestation FROM animals WHERE species = ?'
        result = cursor.execute(query, (species,)).fetchone()
        return result[0]


    def generate_random_gender(self):
        fate = randrange(2)
        if fate == 0:
            return 'male'
        else:
            return 'female'


    def get_animals_in_zoo(self, cursor):
        names = []
        result = cursor.execute('SELECT name FROM animal')
        for item in result:
            names.append(item[0])
        return names


    def is_there_male(self, species, cursor):
            query = 'SELECT gender FROM animal WHERE species = ? and gender = ?'
            result = cursor.execute(query, (species, 'male')).fetchone()
            return result != None

    def decrease_cooldown(self, interval, cursor):
        query = 'UPDATE animal SET cooldown = cooldown - ? WHERE cooldown > 0'
        cursor.execute(query, (interval,))


    def reproduce(self, cursor):
        for species in self.species_list:
            if self.is_there_male(species, cursor):
                query = 'UPDATE animal SET is_pregnant = 1 WHERE gender = ? and cooldown <= ? and species = ?'
                result = cursor.execute(query, ('female', 0, species))



    def carry_child(self, interval, cursor):
        query = 'UPDATE animal SET gestation = gestation - ? WHERE is_pregnant = 1'
        cursor.execute(query, (interval, ))


    def create_baby(self, species, cursor):
        print('Congratulations a baby was born!')
        baby_name ='baby' + str(randrange(1000))
        query = 'INSERT INTO animal (name, species, gender, age, weight, cooldown, gestation, is_pregnant) VALUES(?, ?, ?, 0, ?, 0, ?, 0)'
        cursor.execute(query,
                       (baby_name, species, self.generate_random_gender(),
                        self.get_newborn_weight(species, cursor),
                         30 * self.get_gestation_period(species, cursor)))


    def give_birth(self, cursor):
        for species in self.species_list:
            select_query = 'SELECT COUNT(*) FROM animal WHERE species = ? and gestation <= 0 and is_pregnant = 1'
            result = cursor.execute(select_query, (species,)).fetchone()
            update_query = 'UPDATE animal SET is_pregnant = 0, cooldown = 180, gestation = ? WHERE species = ? and gestation <= 0 and is_pregnant = 1'
            cursor.execute(update_query, (self.get_gestation_period(species, cursor), species))
            for animal in range(result[0]):
                if self.count_animals(cursor) < self.get_capacity():
                    self.create_baby(species, cursor)

    def count_animals(self, cursor):
        result = cursor.execute('SELECT COUNT(*) FROM animal').fetchone()
        return result[0]
                    

    def accommodate(self, species, name, age, weight, cursor):
        if randrange(2) == 1:
            gender = 'male'
        else:
            gender = 'female'
        query = 'INSERT INTO animal VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
        cursor.execute(query,
        (name, species, gender, age * 365, weight, 0, self.get_gestation_period(species, cursor) * 30, -1))

    def move_to_habitat(self, name, cursor):
        delete_query = 'DELETE FROM animal WHERE name = ?'
        cursor.execute(delete_query, (name,))
