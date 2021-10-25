import unittest


def alphanumeric_sort(value):
    numbs = []
    lowercase = []
    uppercase = []
    sort_list = []

    for char in value:
        if (char.islower()):
            lowercase.append(char)

        if (char.isnumeric()):
            numbs.append(char)

        if (char.isupper()):
            uppercase.append(char)

    sort_list.extend(sorted(numbs))

    sort_list.extend(sorted(lowercase))

    sort_list.extend(sorted(uppercase))

    return ''.join(sort_list)


class TestAlphaNumericSort(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(alphanumeric_sort('i11u6'), '116iu')

    def test_case_2(self):
        self.assertEqual(alphanumeric_sort('ai66u9'), '669aiu')


    unittest.main()
