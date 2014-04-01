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
        self.assertEqual(['New'], self.myZoo.get_animals())

if __name__ == '__main__':
    unittest.main()
