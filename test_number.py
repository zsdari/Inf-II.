import unittest
from practice0324 import RandomNumber, EvenNumber, FileNumbers

class RandomNumberTestCase(unittest.TestCase):
    def test_random_numbers(self):
        random_generator = RandomNumber()
        number = random_generator.get_number()
        self.assertIsInstance(number, float) # add assertion here

        count = 5
        while count > 0:
            number = next(random_generator)
            self.assertIsInstance(number, float)
            count -= 1

        count = 5
        for number in random_generator:
            if count == 0:
                break
            self.assertIsInstance(number, float)
            count -= 1

class EvenNumberTestCase(unittest.TestCase):
    def test_even_numbers(self):
        even_number_generator = EvenNumber()
        number = even_number_generator.get_number()
        self.assertIsInstance(number, float) # add assertion here

        count = 5
        while count > 0:
            number = next(even_number_generator)
            self.assertEqual(number%2, 0)
            count -= 1

        count = 5
        for number in even_number_generator:
            if count == 0:
                break
            self.assertEqual(number % 2, 0)
            count -= 1

    def test_even_numbers_list(self):
        excepted = [2,4,6,8,10]
        numbers = []
        even_number_generator = EvenNumber()
        for _ in range(5):
            numbers.append(next(even_number_generator))
        self.assertEqual(excepted, numbers)

class FileNumberTestCase(unittest.TestCase):
    def test_file_numbers(self):
        file_number_generator = FileNumbers("data.dat")
        for number in file_number_generator:
            self.assertIsInstance(number, float)

if __name__ == '__main__':
    unittest.main()
