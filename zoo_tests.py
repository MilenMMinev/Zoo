from zoo import Zoo
import unittest


class TestZoo(unittest.TestCase):

    def setUp(self):
        self.myZoo = Zoo()
        self.myZoo.capacity = 100
        self.myZoo.budget = 10
        self.myZoo.animals.append('Tiger')

    def test_get_capacity(self):
        self.assertEqual(100, self.myZoo.get_capacity())

    def test_get_budget(self):
        self.assertEqual(10, self.myZoo.get_budget())

    def test_get_animals(self):
        self.assertEqual(['Tiger'], self.myZoo.get_animals())

#    def test_give_birth(self):
#        self.assertEqual(1, self.myZoo.give_birth())

#    def test_accommodate(self):
#        self.myZoo.accommodate('horse', 'horsy', 2, 10)

    def test_get_income(self):
        self.assertEqual(180, self.myZoo.get_income())


if __name__ == '__main__':
    unittest.main()
