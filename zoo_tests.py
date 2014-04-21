from zoo import Zoo
import unittest
from random import randrange
from create_animal_db import create_animal_table
import sqlite3

class TestZoo(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect('animals.db')
        self.cursor = self.conn.cursor()
        create_animal_table(self.cursor)
        self.myZoo = Zoo()
        self.myZoo.capacity = 100
        self.myZoo.budget = 10
        self.myZoo.accommodate('tiger', 'tiggy' + str(randrange(100)), 1, 5, self.cursor)
        self.conn.commit()

    def tearDown(self):
        self.cursor.execute('DROP TABLE animal')

    def test_get_capacity(self):
        self.assertEqual(100, self.myZoo.get_capacity())

    def test_animals_count(self):
        self.assertEqual(1, self.myZoo.count_animals(self.cursor))
        self.myZoo.accommodate('lion', '1', 2, 10, self.cursor)
        self.assertEqual(2, self.myZoo.count_animals(self.cursor))


    def test_get_budget(self):
        self.assertEqual(10, self.myZoo.get_budget())

    def test_table_to_list(self):
        self.myZoo.table_to_list(self.cursor)
        self.assertEqual('tiger', self.myZoo.animals[0].get_species())


    def test_get_income(self):
        self.assertEqual(60, self.myZoo.get_income(self.cursor, 1))

    def test_reproduce(self):
        self.myZoo.reproduce(self.cursor)

    def test_move_to_habbitat(self):
        self.myZoo.move_to_habitat('tiggy', self.cursor)
        self.conn.commit()
        self.assertEqual(0, self.myZoo.count_animals(self.cursor))

if __name__ == '__main__':
    unittest.main()
