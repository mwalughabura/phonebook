import unittest
import phonebook

class SavePhoneNumber(unittest.TestCase):

	def test_get_name(self):
		result = phonebook.get_name("Mwalugha")
		result.assertTrue(len(name) > 1)

	def test_get_phone_no(self):
		result = phonebook.get_phone_no(58768687)
		result.assertTrue(len(str(58768687)) > 10)

if __name__ == '__main__':
	unittest.main()