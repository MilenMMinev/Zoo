import unittest
from animal import Animal


class TestAnimals(unittest.TestCase):
	def setUp(self):
		self.tiger = Animal()
		self.tiger.gender = 'male'
		self.tiger.species = 'tiger'
		self.tiger.age = 0
		self.tiger.name = 'Tiger'
		self.tiger.weight = 5
		

	def test_getGender(self):
		self.assertEqual('male', self.tiger.get_gender())


	def test_getSpecies(self):
		self.assertEqual('tiger', self.tiger.get_species())

	def test_getAge(self):
		self.assertEqual(0, self.tiger.get_age())

	def test_getName(self):
		self.assertEqual('Tiger', self.tiger.get_name())
		
	def test_getWeight(self):
		self.assertEqual(5, self.tiger.get_weight())

	def test_grow(self):
		self.tiger.grow(2)
		self.assertEqual(9, self.tiger.weight)
		self.assertEqual(2, self.tiger.age)

if __name__ == '__main__':
	unittest.main()
	
