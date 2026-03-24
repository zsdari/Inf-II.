import unittest
from password_check import LengthFilter, SpecialCharFilter, AndFilter


class PassTestCase(unittest.TestCase):
    def test_lenght_filter_if_password_is_ok(self):
        lenght_filter = LengthFilter()
        result = lenght_filter.validate("12345678")
        self.assertEqual([],result)

    def test_lenght_filter_if_password_is_not_ok(self):
        lenght_filter = LengthFilter(8)
        result = lenght_filter.validate("123")
        self.assertTrue(len(result)>0)

    def test_special_char_if_not_ok(self):
        special_char_filter = SpecialCharFilter()
        result = special_char_filter.validate("abcdefghij")
        self.assertTrue(len(result)>0)

    def test_special_char_if_ok(self):
        special_char_filter = SpecialCharFilter()
        result = special_char_filter.validate("abcd.e,fg*hij")
        self.assertEqual([],result)

    def test_and_if_not_ok(self):
        filters = []
        special_char_filter = SpecialCharFilter()
        filters.append(special_char_filter)
        lenght_filter = LengthFilter(8)
        filters.append(lenght_filter)
        and_filter = AndFilter(filters)
        result = and_filter.validate("abcdefghij")
        self.assertTrue(len(result)>0)
        result = and_filter.validate("ab.")
        self.assertTrue(len(result) > 0)

    def test_and_if_ok(self):
        filters = []
        special_char_filter = SpecialCharFilter()
        filters.append(special_char_filter)
        lenght_filter = LengthFilter(8)
        filters.append(lenght_filter)
        and_filter = AndFilter(filters)
        result = and_filter.validate("abcd.e,fghij")
        self.assertEqual([],result)

    def test_or_if_not_ok(self):
        filters = []

if __name__ == '__main__':
    unittest.main()
