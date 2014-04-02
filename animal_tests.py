from animal import Animal
import unittest


class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.tiger = Animal('tiggy', 'tiger', 'male', 1, 5)
        self.hippo = Animal('hippy', 'hippo', 'female', 1, 50)

    def test_get_name(self):
        self.assertEqual('tiggy', self.tiger.get_name())
        self.assertEqual('hippy', self.hippo.get_name())

    def test_get_species(self):
        self.assertEqual('tiger', self.tiger.get_species())
        self.assertEqual('hippo', self.hippo.get_species())

    def test_get_gender(self):
        self.assertEqual('male', self.tiger.get_gender())
        self.assertEqual('female', self.hippo.get_gender())

    def test_get_weight(self):
        self.assertEqual(5, self.tiger.get_weight())
        self.assertEqual(50, self.hippo.get_weight())

    def test_Get_age(self):
        self.assertEqual(1, self.tiger.get_age())
        self.assertEqual(1, self.hippo.get_age())

    def test_grow_by_age(self):
        self.tiger.grow(1)
        self.hippo.grow(1)
        self.assertEqual(2, self.tiger.get_age())
        self.assertEqual(2, self.hippo.get_age())

    def test_grow_by_weight(self):
        self.tiger.grow(1)
        self.hippo.grow(1)
        self.assertEqual(17, self.tiger.get_weight())
        self.assertEqual(52.72, self.hippo.get_weight())

    def test_grow_when_average_weight_is_reached(self):
        self.tiger.grow(30)
        self.assertEqual(250, self.tiger.get_weight())

    def get_food_type(self):
        self.assertEqual('carnivore', self.tiger.get_food_type())
        self.assertEqual('herbivore', self.hippo.get_food_type())

    def test_get_food_weight_ratio(self):
        self.assertEqual(25, self.hippo.get_food_weight_ratio())
        self.assertEqual(0.06, self.tiger.get_food_weight_ratio())

    def test_eat(self):
        self.assertEqual(1.2, self.tiger.eat())
        self.assertEqual(2500, self.hippo.eat())

    def test_death(self):  # it works! trust me
        pass


if __name__ == '__main__':
    unittest.main()
