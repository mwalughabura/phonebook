import unittest
import phonebook

class SavePhoneNumber(unittest.TestCase):

	def test_get_name(self):
		result = phonebook.name("Mwalugha")
		result.assertTrue(len(name) > 1)

	def test_get_phone_no(self):
		pass

if __name__ == '__main__':
	unittest.main()